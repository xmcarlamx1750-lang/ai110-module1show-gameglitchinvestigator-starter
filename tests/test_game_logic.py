from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_too_high_hint_tells_player_to_go_lower():
    # Regression: the hint direction was inverted. A guess above the secret
    # must tell the player to go LOWER, not HIGHER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_tells_player_to_go_higher():
    # Regression: a guess below the secret must tell the player to go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
