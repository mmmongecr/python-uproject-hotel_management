import numpy

from modules import Mod_FancyThings, Mod_Cipher_Reservations


def people_per_day():
    ch_line = "\n"
    ch_tab = "     "

    reservations = Mod_Cipher_Reservations.getReservations()
    # Variable de matriz que contiene el conteo de los 4 tipos de huésped durante los días de la semana
    ppd_count = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    most_crowded_day = 0
    for counter in range(len(reservations)):
        # Recorre la matriz de las reservaciones y en la segunda dimension verifica el día y la cantidad de personas para hacer el respectivo conteo
        for resident in range(6, 7):
            if reservations[int(reservations[counter][1])][resident] != 0:
                # Se posiciona el ppd_count en el día de la reservación y el tipo de huésped para hacer su conteo
                ppd_count[int(reservations[counter][1]) - 1][int(reservations[counter][resident])-1] += 1


    # for x in range(len(ppd_count)):
    #     # Se define el día más concurrido
    #     if most_crowded_day < ppd_count[x]:
    #         most_crowded_day = ppd_count[x]

    days_of_week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    printable = f"{ch_line}Cantidad de personas atentendidas por día según tipo de huésped:      {ch_line}"
    for filler in range(len(ppd_count)):
        printable += (f"{days_of_week[filler]}: {ch_line}"
                   f"{ch_tab}Hombres: {ppd_count[filler][0]}{ch_line}"
                   f"{ch_tab}Mujeres: {ppd_count[filler][1]}{ch_line}"
                   f"{ch_tab}Hombre Adulto Mayor: {ppd_count[filler][2]}{ch_line}"
                   f"{ch_tab}Mujer Adulta Mayor: {ppd_count[filler][3]}{ch_line}"
                   f"{ch_line}"
                   )

    Mod_FancyThings.fancyTitle(printable, "≈")


