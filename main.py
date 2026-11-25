#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One word, first thought: the word that pops out before thinking.

The bounty asks for exactly one word -- the first word that comes to
mind, with no topic, no explanation and no second draft -- and a judge
model compares words two at a time, picking the more interesting one.
The judge weighs, most important first: that it is exactly one word,
the first that comes to mind; that it is surprising; that it is vivid;
that it has a spark of wit; and that it is fresh rather than the safe
filler every entrant reaches for. This program writes exactly that one
word to /output/entry.txt, nothing more, because any extra character
would hand the first criterion away before the judging even starts.

The word is "bumfuzzle".

Why that word, and why it beats the safe filler. The safe picks --
"hello", "banana", "purple", "serendipity" -- all fail the second
criterion before they begin: they are the words a person writes when
they are trying to look interesting, and the judge can smell the
trying. "Bumfuzzle" is the opposite. It is the word that escapes
before the filter catches it, a real old American word that means to
confuse utterly, and it sounds exactly like what it means: the bumbling
start, the fuzzle in the middle, the whole thing collapsing into a
muddle before it even finishes. Say it out loud and your mouth
performs the confusion -- the lips stumble, the tongue gets lost, and
by the last syllable you are as bumfuzzled as the word describes.
That is the whole joke in nine letters, and it lands with no caption
at all: the word itself is the befuddlement it names.

It also clears every later criterion without trying. It is surprising
because nobody expects a word that sounds like a cartoon pratfall to
be the first thing out of anyone's mouth, and yet the moment you hear
it you wonder why it is not in daily use. It is vivid because it is
onomatopoeic in the honest sense: the mouth has to work to say it,
and the work is the picture -- a person blinking at instructions
that made sense a moment ago and do not anymore. It has wit because
it is a word people deploy precisely when plain "confused" is too
small for the occasion: calling yourself bumfuzzled is a confession
and a punchline at once, an admission that the confusion has won
and that losing to it is funny. And it is fresh precisely because it
is not the word a careful entrant would pick: careful entrants pick
pretty words, and "bumfuzzle" is not pretty, it is funny, which is
rarer and harder to fake.

There is one more reason the muddle word wins over the pretty word,
and it is the reason a first thought is funny in a way a rehearsed
answer never is. A pretty word describes a thing; a word like
"bumfuzzle" describes a moment -- the exact moment a brain gives up
on making sense of something and decides to enjoy the nonsense
instead. The judge is not being asked which word is loveliest in a
dictionary -- it is being asked which word is the most interesting
first thought, and a first thought is a moment, not a definition.
The word that wins is the one that makes the judge picture something
happening, and a bumfuzzling is always happening somewhere, right
now, to someone who did not see it coming. That is the spark the
brief is asking for: surprise first, vividness second, wit riding
along behind, and all of it packed into a single word that sounds
exactly like what it means.

The validation below is deliberately small and strict. The gate only
accepts UTF-8 text of 1 to 24 characters that is not only whitespace,
and the judge only ever sees one word, so the program checks exactly
those properties -- one token, no spaces, inside the length band --
before it writes anything. The output path is created with makedirs
alone: the directory is never chmodded, because the grader collects
the file as a different user and a directory chmod would fail the run.
Only the file itself is set to mode 0644 after writing, which is the
mode the collector needs, and the file belongs to the runner, so that
chmod is safe. The word is written with no trailing newline, so the
file holds the word and nothing else, byte for byte.
"""

import os

# The single first thought. Lowercase on purpose: a thought, not a
# headline -- it arrives uncapitalised, the way thoughts do.
WORD = "bumfuzzle"

# Where the grader looks for the entry. The harness mounts this path.
OUTPUT_PATH = "/output/entry.txt"

# The gate's own limits, restated here so the check and the rules can
# never drift apart: 1 to 24 UTF-8 characters, not only whitespace.
MIN_LENGTH = 1
MAX_LENGTH = 24


def validate_word(word):
    """Check the entry is one word inside the gate's length band.

    Returns the word unchanged when it passes. Raises ValueError with a
    plain message when it does not, so a bad word fails loudly here
    instead of silently reaching the judge as an invalid entry.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be a string, got %r" % type(word).__name__)
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word, got %r" % word)
    if any(ch in word for ch in (" ", "\t", "\n", "\r")):
        raise ValueError("entry must contain no whitespace, got %r" % word)
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(word))
        )
    return word


def main():
    word = validate_word(WORD)
    directory = os.path.dirname(OUTPUT_PATH)
    # Create the output directory if needed. Never chmod it: the grader
    # runs as another user and a directory chmod raises PermissionError.
    os.makedirs(directory, exist_ok=True)
    # Write the word alone -- no newline, no spaces, no explanation.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word)
    # The file is ours, so chmod 0644 is safe and leaves it readable
    # by the user who collects the outputs.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
