from modules import Mod_Cipher_Reservations
from modules import Mod_Cipher_Rooms
from modules import Mod_FancyThings


def menuerror(option):
    match option:
        case 1:
            Mod_FancyThings.separator_thin(1, 44)
            print("\t¡La opción elegida no es válidad!\n"
                  "\t¿Desea intentar de nuevo (1 - Si  ó 2 - No)?")
        case 2:
            Mod_FancyThings.separator_thin(1, 90)
            print("\tLo sentimos pero no contamos con cuartos disponibles para la cantidad de persona indicadas\n"
                  "\t¿Desea intentar de nuevo (1 - Si  ó 2 - No)?")

    return int(input("\tElija una opción: "))


def checkRoom(rooms, chosen_room):
    validation = False
    for x in range(len(rooms)):
        if rooms[x] == int(chosen_room):
            validation = True
    return validation


def listAvailableRooms(rooms):
    available_rooms = ""
    for x in range(len(rooms)):
        available_rooms += f"{rooms[x]}\t"
    return available_rooms


def menu_buyItOrNot(service, ratio, times):
    price = service * ratio * times
    textToPrint = f"\tEl precio del servicio es de ${round(price, 2)} por persona"
    Mod_FancyThings.separator_thin(1, len(textToPrint))
    print(textToPrint)
    menu_exit = 1
    while menu_exit == 1:
        menu_exit = 0
        textToPrint2 = "\tDesea agregar este servicio a su cuenta (1 - Si  ó  2 - No): "
        Mod_FancyThings.separator_thin(1, len(textToPrint2))
        buyItorNot = int(input(textToPrint2))
        match buyItorNot:
            case 1:
                None
            case 2:
                price = 0
            case _:
                menu_exit = menuerror(1)
                if menu_exit == 2:
                    Mod_FancyThings.message_warning("\tEl servicio no será agregado a su reserva")
                    price = 0
    return int(price)


