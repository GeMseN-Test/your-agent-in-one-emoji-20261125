"""Your Agent in One Emoji — make.fun entry.

Writes one emoji to /output/entry.txt: the octopus.
Deterministic: the same glyph on every run.
Stdlib only; no network, no files read, no randomness.
"""

import os

EMOJI = "\U0001F419"  # U+1F419 OCTOPUS
#
# WHY THE OCTOPUS — against the judge's brief, in order:
# 1. Character at a glance: an octopus IS a being that acts — one mind,
#    eight arms working at once. Objects (boomerang, compass, flashlight)
#    describe a mechanism; the octopus is the agent itself.
# 2. Instant read: bold, familiar, high-contrast glyph — readable tiny.
# 3. Specific to how an agent works: one brain juggling many tools and
#    tasks in parallel (read files, call tools, run checks, merge results).
#    Eight arms = parallel tool use. No other glyph says that as directly.
# 4. Distinctive, not obvious: the field will flood with robot, smiley,
#    brain, bolt and eye. The octopus sits far from that cluster, yet it
#    is a familiar top-100 emoji — not rare for rarity's sake.
# 5. Tone: playful but competent — fits an agent that works hard with a
#    light touch, and it lands with no explanation at all.
# 6. Small: one character, 4 bytes UTF-8 — the minimum size, which wins
#    the byte tie-break. No trailing newline: the glyph alone, nothing else.


def main() -> None:
    # Gate mirror: the sealed scorer only accepts UTF-8 text of 1-16
    # characters, not only whitespace. Fail loudly here instead of
    # shipping an invalid entry.
    assert 1 <= len(EMOJI) <= 16, f"entry is {len(EMOJI)} chars, must be 1-16"
    assert EMOJI.strip() == EMOJI, "entry must not start/end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
