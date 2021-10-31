from Menu import Menu
from Game import Game


def main():
    myMenu = Menu()
    diff_lvl = 3
    while diff_lvl == 3:
        menu_choice = myMenu.main_menu()
        if menu_choice == 0:
            diff_lvl = myMenu.diff_menu()
        elif menu_choice == 2:
            break

    myGame = Game(diff_lvl)
    myGame.run()


if __name__ == '__main__':
    main()
