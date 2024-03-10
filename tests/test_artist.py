from lib.artist import Artist

"""
Constructs with an id, title,release date, and artist id 
"""
def test_constructs():
    artist = Artist(1, 'Pixies', 'Rock')
    assert artist.id == 1
    assert artist.name == "Pixies"
    assert artist.genre == "Rock"


"""
artists with equal contents are equal 
"""
def test_compares():
    artist_1 = Artist(1, 'Pixies', 'Rock')
    artist_2 = Artist(1, 'Pixies', 'Rock')
    assert artist_1 == artist_2

"""
artists can be represented as strings
"""
def test_stringifying():
    artist = Artist(1, 'Pixies', 'Rock')
    assert str(artist) == "Artist(1, Pixies, Rock)"