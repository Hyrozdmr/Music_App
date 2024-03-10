import pytest
from lib.album_parameters_validator import AlbumParametersValidator


"""
With A valid title and year
It is valid
"""
def test_is_valid():
    validator = AlbumParametersValidator("My Title", "1990", "1")
    assert validator.is_valid() == True


"""
With A blank or None title
It is not valid
"""
def test_is_not_valid_with_bad_title():
    validator_1 = AlbumParametersValidator("", "1990", "1")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator(None, "1990", "1")
    assert validator_2.is_valid() == False

"""
With non-integer-convertible-string release year
It is not valid
"""
def test_is_not_valid_with_bad_release_year():
    validator_1 = AlbumParametersValidator("My Title", "", "1")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("My Title", None, "1")
    assert validator_2.is_valid() == False
    validator_3 = AlbumParametersValidator("My Title", "fred", "1")
    assert validator_3.is_valid() == False


"""
With non-integer-convertible-string artist id
It is not valid
"""
def test_is_not_valid_with_bad_artist_id():
    validator_1 = AlbumParametersValidator("My Title", "1990", "")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("My Title", "1990", None)
    assert validator_2.is_valid() == False
    validator_3 = AlbumParametersValidator("My Title", "1990", "fred")
    assert validator_3.is_valid() == False

"""
With invalid parameters
Produces errors
"""
def test_generate_errors():
    validator_1 = AlbumParametersValidator("", "", "")
    assert validator_1.generate_errors() == [
        "Title must not be blank",
        "Release year must be a number",
        "Artist id must not be number",
    ]

    validator_2 = AlbumParametersValidator("Title", "", "1")
    assert validator_2.generate_errors() == [
        "Release year must be a number"
    ]
    
    validator_3 = AlbumParametersValidator("", "1990", "1")
    assert validator_3.generate_errors() == [
        "Title must not be blank"
    ]

    validator_4 = AlbumParametersValidator("Title", "1990", "")
    assert validator_4.generate_errors() ==[
        "Artist id must not be number"
    ]


def test_get_valid_title_if_title_valid():
    validator_1 = AlbumParametersValidator("Title", "1990", "1")
    assert validator_1.get_valid_title() == "Title"

def test_get_valid_title_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("", "1990", "1")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_title()
    assert str(err.value) == "Cannot get valid title"


def test_get_valid_release_year_if_release_year_valid():
    validator_1 = AlbumParametersValidator("Title", "1990", "1")
    assert validator_1.get_valid_release_year() == 1990

def test_get_valid_release_year_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("Title", "", "1")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_release_year()
    assert str(err.value) == "Cannot get valid release year"


def test_get_valid_artist_id_if_artist_id_valid():
    validator_1 = AlbumParametersValidator("Title", "1990", "1")
    assert validator_1.get_valid_artist_id() == 1

def test_get_valid_artist_id_refuses_if_invalid():
    validator_1 = AlbumParametersValidator("Title", "1990", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_artist_id()
    assert str(err.value) == "Cannot get valid artist id"