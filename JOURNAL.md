# This JOURNAL.md file gets automatically updated by the journal-logger agent after every interaction with CoPilot. It serves as a comprehensive log of all prompts, responses, changes made, and reflections during the development process. Each entry is formatted consistently for easy reading and is listed in reverse chronological order, with the most recent interactions at the top.

**New Interaction**
**Date**: 03-01-2026 14:36
**User**: justin.d-costa@epita.fr
**Prompt**: Implement a recursive Fibonacci function in main.py
**CoPilot Mode**: Agent
**CoPilot Model**: GPT-5.3-Codex
**Changes Made**: Implemented a recursive `fibonacci(n: int) -> int` function in `main.py` with base cases (`n <= 1`) and recursive relation (`fibonacci(n - 1) + fibonacci(n - 2)`), plus input validation for type and non-negative values.
**Reasons for Changes**: The prompt explicitly requested a recursive Fibonacci implementation in `main.py`; validation was included to make behavior explicit for invalid inputs.
**Context**: `main.py` was empty prior to this change.
**My Observations**: Ran this to verify that the logger triggers automatically after generating code. The AI actually wrote a solid function for fibonacci.

**New Interaction**
**Date**: 03-01-2026 14:34
**User**: justin.d-costa@epita.fr
**Prompt**: Read the ai4se.instructions.md file and follow its directive. Activate the journal agent in journal-logger.agent.md
**CoPilot Mode**: Agent
**CoPilot Model**: GPT-5.3-Codex
**Changes Made**: Read `.github/instructions/ai4se.instructions.md` and `.github/agents/journal-logger.agent.md`; updated `User` in `journal-logger.agent.md` from `default_user` to `justin.d-costa@epita.fr`; prepended this interaction to `JOURNAL.md` in the required format.
**Reasons for Changes**: The repository instruction requires loading and following instruction files, and the journal agent requires persistent user identity plus a reverse-chronological log entry after each prompt.
**Context**: Retrieved user identity from `git config user.email` and timestamp from local system time in `MM-dd-yyyy HH:mm` format.
**My Observations**: Agent setup worked fine. It successfully read the instruction files, grabbed my correct email from git config, and started the journal format perfectly.

