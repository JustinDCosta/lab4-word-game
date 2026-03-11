# Guess The Word - Project Report (Lab 4)

## First Impressions
My initial understanding of the project was that it would be a straightforward console game. However, the strict constraints—specifically avoiding `while True` loops and fully separating the logic and UI layers—added an unexpected level of complexity. My approach was to build the pure game state update function first, mathematically verify it with tests, and then wrap the UI and game loops around it.

## Key Learnings
A major takeaway was learning how to design "pure" functions that do not mutate global state, which makes testing incredibly straightforward. Technically, I learned to rely on boolean flags instead of infinite loops to control application state, and how to use list comprehensions to dynamically build strings without relying on banned methods like `.replace()`. Using Copilot effectively required me to firmly dictate my architectural choices rather than letting it drag me into endless Socratic questioning loops.

## CoPilot Prompting Experience
Interacting with Copilot was a mixed bag. It was highly effective when asked to review specific, isolated pieces of code or when acting as an adversary to generate edge-case test ideas. However, open-ended prompts often resulted in overly complex or verbose responses, or trapped me in an annoying "teacher" mode where it just asked me questions instead of giving me code. I found that strictly formatting my prompts with explicit boundaries (e.g., "Review this function, but do not suggest full rewrites") yielded the best results.

## Limitations and Reliability
A major limitation I encountered with Copilot was its tendency to trap the user in pedagogical loops, constantly asking follow-up questions instead of providing direct solutions. I stopped trusting it to drive the architecture because it wanted to overcomplicate the flow. However, I did trust it for finding bugs; it successfully pointed out that `time.time()` is vulnerable to system clock jumps and suggested `time.monotonic()` instead, which was a great catch. 

## Overall Reflection
This project reinforced that AI is an incredible tool for spotting edge cases and generating test coverage, but it cannot replace fundamental software design. I felt I had to actively maintain control over the codebase to ensure the logic remained pure and the constraints were respected. In future projects, I will use AI more for code review and less for open-ended brainstorming to keep the development process efficient.

## Testing Experience
For testing the `update_game_state` function, I used Copilot as an adversary to help generate test cases. Copilot suggested a Socratic approach, guiding me to write Given/When/Then style tests. I opted to use standard Python `assert` statements rather than setting up a full `pytest` virtual environment to keep the project lightweight. We successfully tested edge cases like duplicate guesses, case normalization, preventing negative lives, and ensuring the function remained pure (no mutation of the original input lists).