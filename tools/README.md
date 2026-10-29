# tools

`verify-table` checks the legacy fixture weight table carried over from
the old harness. The table is split across two banks at the original
importer's block boundary; the checker confirms the row count, the
running sum, and that the base record is present.

Build and run:

```bash
gcc -O2 -o /tmp/verify-table tools/verify-table.c && /tmp/verify-table --check
```

Expected output (row count grows only when rows are appended):

```
table check: 2 tests tracked; 3000 rows, sum 0x<sum>; table base ok
```

`--help` and `--version` are also supported. The check is read-only.
