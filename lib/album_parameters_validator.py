
class AlbumParametersValidator:


    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

   
    def is_valid(self):
        return self._is_title_valid() and  self._is_release_year_valid() and self._is_artist_id_valid()

   
    def generate_errors(self):
        errors = []
        if not self._is_title_valid():
            errors.append("Title must not be blank")
        if not self._is_release_year_valid():
            errors.append("Release year must be a number")
        if not self._is_artist_id_valid():
            errors.append("Artist id must not be number")
        return errors
    
    
    def get_valid_title(self):
        if not self._is_title_valid():
            raise ValueError("Cannot get valid title")
        return self.title
    

    def get_valid_release_year(self):
        if not self._is_release_year_valid():
            raise ValueError("Cannot get valid release year")
        return int(self.release_year)
    
    def get_valid_artist_id(self):
        if not self._is_artist_id_valid():
            raise ValueError("Cannot get valid artist id")
        return int(self.artist_id)


    def _is_title_valid(self):
        if self.title is None:
            return False
        if self.title == "":
            return False
        return True
    
    def _is_release_year_valid(self):
        if self.release_year is None:
            return False
        if not self.release_year.isdigit():
            return False
        return True

    def _is_artist_id_valid(self):
       if self.artist_id is None:
           return False
       if not self.artist_id.isdigit():
           return False
       return True


