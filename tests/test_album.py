from lib.album import Album

"""
Constructs with an id, title,release date, and artist id 
"""
def test_constructs():
    album = Album(1, "Test Title", 1000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 2


"""
Albums with equal contents are equal 
"""
def test_compares():
    album_1 = Album(1, "Test Title", 1000, 2)
    album_2 = Album(1, "Test Title", 1000, 2)
    assert album_1 == album_2

"""
Albums can be represented as strings
"""
def test_stringifying():
    album = Album(1, "Test Title", 1000, 2)
    assert str(album) == "Album(1, Test Title, 1000, 2)"