def reservations_menu():
    Mod_FancyThings.fancyTitle("Módulo de reservas", "+")  # Titulo del módulo

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

    discountForOlds = 0.15

    mainMenuOP = 1  # Variable para controlar el ciclo de la reserva
    menuLvl = 0  # Variable para controlar los niveles de la reserva
    while mainMenuOP == 1:

        # Resertation Array
        # [0] = Tipo de estadía (D-N-H)     [1] = Día                       [2]  = Duración de hospedaje     [3]  = CheckIN
        # [4] = Número de cuarto            [5] = Cantidad de huespedes     [6]  = Tipo huésped 1            [7]  = Tipo huésped 2
        # [8] = Extra Food                  [9] = Extra Facilities          [10] = Extra All Inclusive       [11] = Extra Cantidad (solo para reservación por horas)
        # [12] = Monto Huésped 1            [13] = Monto Huésped 2          [14] = Número de reservación
        # reservation = ["","","","","","","","","","","","","","",""]
        reservation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        print("--- Nueva reserva ---")

        menuLvl = 1  # Variable que define el ciclo de vida del menu
        while menuLvl == 1:
            # Pregunta 1 - menuLvl 1
            menuLvl = 2  # Se prepara la variable para avanzar al siguiente paso/nivel, solo en caso de error vuelve a su valor anterior si el usuario desea reintentar
            print("\n"
                  "* Le ofrecemos las siguientes opciones de reserva (precio por persona):\n"
                  f"\t1 - Día completo por ${round(serv_motel * res_ratio_allDay, 2)}\n"
                  f"\t2 - Noche (12 hrs) por ${round(serv_motel * res_ratio_night, 2)}\n"
                  f"\t3 - Horas por ${round(serv_motel * res_ratio_hours, 2)}\n"
                  f"\t*** Adultos mayores reciben un 15% de descuento en el total de sus servicios")
            Mod_FancyThings.separator_thin(1, 42)  # Separador decorativo
            reservation[0] = int(input("\tEliga la opción de su preferencia (1-3): "))  # Tipo de estadía (D-N-H)

            if 0 < reservation[0] < 4:
                res_ratio_chosen = 0  # Variable que define el % para calcular el precio de los servicios según el tipo de reserva (D,N,H)
                match reservation[0]:
                    case 1:  # Reserva todo el día
                        res_ratio_chosen = res_ratio_allDay
                        reservation[2] = 24  # Duración de hospedaje
                        reservation[3] = 12  # CheckIN
                    case 2:  # Reserva toda la noche
                        res_ratio_chosen = res_ratio_night
                        reservation[2] = 12  # Duración de hospedaje
                        reservation[3] = 18  # CheckIN

                    case 3:  # Reserva por horas
                        res_ratio_chosen = res_ratio_hours
                        Mod_FancyThings.separator_thin(1, 43)
                        reservation[2] = int(input("\tCuántas horas se desea hospedar (01-23): "))  # Duración de hospedaje
                        Mod_FancyThings.separator_thin(1, 46)
                        reservation[3] = int(input("\tA qué hora desea ingresar al motel (00-23): "))  # CheckIN

                    case _:  # Error en nivel 1
                        retry = menuerror(1)
                        if retry == 2:  # Salir del menu
                            menuLvl = 0
                        elif retry == 1:  # Intentar reingresar el dato
                            menuLvl = 1

                while menuLvl == 2:
                    # Pregunta 2 - menuLvl 2
                    menuLvl = 3
                    print("\n"
                          "* Que día le gustaría reversar: \n"
                          "\t1 - Lunes \t\t 2 - Martes \t\t 3 - Miércoles \n"
                          "\t4 - Jueves\t\t 5 - Viernes \n"
                          "\t6 - Sábado \t\t 7 - Domingo")
                    Mod_FancyThings.separator_thin(1, 35)
                    reservation[1] = int(input("\tEliga el día de su reserva (1-7): "))  # Día de reserva

                    if 0 < reservation[1] < 8:

                        print()
                        Mod_FancyThings.loadingMessage("* Verificando disponibilidad.", 3)
                        rooms = Mod_Cipher_Rooms.checkRoomsAvailability(reservation[1], reservation[2],
                                                                        reservation[3])  # Se conecta a la BD y valida los cuartos disponibles

                        print("\n"
                              "* Basado en la información proporcianada tenemos los siguientes números de cuartos disponibles: \n"
                              f"\t{listAvailableRooms(rooms)}")

                        while menuLvl == 3:
                            # Pregunta 3 - menuLvl 3
                            menuLvl = 4
                            Mod_FancyThings.separator_thin(1, 40)
                            reservation[4] = int(input("\tCúal número de cuarto desea reservar: "))  # Número de cuarto

                            if checkRoom(rooms, reservation[4]):  # Válida si el cuarto elegido está en la lista de cuarto disponibles
                                while menuLvl == 4:
                                    # Pregunta 4 - menuLvl 4
                                    menuLvl = 5
                                    Mod_FancyThings.separator_thin(1, 43)
                                    reservation[5] = int(input("\tCúantas personas se van a hospedar (1-2): "))  # Cantidad de huespedes
                                    print("\n* Ingrese la clasificación para el húesped\n"
                                          "\t1 - Hombre\t\t\t\t\t\t2 - Mujer\n"
                                          "\t3 - Hombre Adulto Mayor \t\t4 - Mujer Adulta Mayor")

                                    match reservation[5]:  # Válida que la reserva no sea para más de 2 personas y les solicita la descripción a cada húesped
                                        case 1:
                                            reservation[6] = int(input("\tHúesped : "))
                                            if 0 > reservation[6] >= 5:  # Error nivel 4. Tipo de huesped
                                                retry = menuerror(1)
                                                if retry == 2:  # Salir del menu
                                                    menuLvl = 0
                                                elif retry == 1:  # Intentar reingresar el dato
                                                    menuLvl = 4
                                            reservation[7] = 0  # 0 = Vacio
                                        case 2:
                                            reservation[6] = int(input("\tHúesped 1 : "))
                                            reservation[7] = int(input("\tHúesped 2 : "))

                                            if (0 > reservation[6] >= 5) and (0 > reservation[7] >= 5):  # Error nivel 4. Tipo de huesped
                                                retry = menuerror(1)
                                                if retry == 2:  # Salir del menu
                                                    menuLvl = 0
                                                elif retry == 1:  # Intentar reingresar el dato
                                                    menuLvl = 4
                                        case _:  # Error nivel 2
                                            retry = menuerror(2)
                                            if retry == 2:  # Salir del menu
                                                menuLvl = 0
                                            elif retry == 1:  # Intentar reingresar el dato
                                                menuLvl = 4
                                    while menuLvl == 5:
                                        # Pregunta 5 - menuLvl 5
                                        print("\n* ¿Desea agregar un servicio adicional a su reserva?\n"
                                              "\tLe ofrecemos las siguientes opciones: \n"
                                              f"\t1 - Servicio de comida ${round(serv_food * res_ratio_chosen, 2)}\n"
                                              f"\t2 - Uso de las instalaciones ${round(serv_facilities * res_ratio_chosen, 2)}\n"
                                              f"\t3 - Sistema todo incluido ${round(serv_allInclusive * res_ratio_chosen, 2)}\n"
                                              "\t4 - No agregar adicionales\n"
                                              "\t*** Precios por persona")
                                        Mod_FancyThings.separator_thin(1, 19)
                                        reservation[11] = 1  # Si el servicio es por horas, define cuantos servicios desea contratar, si es por día o noche el default es 1
                                        extrasOP = int(input("\tElija una opción: "))
                                        match extrasOP:  # Procesa y guarda los valores de los servicios extra contratados
                                            case 1:  # Comida

                                                if reservation[0] == 3:
                                                    Mod_FancyThings.separator_thin(1, 112)
                                                    print("\tNuestro servicio de comidas en nuestro restaurante a la carta le permite elegir \n"
                                                          "\tla cantidad de comidas que desee contratar.")
                                                    Mod_FancyThings.separator_thin(1, 48)
                                                    reservation[11] = int(input("\tCuántas comidas desea contratar (por persona): "))
                                                else:
                                                    Mod_FancyThings.separator_thin(1, 102)
                                                    print(
                                                        "\tNuestro servicio de comidas en nuestro restaurante a la carta incluye todas comidas durante su estadía\n")

                                                price = menu_buyItOrNot(serv_food, res_ratio_chosen,
                                                                        reservation[11])  # Llama método que valida la compra y calcula el monto
                                                # Se guarda el precio del servicio extra contratado
                                                reservation[8] = price
                                                # Los demás extras van en 0
                                                reservation[9] = 0
                                                reservation[10] = 0
                                            case 2:  # Instalaciones
                                                if reservation[0] == 3:
                                                    reservation[11] = int(
                                                        input("\tCuántas horas desea utilizar las instalaciones (precio por persona): "))
                                                price = menu_buyItOrNot(serv_facilities, res_ratio_chosen,
                                                                        reservation[11])  # Llama método que valida la compra y calcula el monto
                                                # Se guarda el precio del servicio extra contratado
                                                reservation[9] = price
                                                # Los demás extras van en 0
                                                reservation[8] = 0
                                                reservation[10] = 0

                                            case 3:  # Todo incluido
                                                if reservation[0] == 3:
                                                    reservation[11] = reservation[2]
                                                    Mod_FancyThings.separator_thin(1, 83)
                                                price = menu_buyItOrNot(serv_allInclusive, res_ratio_chosen,
                                                                        reservation[11])  # Llama método que valida la compra y calcula el monto
                                                # Se guarda el precio del servicio extra contratado
                                                reservation[10] = price
                                                # Los demás extras van en 0
                                                reservation[8] = 0
                                                reservation[9] = 0
                                            case 4:  # Ningún servicio extra, todos van en 0
                                                reservation[8] = 0
                                                reservation[9] = 0
                                                reservation[10] = 0
                                                reservation[11] = 0

                                        finalPrice = 0
                                        match reservation[5]:
                                            # Cálculo de monto total por la cantidad de huéspedes y aplicación de descuentos si es necesario
                                            case 1:
                                                finalPrice += (serv_motel * res_ratio_chosen)  # Hospedaje
                                                finalPrice += reservation[8]  # Servicio de comida
                                                finalPrice += reservation[9]  # Servicio de instalaciones
                                                finalPrice += reservation[10]  # Servicio de todo incluido
                                                if 3 >= reservation[6] <= 4:
                                                    finalPrice = finalPrice - (finalPrice * discountForOlds)  # Descuento para adultos mayores
                                                reservation[12] = finalPrice
                                                reservation[13] = 0
                                            case 2:
                                                finalPrice += (serv_motel * res_ratio_chosen)  # Hospedaje
                                                finalPrice += reservation[8]  # Servicio de comida
                                                finalPrice += reservation[9]  # Servicio de instalaciones
                                                finalPrice += reservation[10]  # Servicio de todo incluido
                                                finalPrice = finalPrice  # Monto por 2 huespedes

                                                reservation[12] = finalPrice  # Precio para huésped1
                                                reservation[13] = finalPrice  # Precio para huésped2
                                                if 3 >= reservation[6] <= 4:  # Huesped 1
                                                    reservation[12] = reservation[12] - (
                                                                reservation[12] * discountForOlds)  # Descuento para adultos mayores
                                                if 3 >= reservation[7] <= 4:  # Huesped 2
                                                    reservation[13] = reservation[13] - (
                                                                reservation[13] * discountForOlds)  # Descuento para adultos mayores
                                                finalPrice = reservation[12] + reservation[13]

                                        print()
                                        Mod_FancyThings.separator_thin(0, 150)
                                        print(f"\n"
                                              f" *** El monto total de la reserva es de ${round(finalPrice, 2)}")
                                        confirm_res = int(input(" *** Desea confirmar su reserva (1 - Si  ó  2 - No): "))
                                        print()
                                        match confirm_res:
                                            case 1:  # Guardar datos en la base de datos
                                                Mod_FancyThings.loadingMessage(" *** Añadiendo reserva al sistema.", 3)
                                                print()
                                                reservation[14] = Mod_Cipher_Reservations.getNewReservationID()
                                                # print(reservation)
                                                print()
                                                # Se agrega la reservación al file de reservas
                                                Mod_Cipher_Reservations.addReservation(reservation)
                                                # Se actualiza el file de cuartos de acuerdo a la ocupación
                                                Mod_Cipher_Rooms.updateRoomAgenda(reservation[4], reservation[1], reservation[2], reservation[3])
                                                Mod_FancyThings.fancyTitle("Reserva registrada exitosamente\n"
                                                                           f"Su número de reserva es: {reservation[14]}", "»")
                                            case 2:  # Abortar la reservación
                                                Mod_FancyThings.message_warning("Su reservación ha sido cancelada.")
                                        menuLvl = 6

                            else:  # Error en nivel 3
                                retry = menuerror(1)
                                if retry == 2:  # Salir del menu
                                    menuLvl = 0
                                elif retry == 1:  # Intentar reingresar el dato
                                    menuLvl = 3
                    else:  # Error en nivel 2
                        retry = menuerror(1)
                        if retry == 2:  # Salir del menu
                            menuLvl = 0
                        elif retry == 1:  # Intentar reingresar el dato
                            menuLvl = 2

            else:  # Error en nivel 1
                retry = menuerror(1)
                if retry == 2:  # Salir del menu
                    menuLvl = 0
                elif retry == 1:  # Intentar reingresar el dato
                    menuLvl = 1
            Mod_FancyThings.separator_thin(0, 150)

        mainMenuOP = int(input("\nDesea realizar otra reservación: (1 - Si  ó  2 - No): "))
        Mod_FancyThings.separator(3)