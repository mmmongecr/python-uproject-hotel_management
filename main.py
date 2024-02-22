'''
      Programación Básica (Introducción a la Programación)
      2023 Segundo Cuatrimestre
      LAB:K (6pm-9pm)
      Grupo No.9

      Proyecto
      Integrantes:      Manuel Mora Monge

      Anotaciones:      Este es nuestro primer entregable, aún falta agregar/implementar muchas funcionalidades que estamos explorando, entre ellas la lectura de archivos y su utilización
                        como una pseudo base de datos para poder almacenar los registros del ejercicio y así poder mantener la información aún al cerrar el programa.
'''

import Login
from modules import Mod_FancyThings

Mod_FancyThings.message_welcome("welcomeApp")

Login.login()