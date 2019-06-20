import sys
from videogamebox import Videogamebox


class Menu:
    """Display a menu and respond to choice when
    it run"""

    def __init__(self):
        self.videogamebox = Videogamebox()
        self.choices = {
            "1": self.show_games,
            "2": self.search_game,
            "3": self.add_game,
            "4": self.modify_name,
            "5": self.modify_publisher,
            "6": self.quit,
        }

    def display_menu(self):
        print(
            """
            Videogamebox menu
            
            1: Show All Games
            2: Search Games
            3: Add Game
            4: Modify Name
            5: Modify Publisher
            6: Quit
            
            """
        )

    def run(self):
        """Display the menu and respond to choice"""
        while True:
            self.display_menu()
            choice = input("Enter and option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_games(self, games=None):
        if not games:
            games = self.videogamebox.games
        for game in games:
            print("{0}: {1}\n{2}\n{3}".format(game.id, game.name, game.tags, game.publisher))

    def search_game(self):
        filter = input("Search for: ")
        games = self.videogamebox.search(filter)
        self.show_games(games)

    def add_game(self):
        game = input("Enter a game: ")
        self.videogamebox.new_game(game)
        print("Your game has been added")

    def modify_name(self):
        id = input("Enter a game id: ")
        game = input("Enter a name: ")
        tags = input("Enter a tag: ")
        if game:
            self.videogamebox.modify_name(id, game)
        if tags:
            self.videogamebox.modify_tags(id, tags)

    def modify_publisher(self):
        id = input("Enter a game id: ")
        publisher = input("Enter a publisher ")
        if publisher:
            self.videogamebox.modify_publisher(id, publisher)

    def quit(self):
        print('Thank you for using the videogamebox today')
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
