# My Original Thinking

**What are the states of a game like Hangman?**
- initial setup (picking the word)
- waiting for user input
- game over (win)
- game over (loss)

**What variables are required?**
- the target word
- a list of letters the user has guessed so far
- an integer tracking remaining lives

**What are the rules and invariants?**
- Rules: User inputs one letter. If it's correct, reveal it. If wrong, subtract a life. Win by revealing all letters; lose if lives hit zero.
- Invariants: The target word never changes. Lives can't be negative.

**What kind of bugs and edge cases should we be careful about?**
- User types a number or special character instead of a letter.
- User guesses a letter they already tried (shouldn't penalize them again).
- Uppercase vs lowercase (we need to treat 'A' and 'a' as the same).
- User just hits Enter without typing anything.

# CoPilot Suggestions
**App States**
1. Setup: Has the secret word and starting lives been initialized?
2. Awaiting Guess: Is the game paused for player input?
3. Validate Guess: Is the input a single new letter (not empty, not duplicate)?
4. Apply Guess: Should we reveal letters or decrement lives?
5. Check End Condition: Did the player win, lose, or continue?
6. Terminal State: Won or Lost.
7. Replay Decision (optional): Play again or exit?

**App Variables**
1. What is the one value that never changes after setup?
2. Which value decreases only on wrong guesses?
3. Which collection must grow over time so you can detect duplicate guesses?
4. How will you represent the current revealed pattern (for example, `_ a _ _ m a n`)?
5. What variable tells you whether the game is still running, won, or lost?
6. Do you need a variable for the last input, so you can validate and message the player clearly?

**App Rules and Invariants**
1. Rules (behavior)
- If input is invalid, what is the system response?
- If guess is correct, what changes?
- If guess is wrong, what changes?
- If all letters are revealed, what transition happens?
- If lives reach zero, what transition happens?

2. Invariants (always true)
- Which variables should never mutate unexpectedly?
- What numeric bounds must always hold (for lives)?
- What relationship must always hold between guessed letters and displayed word?
- What consistency should always hold for letter case (uppercase/lowercase handling)?

**App Bugs**
1. Input validity: What happens if the player enters empty input, multiple characters, a number, punctuation, or whitespace?
2. Case handling: Are A and a treated as the same guess everywhere?
3. Duplicate guesses: If a letter was already guessed, do you warn only, or also subtract a life?
4. Life counter safety: Can lives ever drop below 0 because of repeated wrong processing?
5. Repeated letters in the word: If the word has two a’s, does one correct guess reveal both?
6. State transition order: Do you check win/loss after every guess update, and only once per turn?
7. Win/loss conflict: If the final guess reveals the last letter, could the code also incorrectly trigger loss in the same turn?
8. Hidden-word display sync: Is the displayed pattern always consistent with guessed letters?
9. Word quality: Could the chosen word include spaces, hyphens, or uppercase letters that break your rules?
10. Replay reset: On a new game, are guessed letters, lives, and display fully reset?
11. Infinite-loop risk: Could invalid input keep the game stuck without clear feedback?
12. Testability: Have you tried tiny words like a, repeated-letter words like letter, and near-loss scenarios with 1 life left?

# Observations
**Did CoPilot overcomplicate or under-specify?**
It overcomplicated things initially. Instead of just giving me a straight list of variables or rules, it gave me a bunch of checklists and questions to answer myself. Later on, it kept trying to trap me in these endless "Socratic method" teacher loops when I just wanted to verify my code and move on.

**Does that help? In what way?**
Yes, the state transition map it provided was actually exactly what I needed to build the main game loop. It was also really good at spotting edge cases I hadn't thought of (like checking `time.monotonic()` instead of `time.time()` for the timer so system clock updates don't break the game, and making sure words with hyphens don't break the win condition).

# Implementation & Architecture Notes
**Dealing with constraints:**
- **No `while True`:** Handled this by using strict boolean flags (`game_active`, `keep_playing`, `valid_response`) to control the loops.
- **No string replacement functions:** Used a Python list comprehension to build the masked word dynamically (`" ".join([char if ... else "_"])`) instead of relying on `.replace()`.
- **Logic vs. UI separation:** Kept the `update_game_state` function completely pure. All `print()` statements and input prompts happen in separate UI functions or the main loop.

**Testing:**
- Decided to skip setting up a full `pytest` virtual environment. Kept it lightweight by just writing a `test_game.py` file with standard Python `assert` functions.
- Wrote tests to verify Given/When/Then scenarios.
- Key tests: checking for list purity (making sure original inputs aren't mutated), handling duplicate guesses properly without losing extra lives, testing the case normalization (A == a), and making sure lives floor at 0.

**Extensions added:**
- Added Word Categories using a dictionary.
- Added Difficulty settings (Easy, Medium, Hard) that scale lives and time limits.
- Added a strict timer that automatically docks a life if the user takes too long to type.
- Built a score system that tracks points across replays based on lives remaining and a speed bonus.

# Auto Play MOde Assignment

**Initial Thoughts:**
- Okay, I need to add a menu right at the start asking if the user wants to play manually or watch the computer play. 
- The computer has to make guesses on its own.
- The one big rule: the computer can neverr guess the same letter twice.

**MY Plan / Design Decisions:**
- **Preventing repeats:** Instead of checking `if guess in guessed_letters` and looping until I find a new one, I'm just going to make a list of the alphabet, shuffle it, and `pop()` a letter off the end each turn. Easy, fast, and guarantees no duplicate guesses.
- **Code structure:** I'm not going to mess with my `play_single_game` function because I don't want to break the timer or scoring stuff. I'll just duplicate it into a new `auto_play_single_game` function and strip out the input prompts.
- **Pacing:** I need to import `time` and add `time.sleep(1)` between the computer's guesses. Otherwise, it will just instantly print the end of the game to the terminal and I won't be able to actually watch it play.