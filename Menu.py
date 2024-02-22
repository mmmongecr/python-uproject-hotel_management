import random

from modules import Mod_Menu_Reservations, Mod_Menu_Invoices, Mod_Menu_Reports
from modules import Mod_FancyThings #


def mainMenu():

    # Variable menuLvl se encarga del ciclo de vida del menu, siempre que el valor sea 1 el menu se repetirá
    menuLvl = 1
    while menuLvl == 1:

        showMenu = random.randrange(1, 3)
        match showMenu:
            case 1:
                Mod_FancyThings.message_welcome("menu_main")
            case 2:
                Mod_FancyThings.message_welcome("menu_alt")

        Mod_FancyThings.mainmenu()

        menuOpcion = int(input ("\nSelecione un opción: "))
        Mod_FancyThings.separator(3)

        match menuOpcion:
            case 1:
                Mod_Menu_Reservations.reservations_menu()
                Mod_FancyThings.loadingMessage("Volviendo a menu principal.", 3)
                Mod_FancyThings.separator(3)
            case 2:
                Mod_Menu_Invoices.invoices_menu()
                Mod_FancyThings.loadingMessage("Volviendo a menu principal.", 3)
                Mod_FancyThings.separator(3)

            case 3:
                Mod_Menu_Reports.report_menu()
                Mod_FancyThings.loadingMessage("Volviendo a menu principal.", 3)
                Mod_FancyThings.separator(3)
            case 4:
                print("Gracias por visitarnos y por su interes")
                menuLvl = 0

#mainMenu()