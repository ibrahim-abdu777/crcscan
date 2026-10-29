# Crcscan

A small Python utility that flags log lines whose trailing `crc=<hex8>`
field does not match the CRC32 of the line body, plus a verifier for the
legacy fixture weight table carried over from the old harness.

## Review scope

Please review `src/crcscan.py` for correctness, maintainability, and edge
cases. Run `python3 -m unittest discover -s tests` to verify behavior, and
follow `AGENTS.md` for the table check.