def money_per_day():
    ch_line = "\n"
    ch_tab = "     "

    # Variables que definen el porcentaje del precio que tendrá cada servicio
    # Basado en el tipo de reserva (día completo, noche, horas)
    res_ratio_allDay = 1
    res_ratio_night = 0.61
    res_ratio_hours = 0.12

    # Precios standar de servicios para un día completo
    serv_motel = 60
    serv_food = 60
    serv_facilities = 40
    serv_allInclusive = 80


    reservations = Mod_Cipher_Reservations.getReservations()
    # Variable de matriz que contiene la suma de los 4 tipos de servicio que ofrece el motel y su tipo de huésped: estadía, comida, instalaciones, todo incluido
    mpd_count = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for counter in range(len(reservations)):
        # Recorre la matriz de las reservaciones y en la segunda dimension verifica el tipo de servicio contratado

        # Verifica el tipo de huesped
        for resident in range(6, 7):
            # Se define si el huésped tenía descuento
            discount = 0 if int(reservations[counter][resident]) > 3 else 0.15
            if int(reservations[counter][resident]) != 0:
                res_ratio_chosen = 0  # Variable que define el % para calcular el precio de los servicios según el tipo de reserva (D,N,H)
                match int(reservations[counter][0]):
                    case 1:  # Reserva todo el día
                        res_ratio_chosen = res_ratio_allDay
                        # Monto de estadía
                        mpd_count[0][int(reservations[counter][resident])-1] += (serv_motel * res_ratio_chosen) - (serv_motel * res_ratio_chosen)*discount
                        if int(reservations[counter][8]) != 0:  # Si el valor de comida no es cero hace el cálculo y lo suma al total
                            mpd_count[1][int(reservations[counter][resident]) - 1] += (serv_food * res_ratio_chosen) - (serv_food * res_ratio_chosen) * discount
                        elif int(reservations[counter][9]) != 0:  # Si el valor de instalaciones no es cero hace el cálculo y lo suma al total
                            mpd_count[2][int(reservations[resident]) - 1] += (serv_facilities * res_ratio_chosen) - (serv_facilities * res_ratio_chosen) * discount
                        elif int(reservations[counter][10]) != 0:  # Si el valor de todo incluido no es cero hace el cálculo y lo suma al total
                            mpd_count[3][int(reservations[counter][resident]) - 1] += (serv_allInclusive * res_ratio_chosen) - (serv_allInclusive * res_ratio_chosen) * discount
                    case 2:  # Reserva toda la noche
                        res_ratio_chosen = res_ratio_night
                        # Monto de estadía
                        mpd_count[0][int(reservations[counter][resident]) - 1] += (serv_motel * res_ratio_chosen) - (serv_motel * res_ratio_chosen) * discount
                        if int(reservations[counter][8]) != 0:  # Si el valor de comida no es cero hace el cálculo y lo suma al total
                            mpd_count[1][int(reservations[counter][resident]) - 1] += (serv_food * res_ratio_chosen) - (serv_food * res_ratio_chosen) * discount
                        elif int(reservations[counter][9]) != 0:  # Si el valor de instalaciones no es cero hace el cálculo y lo suma al total
                            mpd_count[2][int(reservations[counter][resident]) - 1] += (serv_facilities * res_ratio_chosen) - (serv_facilities * res_ratio_chosen) * discount
                        elif int(reservations[counter][10]) != 0:  # Si el valor de todo incluido no es cero hace el cálculo y lo suma al total
                            mpd_count[3][int(reservations[counter][resident]) - 1] += (serv_allInclusive * res_ratio_chosen) - (serv_allInclusive * res_ratio_chosen) * discount
                    case 3:  # Reserva por horas
                        res_ratio_chosen = res_ratio_hours
                        # Monto de estadía
                        mpd_count[0][int(reservations[counter][resident]) - 1] += (serv_motel * res_ratio_chosen * int(reservations[counter][2])) - (serv_motel * res_ratio_chosen * int(reservations[counter][2])) * discount
                        if int(reservations[counter][8]) != 0:  # Si el valor de comida no es cero hace el cálculo y lo suma al total
                            mpd_count[1][int(reservations[counter][resident]) - 1] += (serv_food * res_ratio_chosen * int(reservations[counter][11])) - (serv_food * res_ratio_chosen * int(reservations[counter][11])) * discount
                        elif int(reservations[counter][9]) != 0:  # Si el valor de instalaciones no es cero hace el cálculo y lo suma al total
                            mpd_count[2][int(reservations[counter][resident]) - 1] += (serv_facilities * res_ratio_chosen * int(reservations[counter][11])) - (serv_facilities * res_ratio_chosen * int(reservations[counter][11])) * discount
                        elif int(reservations[counter][10]) != 0:  # Si el valor de todo incluido no es cero hace el cálculo y lo suma al total
                            mpd_count[3][int(reservations[counter][resident]) - 1] += (serv_allInclusive * res_ratio_chosen * int(reservations[counter][11])) - (serv_allInclusive * res_ratio_chosen * int(reservations[counter][11])) * discount

    services = ["Estadía", "Comida", "Uso de instalaciones", "Todo Incluído"]

    printable = f"{ch_line}Cantidad de dinero generado por servicio:      {ch_line}"
    for filler in range(len(mpd_count)):
        printable += (f"{services[filler]}: {ch_line}"
                      f"{ch_tab}Hombres: {round(mpd_count[filler][0],2)}{ch_line}"
                      f"{ch_tab}Mujeres: {round(mpd_count[filler][1],2)}{ch_line}"
                      f"{ch_tab}Hombre Adulto Mayor: {round(mpd_count[filler][2],2)}{ch_line}"
                      f"{ch_tab}Mujer Adulta Mayor: {round(mpd_count[filler][3],2)}{ch_line}"
                      f"{ch_line}"
                      )

    Mod_FancyThings.fancyTitle(printable, "≈")

def highflow_hours():
    printable = ""
    for underConstruction in range(20):
        printable += ""
    printable += ("Lo sentimos esta opción se encuentra "
                  "deshabilitada de forma temporal\n"
                  "Por favor intente luego")
    Mod_FancyThings.fancyTitle(printable, "≈")

def lowflow_hours():
    highflow_hours()

def report_menu():
    ch_line = "\n"
    # ch_tab = "\t"
    ch_tab = "     "

    Mod_FancyThings.fancyTitle("Módulo de reportes", "+")  # Titulo del módulo

    exitMenu = 1

    while exitMenu == 1:
        print(f"{ch_line}"
              f"* Tipos de reporte :{ch_line}"
              f"{ch_tab}1 - Cantidad de personas atendidas por día{ch_line}"
              f"{ch_tab}2 - Cantidad de dinero generado por día{ch_line}"
              f"{ch_tab}3 - Horario con mayor con menor cantidad de personas{ch_line}"
              f"{ch_tab}4 - Horario con menor cantidad de personas{ch_line}"
              )
        menuop = int(input(f"{ch_tab}Ingrese el tipo de reporte que desea generar: "))

        print()
        Mod_FancyThings.loadingMessage(f"{ch_tab}Generando reporte.", 3)
        print()
        match menuop:
            case 1:
                people_per_day()
            case 2:
                money_per_day()
            case 3:
                highflow_hours()
            case 4:
                lowflow_hours()
            case _:
                Mod_FancyThings.separator_thin(1,48)
                exitMenu = int(input(f"{ch_tab}La opción elegida no es válida. Desea intentar de nuevo? (1 - Si  ó  2 - No): "))

        exitMenu = int(input("Desea generar otro reporte(1 - Si  ó  2 - No): "))

