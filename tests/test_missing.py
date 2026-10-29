import unittest
from src.crcscan import scan


class TestMissing(unittest.TestCase):
    def test_lines_without_crc_ignored(self):
        self.assertEqual(scan(["plain line", "another"]), [])


if __name__ == "__main__":
    unittest.main()
