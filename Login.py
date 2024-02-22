import os
import time

import Menu
from modules import Mod_FancyThings
from modules import Mod_Cipher_Users


def login():

    Mod_FancyThings.fancyTitle("       Inicio de sesión       ","¤")

    # log_status: variable que define el estatus del inicio de sesión,
    # permite identificar si debemos pasar al siguiente paso o si debe volver a intentarlo
    log_status = False

    while log_status == False:

        print("Por favor introduzca sus credenciales: ")
        log_user = input("Usuario: ")
        log_pass = input("Contraseña: ")

        validation = Mod_Cipher_Users.validate_user(log_user, log_pass) # Verifica si el usuario y la contraseña están registrados en la DB
        Mod_FancyThings.separator_thin(0,150)
        Mod_FancyThings.loadingMessage("Validando.", 3)

        match validation:
            case 1:
                # El valor de log status cambia a True para salir del menu
                log_status = True
                print()
                Mod_FancyThings.fancyTitle("Resgistro exitoso!!!", "»")
                Mod_FancyThings.separator(1)
                time.sleep(3)
                Menu.mainMenu()
            case 2:
                print("\nEl usuario ingresado no es correcto, por favor intente de nuevo\n")
                Mod_FancyThings.separator_thin(0, 150)
            case 3:
                print("\nLa contraseña ingresada no es correcta, por favor intente de nuevo\n")
                Mod_FancyThings.separator_thin(0, 150)
            case 4:
                print("\nLos credenciales ingresados no son correctos, por favor intente de nuevo\n")
                Mod_FancyThings.separator_thin(0, 150)