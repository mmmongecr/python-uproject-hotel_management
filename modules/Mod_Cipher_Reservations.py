from modules import Mod_CipherConnect


def getReservationsRawData():
    cipher = Mod_CipherConnect.CipherBox("reslog")
    reservations = cipher.read_data()
    for deleteRow in range(0,6):
        # Remueve las líneas no necesarias del file
        reservations.pop(0)

    for x in range(len(reservations)):
        reservations[x] = str.replace(reservations[x], "\n", "")
    return reservations

def getReservations():
    rawdata = getReservationsRawData()
    reservations = []
    for filler in range(len(rawdata)):
        # Convierte los datos del archivo a una matriz utilizable
        reservations.insert(len(reservations), str.split(rawdata[filler], "|"))
    return reservations


def getLastReservationID():
    lastID = 0
    reservations = getReservationsRawData()
    for x in range(len(reservations)):
        reservations[x] = str.replace(reservations[x], "RES", "")
        current_reservation = str.split(reservations[x], "|")
        if int(current_reservation[len(current_reservation) - 1]) > lastID:
            lastID = int(current_reservation[len(current_reservation) - 1])
    return lastID


def getNewReservationID():
    # Formato de ID de reservación
    # RES + 6 digitos
    newReservationID = "RES"

    newLastID = getLastReservationID() + 1
    newLastID = str(newLastID)  # Se convierte la variable newLastID a string
    for x in range(6 - len(newLastID)):  # Se agregan los ceros necesarios para completar el formato del ID de reservación
        newReservationID += "0"
    newReservationID += newLastID
    return newReservationID


def addReservation(reservation):
    reservationInfo = ""
    for x in range(len(reservation)):
        reservationInfo += str(reservation[x])
        if x != len(reservation) - 1:
            reservationInfo += "|"
    cipher = Mod_CipherConnect.CipherBox("reslog")
    cipher.add_data(reservationInfo + "\n")
    #print(reservationInfo)


def lookForReservationID(resID):
    resID = str.upper(resID)
    reservations = getReservationsRawData()
    reservationInfo = []
    for x in range(len(reservations)):
        current_reservation = str.split(reservations[x], "|")
        if current_reservation[len(current_reservation) - 1] == resID:
            reservationInfo = current_reservation
    return reservationInfo

def idTranslator(position,itemID):
    # Traduce el valor númerico de una posición en la matriz de reservación a su valor textual
    translation = ""
    reservationItemsDB = \
        [
            ["Día","Noche","Horas"],
            ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
            [""],
            [""],
            [""],
            [""],
            ["Hombre", "Mujer", "Hombre Adulto Mayor","Mujer Adulta Mayor"],
            [""],
            ["Comida"],
            ["Instalaciones"],
            ["Todo incluido"],
            [""],
            [""],
            [""],
            [""],
        ]
    if position == 7:
        position = 6
    # print(f"pocisition {position}\n"
    #       f"item {itemID}")
    return reservationItemsDB[int(position)][int(itemID)-1]

