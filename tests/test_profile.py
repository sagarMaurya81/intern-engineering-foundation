from src.profile import get_profile


def test_profile_name():
    profile = get_profile()
    assert profile["name"] == "Sagar Maurya"


def test_profile_department():
    profile = get_profile()
    assert profile["department"] == "Engineering"


def test_profile_skills():
    profile = get_profile()
    assert len(profile["skills"]) > 0