import fs from 'fs';
const html = fs.readFileSync('verifier.html','utf8');
const start = html.indexOf('/* <core>');
const end = html.indexOf('/* </core>');
const src = html.slice(start, end);
const CORE = eval(src + '; CORE');

function load(dir){
  const f={};
  for (const n of fs.readdirSync(dir)) f[n]=fs.readFileSync(dir+'/'+n,'utf8');
  return f;
}
const good = load('/tmp/pkt');
const r1 = await CORE.verify(good);
console.log('TEST 1 (valid packet) ->', r1.verdict, '| events', r1.stats.events, '| gaps', r1.stats.gaps);
for (const f of r1.findings) console.log('   ', f.level.toUpperCase().padEnd(4), f.check.padEnd(16), f.detail);

// TEST 2: tamper with one event's payload but leave the stored hash
const lines = good['events.jsonl'].trim().split('\n').map(JSON.parse);
lines[3].payload.approver = 'Someone Else';
const tampered = Object.assign({}, good, {'events.jsonl': lines.map(e=>JSON.stringify(e)).join('\n')+'\n'});
const r2 = await CORE.verify(tampered);
console.log('\nTEST 2 (payload edited after the fact) ->', r2.verdict);
for (const f of r2.findings.filter(f=>f.level!=='ok')) console.log('   ', f.level.toUpperCase().padEnd(4), f.check.padEnd(16), f.detail);

// TEST 3: delete an event (a hole in the record)
const holed = Object.assign({}, good, {'events.jsonl': good['events.jsonl'].trim().split('\n').filter((_,i)=>i!==3).join('\n')+'\n'});
const r3 = await CORE.verify(holed);
console.log('\nTEST 3 (one event removed) ->', r3.verdict);
for (const f of r3.findings.filter(f=>f.level!=='ok')) console.log('   ', f.level.toUpperCase().padEnd(4), f.check.padEnd(16), f.detail);

// TEST 4: companion report swapped
const swapped = Object.assign({}, good, {'report.md': '# Report\n\nNothing to see here.\n'});
const r4 = await CORE.verify(swapped);
console.log('\nTEST 4 (report file swapped) ->', r4.verdict);
for (const f of r4.findings.filter(f=>f.level!=='ok')) console.log('   ', f.level.toUpperCase().padEnd(4), f.check.padEnd(16), f.detail);

// TEST 5: decisions with no approvals recorded
const noapp = Object.assign({}, good, {'events.jsonl': good['events.jsonl'].trim().split('\n').filter(l=>!l.includes('human_approval')).join('\n')+'\n'});
const r5 = await CORE.verify(noapp);
console.log('\nTEST 5 (approval event stripped) ->', r5.verdict);
for (const f of r5.findings.filter(f=>f.level!=='ok')) console.log('   ', f.level.toUpperCase().padEnd(4), f.check.padEnd(16), f.detail);
