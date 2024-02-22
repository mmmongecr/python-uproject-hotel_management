import time


def loadingMessage (text,times):
    # Método que muestra un mensaje introducido por el usuario la cantidad de veces que este lo decida
    for x in range(times):
        print(text)
        text += "."
        time.sleep(0.7)

def fancyTitle(title, deco):
    # Función para decorar titulos dentro de un cuadrado
    newtitle = ""
    if len(str.split(title,"\n")) < 2: # Titulos de solo una linea
        title_len = len(title)
        newtitle = (deco*(title_len+8) + "\n" +
                    deco*2 + "  " + title + "  " + deco * 2 + "\n" +
                    deco*(title_len+8) + "\n")
    else: # Titulos  multilinea

        title = str.split(title,"\n")
        title_len = 0

        # Se calcula cual de las lineas es la más largas para tomarla como referencia
        for x in range(len(title)):
            if len(title[x])> title_len:
                title_len = len(title[x])
        # Se empieza a construir el titulo
        newtitle = deco * (title_len + 8) + "\n"
        # Se agregan las lineas que conforman el cuerpo del titulo
        for x in range(len(title)):
            # Variable temporal para calcular la cantidad de espacios extra necesarios en la linea para crear un marco perfecto
            temp_title = deco * 2 + "  " + title[x] + "  " + deco * 2
            if len(temp_title) < title_len + 8:
                extraSpace = (title_len + 8)-len(temp_title)
                newtitle += deco * 2 + " "*2 + title[x] + " " * (extraSpace+2) + deco * 2 + "\n"
            else:
                newtitle += deco * 2 + "  " + title[x] + "  " + deco * 2 + "\n"
        newtitle += deco * (title_len + 8) + "\n"
    print(newtitle)

def separator(pageBreaksNums):
    deco = "="
    pageBreaks = "\n" * (pageBreaksNums-1)
    print(f"{pageBreaks}"
          f"{deco*150}"
          f"{pageBreaks}")
def separator_thin(tabs,long):
    tab = "\t"
    deco = "-"
    print(f"{tab*tabs}{deco*long}")

def message_warning(text):
    print(f"\n¡¡¡¡¡ AVISO: {text} !!!!!\n\n")

def message_welcome(option):
    match option:
        case "welcomeApp":
            print("\n\n"
                  "===========================================================================================================================================================\n"
                  "║   ███╗   ███╗  ██████╗  ████████╗ ███████╗ ██╗         ███████╗ ██╗          ██████╗  █████╗  ███████╗  ██████╗  ██╗   ██╗ ███████╗ ████████╗ ███████╗   ║\n"
                  "║   ████╗ ████║ ██╔═══██╗ ╚══██╔══╝ ██╔════╝ ██║         ██╔════╝ ██║         ██╔════╝ ██╔══██╗ ██╔════╝ ██╔═══██╗ ██║   ██║ ██╔════╝ ╚══██╔══╝ ██╔════╝   ║\n"
                  "║   ██╔████╔██║ ██║   ██║    ██║    █████╗   ██║         █████╗   ██║         ██║      ███████║ ███████╗ ██║   ██║ ██║   ██║ █████╗      ██║    █████╗     ║\n"
                  "║   ██║╚██╔╝██║ ██║   ██║    ██║    ██╔══╝   ██║         ██╔══╝   ██║         ██║      ██╔══██║ ╚════██║ ██║▄▄ ██║ ██║   ██║ ██╔══╝      ██║    ██╔══╝     ║\n"
                  "║   ██║ ╚═╝ ██║ ╚██████╔╝    ██║    ███████╗ ███████╗    ███████╗ ███████╗    ╚██████╗ ██║  ██║ ███████║ ╚██████╔╝ ╚██████╔╝ ███████╗    ██║    ███████╗   ║\n"
                  "║   ╚═╝     ╚═╝  ╚═════╝     ╚═╝    ╚══════╝ ╚══════╝    ╚══════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝ ╚══════╝  ╚══▀▀═╝   ╚═════╝  ╚══════╝    ╚═╝    ╚══════╝   ║\n"
                  "============================================================================================================================================================\n"
                  )
        case "menu_main":
            print("\n",
                  "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n",
                  "░░   ______     __     ______     __   __     __    __   ______     __   __     __     _____     ______     ░░\n",
                  "░░  /\  == \   /\ \   /\  ___\   /\ ^-.\ \   /\ \  / /  /\  ___\   /\ '-.\ \   /\ \   /\  __-.  /\  __ \    ░░\n",
                  "░░  \ \  __<   \ \ \  \ \  __\   \ \ \- . \  \ \ \ '/   \ \  __\   \ \ \-.  \  \ \ \  \ \ \/\ \ \ \ \/\ \   ░░\n",
                  "░░   \ \_____\  \ \_\  \ \_____\  \ \_\\^\_ \  \ \__|     \ \_____\  \ \_\\^\_ \  \ \_\  \ \____-  \ \_____\  ░░\n",
                  "░░    \/_____/   \/_/   \/_____/   \/_/ \/_/   \/_/       \/_____/   \/_/ \/_/   \/_/   \/____/   \/_____/  ░░\n",
                  "░░                                                                                                          ░░\n",
                  "░░    ______     __            ______     __     ______     ______   ______     __    __     ______         ░░\n",
                  "░░   /\  __ \   /\ \          /\  ___\   /\ \   /\  ___\   /\__  _\ /\  ___\   /\ ^-./  \   /\  __ \        ░░\n",
                  "░░   \ \  __ \  \ \ \____     \ \___  \  \ \ \  \ \___  \  \/_/\ \/ \ \  __\   \ \ \-./\ \  \ \  __ \       ░░\n",
                  "░░    \ \_\ \_\  \ \_____\     \/\_____\  \ \_\  \/\_____\    \ \_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\      ░░\n",
                  "░░     \/_/\/_/   \/_____/      \/_____/   \/_/   \/_____/     \/_/   \/_____/   \/_/  \/_/   \/_/\/_/      ░░\n",
                  "░░                                                                                                          ░░\n",
                  "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ \n")
        case "menu_alt":
            print("\n"
                  "▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬▬\n"
                  "▬   ____   __   ____   __ _   _  _   ____   __ _   __   ____    __       __    __       ____   __   ____   ____   ____   _  _    __    ▬\n"
                  "▬  (  _ \ (  ) (  __) (  ( \ / )( \ (  __) (  ( \ (  ) (    \  /  \     / _\  (  )     / ___) (  ) / ___) (_  _) (  __) ( \/ )  / _\   ▬\n"
                  "▬   ) _ (  )(   ) _)  /    / \ \/ /  ) _)  /    /  )(   ) D ( (  O )   /    \ / (_/\   \___ \  )(  \___ \   )(    ) _)  / \/ \ /    \  ▬\n"
                  "▬  (____/ (__) (____) \_)__)  \__/  (____) \_)__) (__) (____/  \__/    \_/\_/ \____/   (____/ (__) (____/  (__)  (____) \_)(_/ \_/\_/  ▬\n"
                  "▬                                                                                                                                      ▬\n"
                  "▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬▬\n"
                  )
def mainmenu():
    print("\n"
          "==========================\n"
          "|     Menú Principal     |\n"
          "==========================\n"
          "|  Opciones              |\n"
          "--------------------------\n"
          "|  1- Reservas           |\n"
          "|  2- Facturas           |\n"
          "|  3- Informes           |\n"
          "|  4- Salir del sistema  |\n"
          "==========================")