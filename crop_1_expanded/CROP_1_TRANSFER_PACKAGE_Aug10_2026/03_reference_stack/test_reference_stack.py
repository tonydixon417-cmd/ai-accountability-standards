import tempfile
import unittest
from pathlib import Path

from .aibb import AIBBRecorder
from .durable_archive import DurableArchive
from .gateway import ActionGateway
from .pil import PILStore


class ReferenceStackTests(unittest.TestCase):
    def test_aibb_chain_detects_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            recorder = AIBBRecorder(path)
            recorder.record("output", {"text": "draft"})
            self.assertTrue(recorder.verify_chain())
            path.write_text(path.read_text().replace("draft", "altered"))
            self.assertFalse(recorder.verify_chain())

    def test_pil_preserves_human_correction(self):
        store = PILStore()
        store.add_scar("recalled number", "query the source first")
        self.assertTrue(store.contains_correction("query the source first"))

    def test_gateway_blocks_high_risk_without_approval(self):
        gateway = ActionGateway(approved_max="low")
        blocked = gateway.evaluate("send_payment", "high")
        approved = gateway.evaluate("send_payment", "high", human_approved=True)
        self.assertFalse(blocked.allowed)
        self.assertTrue(approved.allowed)

    def test_durable_archive_survives_reopen(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "continuity.sqlite3"
            archive = DurableArchive(path)
            archive.put("identity", {"authority": "human"})
            archive.close()

            reopened = DurableArchive(path)
            self.assertEqual(reopened.get("identity"), {"authority": "human"})
            reopened.close()


if __name__ == "__main__":
    unittest.main()
