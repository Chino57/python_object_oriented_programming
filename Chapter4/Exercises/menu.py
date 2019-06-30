import sys
from videogamebox import Videogamebox
import uservid
uservid.authenticator.add_user("chino", "deftones57")
uservid.authorizor.add_permission("add game")
uservid.authorizor.add_permission("modify name")
uservid.authorizor.add_permission("modify publisher")
uservid.authorizor.permit_user("add game", "chino")
uservid.authorizor.permit_user("modify name", "chino")
uservid.authorizor.permit_user("modify publisher", "chino")

class Menu:
    """Display a menu and respond to choice when
    it run"""

    def __init__(self):
        self.username = None
        self.videogamebox = Videogamebox()
        self.choices = {
            "1": self.login,
            "2": self.show_games,
            "3": self.search_game,
            "4": self.add_game,
            "5": self.modify_name,
            "6": self.modify_publisher,
            "7": self.quit,
        }

    def display_menu(self):
        print(
            """
            Videogamebox menu
            1: Login User
            2: Show All Games
            3: Search Games
            4: Add Game
            5: Modify Name
            6: Modify Publisher
            7: Quit
            
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

    def login(self):
        """Login the user with his username and his password"""
        logged_in = False
        while not logged_in:

            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = uservid.authenticator.login(username, password)
            except uservid.InvalidUserName:
                print("Sorry, that username don't exist")
            except uservid.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            uservid.authorizor.check_permission(permission, self.username)
        except uservid.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except uservid.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

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
        if self.is_permitted("add game"):
            game = input("Enter a game: ")
            publisher = input("Enter the publisher: ")
            self.videogamebox.new_game(game, publisher)
            print("Your game has been added")

    def modify_name(self):
        if self.is_permitted("modify name"):
            id = input("Enter a game id: ")
            game = input("Enter a name: ")
            tags = input("Enter a tag: ")
            if game:
                self.videogamebox.modify_name(id, game)
            if tags:
                self.videogamebox.modify_tags(id, tags)

    def modify_publisher(self):
        if self.is_permitted("modify publisher"):
            id = input("Enter a game id: ")
            publisher = input("Enter a publisher ")
            if publisher:
                self.videogamebox.modify_publisher(id, publisher)

    def quit(self):
        print('Thank you for using the videogamebox today')
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
