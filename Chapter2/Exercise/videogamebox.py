import datetime

# store the newt available id for all new videogame available
last_id = 0


class VideoGame:
    """Represent a videogame that will be put inside the videogamebox
    Match against a string in searches and store tag for each videogame"""

    def __init__(self, name, publisher, tags=""):
        """Initialize a new videogame with the name and the publisher
        and optional space-separated tags.Automatically set the add box date
        and a unique ID"""
        self.name = name
        self.publisher = publisher
        self.tags = tags
        self.add_box_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this game match the filter
        text. Return True if it matches , False otherwise

        Search is case sensitive and matches both name, publisher
        and tags"""
        return filter in self.name or filter in self.publisher or filter in self.tags

<<<<<<< HEAD

=======
>>>>>>> 8cf8691aaf866a18678905b9ea5f9f0af787aed9
class Videogamebox:
    """Represent a box of videogame that can be tagged,
    modified and searched"""

    def __init__(self):
        """Initialize a videogamebox with an empty list"""
        self.games = []

    def new_game(self, name, publisher, tags=""):
        """Created a game and add in the box"""
        self.games.append(VideoGame(name, publisher, tags))

    def _find_game(self, game_id):
        """Locate the game with the given id"""
        for game in self.games:
            if str(game.id) == str(game_id):
                return game
        return None

    def modify_name(self, game_id, name):
        """Find the game with the given id
        and change the name"""
        game = self._find_game(game_id)
        if game:
            game.name = name
            return True
        return False

    def modify_tags(self, game_id, tags):
        """Find thz game with the good id and
        change the tags"""
        self._find_game(game_id).tags = tags

    def modify_publisher(self, game_id, publisher):
        """Find the game with the good id and
        change the publisher"""
        self._find_game(game_id).publisher = publisher

    def search(self, filter):
        """Find all game that match the given filter
        string"""
        return [game for game in self.games if game.match(filter)]
