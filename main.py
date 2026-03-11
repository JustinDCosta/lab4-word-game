import random
import time


def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """Return updated guessed letters and lives after one guess.

    Assumptions:
    - Input validation is handled by the caller (single alphabetic character).
    - Guesses are stored in lowercase for consistent duplicate checks.

    Behavior:
    - New wrong guesses decrement lives by 1, clamped at 0.
    - Repeated guesses do not change lives.
    """
    new_guessed_letters = guessed_letters.copy()
    new_lives = lives
    clean_guess = guess.lower()

    if clean_guess not in new_guessed_letters:
        new_guessed_letters.append(clean_guess)
        if clean_guess not in secret_word.lower():
            new_lives = max(0, new_lives - 1)

    return new_guessed_letters, new_lives


def is_game_won(secret_word: str, guessed_letters: list[str]) -> bool:
    return all(char.lower() in guessed_letters for char in secret_word if char.isalpha())


def calculate_round_score(won: bool, lives_remaining: int, difficulty_multiplier: int, elapsed_time: float) -> int:
    if not won:
        return 0
    base_score = lives_remaining * 10 * difficulty_multiplier
    time_bonus = max(0, 50 - int(elapsed_time))
    return base_score + time_bonus


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    masked = [char if (char.lower() in guessed_letters or not char.isalpha()) else "_" for char in secret_word]
    return " ".join(masked)


def display_game_state(secret_word: str, guessed_letters: list[str], lives: int, time_limit: int):
    print(f"\nWord: {get_masked_word(secret_word, guessed_letters)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Lives remaining: {lives} | You have {time_limit} seconds per guess!")


def display_categories(categories: dict) -> str:
    print("\nAvailable Categories:")
    for cat in categories.keys():
        print(f"- {cat}")
    return "Select a category: "


def display_difficulties() -> str:
    print("\nAvailable Difficulties:")
    print("- Easy (8 lives, 15s per guess)")
    print("- Medium (6 lives, 10s per guess)")
    print("- Hard (4 lives, 5s per guess)")
    return "Select a difficulty: "


def play_single_game(category_words: list[str], starting_lives: int, time_limit: int, diff_multiplier: int) -> int:
    secret_word = random.choice(category_words)
    guessed_letters = []
    lives = starting_lives

    game_active = True
    round_start_time = time.monotonic()

    while game_active:
        display_game_state(secret_word, guessed_letters, lives, time_limit)

        guess_start_time = time.monotonic()
        guess = input("Guess a letter: ").strip().lower()
        guess_duration = time.monotonic() - guess_start_time

        if guess_duration > time_limit:
            print(f"Too slow! That took {guess_duration:.1f}s. You lost a life.")
            lives = max(0, lives - 1)
            if lives == 0:
                print(f"\nGame Over! You ran out of lives. The word was: {secret_word}")
                game_active = False
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)

        if is_game_won(secret_word, guessed_letters):
            total_round_time = time.monotonic() - round_start_time
            score = calculate_round_score(True, lives, diff_multiplier, total_round_time)
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            print(f"Round Score: {score} points!")
            return score
        elif lives == 0:
            print(f"\nGame Over! You ran out of lives. The word was: {secret_word}")
            game_active = False

    return 0


def main():
    word_database = {
        "Tech": ["python", "software", "developer", "algorithm"],
        "Animals": ["elephant", "giraffe", "penguin", "kangaroo", "polar bear"],
        "Food": ["pizza", "hamburger", "spaghetti", "ice-cream"]
    }

    difficulty_settings = {
        "easy": {"lives": 8, "time": 15, "multiplier": 1},
        "medium": {"lives": 6, "time": 10, "multiplier": 2},
        "hard": {"lives": 4, "time": 5, "multiplier": 3}
    }

    keep_playing = True
    total_score = 0
    games_played = 0

    print("Welcome to Guess The Word: Ultimate Edition!")

    while keep_playing:
        category_selected = False
        selected_cat = ""
        while not category_selected:
            cat_input = input(display_categories(word_database)).strip().title()
            if cat_input in word_database:
                selected_cat = cat_input
                category_selected = True
            else:
                print("Invalid category. Try again.")

        diff_selected = False
        selected_diff = ""
        while not diff_selected:
            diff_input = input(display_difficulties()).strip().lower()
            if diff_input in difficulty_settings:
                selected_diff = diff_input
                diff_selected = True
            else:
                print("Invalid difficulty. Try again.")

        settings = difficulty_settings[selected_diff]

        print(f"\nStarting game in category '{selected_cat}' on '{selected_diff.title()}' difficulty...")
        round_score = play_single_game(
            word_database[selected_cat],
            settings["lives"],
            settings["time"],
            settings["multiplier"]
        )

        total_score += round_score
        games_played += 1

        print(f"\n--- SESSION STATS ---")
        print(f"Games Played: {games_played} | Total Score: {total_score}")

        valid_response = False
        while not valid_response:
            replay = input("\nDo you want to play again? (y/n): ").strip().lower()
            if replay == 'y':
                valid_response = True
            elif replay == 'n':
                valid_response = True
                keep_playing = False
            else:
                print("Please enter 'y' or 'n'.")

    print(f"\nThanks for playing! Final Score: {total_score} across {games_played} games.")


if __name__ == "__main__":
    main()
