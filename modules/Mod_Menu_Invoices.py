import time

from modules import Mod_Cipher_Reservations, Mod_FancyThings
from datetime import datetime

def invoices_menu():
    ch_line = "\n"
    # ch_tab = "\t"
    ch_tab = "     "

    Mod_FancyThings.fancyTitle("Módulo de facturas", "+")  # Titulo del módulo

    exit_menu = 1
    while exit_menu == 1:
        print(f"{ch_line}"
              f"* Para poder generar su factura necesitamos que ingrese los siguientes datos:{ch_line}")
        cxName = input(f"{ch_tab}Nombre Completo: ")
        cxID = input(f"{ch_tab}Número de cédula: ")
        cxEmail = input(f"{ch_tab}Correo Electrónico: ")
        cxReservationID = input(f"{ch_tab}Número de reservación: ")

        print(f"{ch_line}"
              f"{ch_tab}¡Gracias por su información!{ch_line}")

        Mod_FancyThings.loadingMessage(f"{ch_tab}Generando factura.",3)

        print()

        reservationInfo = Mod_Cipher_Reservations.lookForReservationID(cxReservationID)

        # Formula el campo a imprimir del item Servicios adicionales
        extras = ""
        if int(reservationInfo[0]) != 2:
            if float(reservationInfo[8]) != 0:
                extras = "Comida por tiempo de estadía"
            elif float(reservationInfo[9]) != 0:
                extras = "Uso de instalaciones por tiempo de estadía"
            elif float(reservationInfo[10]) != 0:
                extras = "Todo incluido por tiempo de estadía"
            else:
                extras = "N/a"
        else:
            if float(reservationInfo[8]) != 0:
                extras = f"Comida - Cantidad contratada por persona: {reservationInfo[11]}"
            elif float(reservationInfo[9]) != 0:
                extras = f"Uso de instalaciones - Horas contratadas por persona: {reservationInfo[11]}"
            elif float(reservationInfo[10]) != 0:
                extras = f"Todo incluído - Horas contratadas por persona: {reservationInfo[11]}"
            else:
                extras = "N/a"
        resident_kind = "Tipo de huésped"
        if int(reservationInfo[5]) == 1:
            resident_kind += f": {Mod_Cipher_Reservations.idTranslator(6, reservationInfo[6])}"
        elif int(reservationInfo[5]) == 2:
            resident_kind += (f"es: "
                              f"H1: {Mod_Cipher_Reservations.idTranslator(6, reservationInfo[6])}  |  "
                              f"H2: {Mod_Cipher_Reservations.idTranslator(7, reservationInfo[7])}")

        #Calculo del descuento para adulto mayor para el H1 y H2
        discountH1 = 0
        if int(reservationInfo[6]) == 3 or int(reservationInfo[6]) == 4:
            discountH1 = float(reservationInfo[12]) * 0.15
        else:
            discountH1 = 0
        discountH2 = 0
        if int(reservationInfo[7]) == 3 or int(reservationInfo[7]) == 4:
            discountH2 = float(reservationInfo[13]) * 0.15
        else:
            discountH2 = 0

        # Formula el campo a imprimir del item Monto a pagar
        cart = ""
        if int(reservationInfo[5] == 1):
            cart += f"El monto total a pagar es de ${reservationInfo[12]}. Descuento para adulto mayor aplicado: ${discountH1}"
        else:
            cart += (f"El monto total a pagar es de ${round(float(reservationInfo[12])+ float(reservationInfo[13]),2)}. Descuento para adulto mayor aplicado: ${round(discountH1+discountH2,2)}{ch_line}"
                     f"{ch_tab}Huésped 1: ${round(float(reservationInfo[12]),2)} | Descuento para adulto mayor: ${round(discountH1,2)}{ch_line}"
                     f"{ch_tab}Huésped 2: ${round(float(reservationInfo[13]),2)} | Descuento para adulto mayor: ${round(discountH2,2)}{ch_line}")

        time_stamp = datetime.now()


        invoice = (
                f"{ch_line}Factura Digital{ch_line}"
                f"---------------{ch_line*2}"
                f"Datos del comercio{ch_line}"
                f"{ch_tab}Nombre: Motel El Casquete S.A.{ch_line}"
                f"{ch_tab}Cédula juridica: 3-014-042113{ch_line}"
                f"Datos del cliente{ch_line}"
                f"{ch_tab}Nombre Completo: {cxName}{ch_line}"
                f"{ch_tab}Cédula física: {cxID}{ch_line}"
                f"{ch_tab}Correo Electrónico: {cxEmail}{ch_line}"
                f"Fecha de emisión de la factura: {time_stamp}{ch_line*3}"
                f"Reservación número {reservationInfo[14]}{ch_line}"
                f"----------------------------{ch_line}"
                f"{ch_tab}Tipo de reserva: {Mod_Cipher_Reservations.idTranslator(0,reservationInfo[0])}{ch_line}"
                f"{ch_tab}Cantidad de horas: {reservationInfo[2]}{ch_line}"
                f"{ch_tab}Día de ingreso: {Mod_Cipher_Reservations.idTranslator(1,reservationInfo[1])}{ch_line}"
                f"{ch_tab}Hora de ingreso: {reservationInfo[3]}{ch_line}"
                f"{ch_tab}Número de cuarto: {reservationInfo[4]}{ch_line}"
                f"{ch_tab}Cantidad de huéspedes: {reservationInfo[5]}{ch_line}"
                f"{ch_tab}{resident_kind}{ch_line}"
                f"{ch_tab}Servicios adicionales: {extras}{ch_line*3}"
                f"Monto a cancelar{ch_line}"
                f"----------------{ch_line}"
                f"{cart}{ch_line*2}"
                f"¡Gracias por visitarnos!{ch_line*2}")

        Mod_FancyThings.fancyTitle(invoice,"≡")
        time.sleep(5)
        exit_menu = int(input("Desea generar otra factura(1 - Si  ó  2 - No): "))