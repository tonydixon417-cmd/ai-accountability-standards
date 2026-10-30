# Accountability standards — and one thing you can run

**Anthony Cyle Dixon · 30 October 2026 · Contrail Equity Strategies LLC**

I spent a year writing about why AI systems leave no trustworthy record of what
they did. This repository is the work: the file formats, the verifier, the
papers, and the failures that produced them.

Start with the thing that runs. Everything else here is depth for people who
want it.

---

## Run it in 30 seconds

**[verifier.html](incident-packet-verifier/verifier.html)** — download it, open it
in any browser, drop the sample packet from
[`incident-packet-verifier/examples/packet`](incident-packet-verifier/examples/packet)
on the page.

A valid packet prints `INTACT`. Edit one character in `events.jsonl`, drop it
again, and it prints `FAILED` with the check that caught you. No install, no
build, no network, no account.

How it works: a packet is a folder of files. Every event carries a hash. Each
hash chains to the previous one. A manifest seals the set. Anyone holding the
folder can prove nothing changed after sealing, **without trusting the party
that produced it.**

What it does not do: prove the recording was complete or honest. It proves the
record you are holding is the record that was sealed. That is a smaller claim
than most vendors make and it is the only one this tool can support.

See [`incident-packet-verifier/`](incident-packet-verifier/) for the format spec,
the verifier requirements, and a headless test suite that passes one valid packet
and catches four kinds of tampering.

## Two gates

[`tools/`](tools/) holds the two utilities I built to stop my own failures.

`claim_audit.py` refuses to ship a draft whose factual claims have no logged
receipt. `publish_gate.py` builds a release from an explicit file list and
refuses if it finds health data, third-party names, personal finance, email
addresses, or credentials. Both are public domain and both exist because those
mistakes were made for real.

## The papers

Forty-nine documents, written 2025 into 2026, most of them half a step behind an
error that had just reached someone.

**Accountability architecture**
[AIBB v2.5](AIBB_Whitepaper_v2.5.md) ·
[Loop Detector v1.3](Loop_Detector_Whitepaper_v1.3.md) ·
[The Missing CVR](Missing_CVR_Whitepaper_v1.2.md) ·
[ZeroTX v2.0](ZeroTX_Whitepaper_v2.0.md) ·
[Ethics Floor v2.0](Ethics_Floor_Whitepaper_v2.0.md)

**Identity and portability**
[PIL Paradigm Paper](PIL_Paradigm_Paper_v1.0.md) ·
[PIL v1.2](PIL_Whitepaper_v1.2.md) ·
[PIL Training Layer v2.0](PIL_Training_Layer_Whitepaper_v2.0.md) ·
[Isomorphic Architecture](Isomorphic_Architecture_PIL_Whitepaper_v0.2.md)

**Institutions and oversight**
[CAAO job description](CAAO_Job_Description_Template_v1.0.md) ·
[Covenant Warning System](Covenant_Warning_System_v1.0.md) ·
[Distributed Oversight Model](Distributed_Oversight_Model_v1.0.md) ·
[Early Warning Channel](Early_Warning_Channel_v1.0.md)

**Aviation as the reference case**
[AI Preflight Briefing](AI_Preflight_Briefing_Standard_v1.0.md) ·
[Check Ride Protocol](Check_Ride_Protocol_v1.0.md) ·
[AI Type Rating Framework](AI_Type_Rating_Framework_v1.0.md) ·
[Aviation AI Translation Stack](Aviation_AI_Translation_Stack.md)

**Reference implementation** — [`reference_stack/`](reference_stack/) is runnable
Python: a minimal AIBB, a gateway, a PIL module, and tests. Start with
[`demo.py`](reference_stack/demo.py).

## What this is not

- Not adopted. No regulator, standards body, or company uses any of it. There is
  no pilot program and no customer.
- Not peer-reviewed. One person wrote it.
- Not funded, not a company, not for sale.
- Not complete. Several documents describe systems that exist only as
  specification, and the ones that blur that line are wrong to do so.

## Status of the record

Versions through June 2026 were deposited to Zenodo. In October 2026 that
account was closed and those deposits were removed; most of their identifiers no
longer resolve. The one surviving record is
[10.5281/zenodo.20883473](https://doi.org/10.5281/zenodo.20883473).

Git is the durable copy now. A repository can be forked by anyone, which is the
only property that matters when the previous host deletes your work.

## License

The verifier and the tools are public domain, CC0 1.0. Use them, fork them,
sell them, no attribution needed.

The papers are published here for reading and citation. Their copyright is
registered to the author and they are not licensed for commercial
redistribution.
