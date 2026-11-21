# Signature at the Crime Scene

[![Competition](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![Rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Kiowayyy2109/makefun-joke-reviewer/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![Reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/Kiowayyy2109/makefun-joke-reviewer/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for the make.fun competition **"The joke the reviewer laughs at"**.

A one-line joke about working alongside an AI coding agent, written for
the reviewer of a change: the agent wrote the code, wrote the tests, and
even wrote "all tests pass" — the human reviewer's only remaining job is
providing the signature at the crime scene. It lands because every
developer who has reviewed an agent-authored diff recognises the truth
in it: approval has quietly become attestation.

The program writes exactly one line (120 characters, UTF-8, no trailing
newline) to `/output/entry.txt`:

```
The agent wrote the code, wrote the tests, and wrote 'all tests pass' — I just provide the signature at the crime scene.
```

## Run it

Requires Python 3.13, standard library only, no network access.

```bash
python3 main.py
cat /output/entry.txt
```

Running it twice produces byte-identical output.
