from services.game_service import compare_secret_code_to_user_guess, create_feedback


def test_all_correct():
    """Test that all digits are correctly guessed both in number and position.
        The user's guess exactly matches the secret code,
        both the number of correct digits and their positions are accurately counted."""

    secret_code = "1234"
    user_guess = "1234"
    assert compare_secret_code_to_user_guess(secret_code, user_guess) == (4, 4)


def test_some_correct_numbers():
    """Test that the function identifies correct numbers even when they are in the wrong position. """
    secret_code = "1234"
    user_guess = "5671"
    assert compare_secret_code_to_user_guess(secret_code, user_guess) == (1, 0)


def test_repeating_numbers_in_guess():
    """Test the function of repeated numbers in the user's guess. """
    secret_code = "1231"
    user_guess = "1111"
    assert compare_secret_code_to_user_guess(secret_code, user_guess) == (2, 2)


def test_create_feedback_won():
    """Test feedback generation when the user wins by correctly guessing the entire secret code."""
    feedback = create_feedback("1234", "1234")
    assert feedback == "You won!"


def test_create_feedback_no_correct():
    """ Test feedback generation for no correct digits or positions. """
    feedback = create_feedback("1234", "5678")
    assert feedback == "No correct number(s), no correct place(s)"


def test_feedback_some_correct_numbers_and_places():
    """ Test feedback when some numbers are correct but not all in the correct places. """
    secret_code = "1234"
    user_guess = "1325"
    feedback = create_feedback(secret_code, user_guess)
    assert feedback == "3 correct number(s), 1 correct place(s)"


def test_feedback_all_correct_numbers_some_incorrect_places():
    """ Test feedback when all numbers are correct but some are in the wrong places. """
    secret_code = "1234"
    user_guess = "1243"
    feedback = create_feedback(secret_code, user_guess)
    assert feedback == "4 correct number(s), 2 correct place(s)"


def test_feedback_no_correct_numbers_some_correct_places():
    """ Test feedback when no numbers are correct but some correct places exist due to similar numbers. """
    secret_code = "1234"
    user_guess = "1893"
    feedback = create_feedback(secret_code, user_guess)
    assert feedback == "2 correct number(s), 1 correct place(s)"
