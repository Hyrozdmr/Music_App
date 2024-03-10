import pytest
from playwright.sync_api import Page, expect

# Tests for your routes add Albums

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"
    ])


def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Doolittle")
    release_year_tag = page.locator(".t-release_year")
    expect(release_year_tag).to_have_text("Released: 1989")
    artist_tag = page.locator(".t-artist")
    expect(artist_tag).to_have_text("Artist: Pixies")


def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")


def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add album"')

    page.fill("input[name='title']", "Test Album")
    page.fill("input[name='release_year']", "1134")
    page.fill("input[name='Artist']", "1")
    page.click('text="Add album"')

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Test Album")
    release_year_tag = page.locator(".t-release_year")
    expect(release_year_tag).to_have_text("Released: 1134")


def test_validate_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add album"')
    page.click('text="Add album"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: Title must not be blank, Release year must be a number")



#Tests for your routes add Artists

def test_get_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone'
    ])


def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Pixies")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Rock")


def test_visit_artist_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist")


def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Add a new artist"')

    page.fill('input[name=name]', "Test Artist")
    page.fill('input[name=genre]', "Test Genre")
    page.click('text="Add artist"')

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Test Artist")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Test Genre")


def test_validate_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click('text="Add artist"')
    page.click('text="Add artist"')

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title must not be blank, " \
        "Genre must not be blank"
    )
