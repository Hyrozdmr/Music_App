from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When I call #all
I get all the artists in the artists table
"""
def test_all(db_connection):
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, "Wild nothing", "Indie")
    ]


"""
When I call #find with an id
I get that artist back
"""
def test_find(db_connection):
    repository = ArtistRepository(db_connection)
    assert repository.find(1) == Artist(1, 'Pixies', 'Rock')



"""
When I call #create
I create an artist in the database
And I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Wild nothing", "Indie")
    repository.create(artist)
    assert repository.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, "Wild nothing", "Indie")
    ]
    