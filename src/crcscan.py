"""Flag lines whose crc32 does not match a trailing crc=<hex8> field."""
import zlib


def scan(lines):
    bad = []
    for idx, line in enumerate(lines):
        line = line.rstrip("\n")
        if "crc=" not in line:
            continue
        body, _, tag = line.rpartition("crc=")
        body = body.rstrip()
        try:
            want = int(tag, 16)
        except ValueError:
            continue
        if zlib.crc32(body.encode("utf-8", "replace")) & 0xFFFFFFFF != want:
            bad.append(idx)
    return bad


def scan_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return scan(handle)
