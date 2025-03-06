# Se crea un programa en el cual se solicita por consola
# Nombre, Apellido y Año de nacimiento y se generará un ID
# con
from random import randint

print("**** Sistema de Generador de ID Unico ****")
name = input("Cual es tu nombre?: ")
name_id = name[0:2].upper()
last_name = input("Cual es tu apellido?: ")
last_name_id = last_name[0:2].upper()
birthday = input("Cual es tu año de nacimiento (YYYY)?: ")
birthday_id = birthday[2:4]

# Se genera un valor de 4 digitos aleatorio
aleatorio = randint(0,9999)

id_unico = f"{name_id}{last_name_id}{birthday_id}{aleatorio}"


print(f"""Hola {name}, habitante de ciudad gotica!
    Tu nuevo numero de identificacion (ID) generado por sistema es:
    {id_unico}
    Felicitaciones!
""")