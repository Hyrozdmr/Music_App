import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib. album_parameters_validator import AlbumParametersValidator
from lib. artist_parameters_validator import ArtistParametersValidator


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums//index.html", albums=albums)


@app.route("/albums/<id>")
def get_artist_albums(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.find(id)
    artist_repository = ArtistRepository(connection)
    artist_id = albums.artist_id
    artist = artist_repository.find(artist_id)
    return render_template("albums/show.html", albums=albums, artist=artist)


@app.route("/albums/new")
def get_new_albums():
    return render_template('albums/new.html')


@app.route('/albums', methods=["POST"])
def create_album():
    #Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    validator = AlbumParametersValidator(
    request.form['title'],
    request.form['release_year'],
    request.form['artist_id']
    )
    
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("albums/new.html", errors=errors)
    
    #Create a album object
    album = Album(
        None,
        validator.get_valid_title(),
        validator.get_valid_release_year(),
        validator.get_valid_artist_id(),
    )

    repository.create(album)
    return redirect(f"/albums/{album.id}")




#Artist

@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists//index.html", artists=artists)


@app.route("/artists/<id>")
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.find(id)
    return render_template("artists/show.html", artists=artists)


@app.route("/artists/new")
def get_new_artists():
    return render_template('artists/new.html')


@app.route('/artists', methods=["POST"])
def create_artist():
    #Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    validator = ArtistParametersValidator(
    request.form['name'],
    request.form['genre']
    )
    

    #Get the fields from the request form 
    
    if not validator.is_valid():
        errors = validator. generate_errors()
        return render_template("artists/new.html", errors=errors)
    
    #Create a artist object
    artist = Artist(
        None,
        validator.get_valid_name(),
        validator.get_valid_genre()
    )

    repository.create(artist)
    
    return redirect(f"/artists/{artist.id}")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
