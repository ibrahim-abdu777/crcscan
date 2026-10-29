import unittest
import zlib
from src.crcscan import scan


def tagged(s):
    return f"{s} crc={zlib.crc32(s.encode()) & 0xFFFFFFFF:08x}"


class TestScan(unittest.TestCase):
    def test_good_line_passes(self):
        self.assertEqual(scan([tagged("hello world")]), [])

    def test_bad_line_flagged(self):
        self.assertEqual(scan(["hello world crc=deadbeef"]), [0])


if __name__ == "__main__":
    unittest.main()
