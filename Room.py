
# Variables globales  (r= room)
r_number = None
r_dbID = None
r_reservationNumber = None
r_occupancy = None

class Room:
    def __init__(self, number, dbID, rawData):
        global r_number
        global r_dbID
        global r_reservationNumber
        global r_occupancy

        r_number= number
        r_dbID = dbID

        # Se crea una matriz de 4 dimensiones vacía para almacenar los datos del room, estos datos se almacenan en el mismo
        # formato en la base de datos, para conocer la estructura de esta matriz dirijase al archivo de datos rooms.chiper
        r_occupancy = [[[[None for _ in range(2)] for _ in range(1)] for _ in range(24)] for _ in range(7)]

        #Limpiando la información de la base de datos, se remueven caracteres no necesarios
        rawData = rawData [:2]
        rawData = rawData.replace('{')
        rawData = rawData.replace('}')



        #{"NDAYOFWEEK.NHOUR", "RESERVATIONNUMBER", "[MEN.WOMAN.OLDMEN.OLDWOMEN]", "[FOODCOST,FACILITIESFEE]"}



cuarto = Room("02",4,"[R02]= 1.08|MOT00001|")