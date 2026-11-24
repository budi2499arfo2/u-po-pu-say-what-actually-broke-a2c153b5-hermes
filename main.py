"""Say What Actually Broke — Hermes entry.

One line of software error copy (1-200 characters) that tells the user the
brutal truth about what went wrong and makes them laugh on the way.

The failure: the password reset email went to the wrong inbox because the
user typed their own email wrong. The dialog admits the reset link is
sitting unread in a stranger's inbox — three of them by now — and that
the fix is spelling, not the spam folder. The joke lands because the
app knows exactly whose inbox it is not.
"""

import os
import sys

TEXT = (
    "Reset link sent to 'hammond@gmal.com'. That's not your inbox — "
    "it's a stranger's, where 3 of your resets now sit unread. "
    "Check your spelling, not your spam folder."
)


def main() -> int:
    # Gate: exactly one line, 1-200 characters, not whitespace-only.
    if not TEXT.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in TEXT.strip():
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"error: entry is {len(TEXT)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(path, "r", encoding="utf-8") as f:
        got = f.read()
    if got != TEXT:
        print("error: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(TEXT)} chars, 1 line)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
