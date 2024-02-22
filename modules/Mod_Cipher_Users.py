from modules.Mod_CipherConnect import CipherBox


def getUsers(): # Crea una instancia de ChiperBox y lee la base de datos de usuarios
    cipher = CipherBox("udb")
    users = cipher.read_data()
    return users

def validate_user(user, passw):
    dbUsers = getUsers()

    validation = 0 # 1 = user&passw correctos | 2 = user incorrecto | 3 = passw incorrecto | 4 = user&passw incorrectos

    for x in range(0,len(dbUsers)): # Lee línea por linea la base de datos de usuarios
        temp_user = str.split(dbUsers[x],"|") # Separa cada línea en usuario y contraseña
        temp_user[1] = str.replace(temp_user[1],"\n","") # Se elimina salto de línea en la contraseña. Salto de línea por default al leer el dato
        val_user = str.lower(user) == str.lower(temp_user[0])
        val_passw = str(passw) == str(temp_user[1])

        if val_user == True:
            if val_passw == True:
                validation = 1
            else:
                validation = 3
            break # Los usuarios son únicos, por lo que cierra el for al encontrar el usuario correcto
        elif val_user == False:
            if val_passw == True:
                validation = 2
            else:
                validation = 4
    return validation
