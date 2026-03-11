# Guess The Word (Lab 4)

This is my complete implementation of the Word Game assignment. I built the core logic first, verified it with tests, and then integrated all the optional extensions into the final loop.

## Features
* **Strictly follows constraints:** No `while True` loops, no string `.replace()` methods, and total separation of the UI and logic layers.
* **Categories:** Choose between Tech, Animals, or Food.
* **Difficulties:** Easy, Medium, and Hard (scales your starting lives and guess time limits).
* **Speed Timer:** Uses `time.monotonic()` to track how long you take. If you don't guess fast enough, you lose a life.
* **Score Tracking:** Keeps a running score across multiple games based on remaining lives, difficulty multipliers, and speed bonuses.

## How to Play
Open your terminal in the project folder and run:
`python main.py`

Follow the prompts to select your category and difficulty. Type a single letter to guess. You can play as many rounds as you want without restarting the script.

## Testing
To run the test suite for the core game logic, execute:
`python test_game.py`

This runs a series of basic assertion tests (no `pytest` virtual environment needed) that verify the game state updates properly. It tests list purity (ensuring original inputs aren't mutated), duplicate guess handling, case normalization, and ensures lives never drop below zero. If successful, it prints "All tests passed successfully!".