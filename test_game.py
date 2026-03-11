from main import update_game_state


def test_new_wrong_guess_decrements_lives_once():
    guessed_letters = []
    new_letters, new_lives = update_game_state("python", guessed_letters, "z", 6)
    assert new_letters == ["z"] and new_lives == 5
    assert guessed_letters == []  # Purity check


def test_duplicate_wrong_guess_should_not_decrement_lives_again():
    guessed_letters = ["z"]
    new_letters, new_lives = update_game_state("python", guessed_letters, "z", 5)
    assert new_letters == ["z"] and new_lives == 5
    assert guessed_letters == ["z"]  # Purity check


def test_new_correct_guess_keeps_lives_unchanged():
    guessed_letters = []
    new_letters, new_lives = update_game_state("python", guessed_letters, "p", 6)
    assert new_letters == ["p"] and new_lives == 6
    assert guessed_letters == []


def test_uppercase_guess_normalization():
    guessed_letters = []
    new_letters, new_lives = update_game_state("python", guessed_letters, "P", 6)
    assert new_letters == ["p"] and new_lives == 6
    assert guessed_letters == []


def test_lives_floor_at_zero():
    guessed_letters = []
    new_letters, new_lives = update_game_state("python", guessed_letters, "z", 0)
    assert new_letters == ["z"] and new_lives == 0
    assert guessed_letters == []


def test_mixed_case_secret_word_works():
    guessed_letters = []
    new_letters, new_lives = update_game_state("PyThOn", guessed_letters, "p", 6)
    assert new_letters == ["p"] and new_lives == 6
    assert guessed_letters == []


def test_duplicate_correct_guess_keeps_state_unchanged():
    guessed_letters = ["p"]
    new_letters, new_lives = update_game_state("python", guessed_letters, "p", 6)
    assert new_letters == ["p"] and new_lives == 6
    assert guessed_letters == ["p"]


if __name__ == "__main__":
    test_new_wrong_guess_decrements_lives_once()
    test_duplicate_wrong_guess_should_not_decrement_lives_again()
    test_new_correct_guess_keeps_lives_unchanged()
    test_uppercase_guess_normalization()
    test_lives_floor_at_zero()
    test_mixed_case_secret_word_works()
    test_duplicate_correct_guess_keeps_state_unchanged()
    print("All tests passed successfully!")
