# mostrar mensaje de bienvenida
print("\nBienvenido a Aguas Termales Paraiso Azul")

# tarifas a tomar en cuenta denominadas como constantes
TARIFA1 = 1000 # tarifa para niños
TARIFA2 = 3000 # tarifa para adultos
TARIFA3 = 2000 # tarifa para adultos mayores

# mostrar al usuario los tipos de entrada
print("\nA continuacion se presentan las tarifas disponibles...\nTarifa 1 para niños:", TARIFA1,"\nTarifa 2 para adultos:", TARIFA2,"\nTarifa 3 para adultos mayores:", TARIFA3)

entrada_tipo1 = 0 # inicializacion de variable
entrada_tipo2 = 0 # inicializacion de variable
entrada_tipo3 = 0 # inicializacion de variable

pregunta1 = "si" # inicializacion de variable

# interaccion con el usuario
while pregunta1.lower() == "si":
    print("\n\nInserte el numero de tarifa que desea seleccionar.\n1 para niños\n2 para adultos\n3 para adultos mayores")
    seleccion = int(input("\nInserte la tarifa que desea seleccionar: "))
    cantidad_seleccion = int(input("Inserte la cantidad de entradas que desea comprar: "))
    print("Usted ha seleccionado ", cantidad_seleccion,"entradas para la tarifa", seleccion)

    if seleccion == 1:
        tarifa_total = TARIFA1*cantidad_seleccion
        print("El total por su seleccion es: ", tarifa_total)

        entrada_tipo1 += cantidad_seleccion
    elif seleccion == 2:
        tarifa_total = TARIFA2*cantidad_seleccion
        print("El total por su seleccion es: ", tarifa_total)

        entrada_tipo2 += cantidad_seleccion
    else:
        seleccion == 3
        tarifa_total = TARIFA3*cantidad_seleccion
        print("El total por su seleccion es: ", tarifa_total)

        entrada_tipo3 += cantidad_seleccion
    pregunta1 = input("Desea comprar mas entradas? ") # pregunta al usuario si desea comprar mas entradas o no

lista_entradas = [entrada_tipo1, entrada_tipo2, entrada_tipo3]
suma_de_lista = sum(lista_entradas)
print("total de entradas:",suma_de_lista)

# mostrar cantidad de entradas hasta el momento
print("\nUsted ha seleccionado las siguientes entradas: ")
if entrada_tipo1 > 0:
     print("Entrada para niño \n\tCantidad: \t",entrada_tipo1)
if entrada_tipo2 > 0:
     print("Entrada para adulto \n\tCantidad: \t",entrada_tipo2)
if entrada_tipo3 > 0:
     print("Entrada para adulto mayor \n\tCantidad: \t",entrada_tipo3)

# solicitar informacion de cada visitante
print("\nInserte la siguiente informacion de cada visitante")
for i in range(suma_de_lista):
    print("\nInserte la informacion de la persona ", i+1)
    nombre_completo = str(input("Inserte su nombre completo: "))
    cedula = str(input("Inserte su identificacion: "))
    while True:
        try:
            telefono = int(input("Inserte su numero de telefono: "))
            break
        except ValueError:
            print("Por favor ingresar un numero de telefono")
    correo = str(input("Inserte su correo electronico: "))
    direccion = str(input("Indique su direccion: "))
    nacional_extranjero = str(input("Indique si es nacional o extranjero: "))
    clase = str(input("Indique si es niño, adulto o adulto mayor: "))

# crear turnos
TURNO1 = " De 7:00 am a 12:00 pm "
TURNO2 = " De 12:30 pm a 5:30 pm "

# mostrar y solicitar el turno y horario
print("\nA continuacion se muestran los turnos a elegir: \nTurno 1: ",TURNO1,"\nTurno 2: ",TURNO2)
turno_seleccionado = input("\nDigite 1 para el turno 1 o Digite 2 para el turno 2: ")

if turno_seleccionado == "1" or turno_seleccionado.lower() == "turno 1":
    print("Usted ha seleccionado el turno 1 con horario de ",TURNO1)
else:
    turno_seleccionado == "2" or turno_seleccionado.lower() == "turno 2"
    print("Usted ha seleccionado el turno 2 con horario de ",TURNO2)

# solicitar fecha
print("\nInserte la fecha que desea reservar a continuacion")
while True:
    try:
        dia = int(input("Dia: "))
        break
    except ValueError:
        print("Digite el dia en formato numerico")
mes = str(input("Mes: "))
while True:
    try:
        year = int(input("Año: "))
        break
    except ValueError:
        print("Digite el año en formato numerico")
print("Fecha de reservacion: ",end="")
print(dia,mes,year,sep="/")

# solicitar encargado de registro de reserva
encargado = str(input("\nIngrese el nombre del encargado o encargada de su reserva: "))

# generar numero de reserva
from random import randint
numero_de_reserva = randint(0, 1000)

# operaciones para factura
IVA = 0.04 # constante representa el 4% de impuesto sobre el total
subtotal_niños = entrada_tipo1 * TARIFA1
subtotal_adultos = entrada_tipo2 * TARIFA2
subtotal_adultos_mayores = entrada_tipo3 * TARIFA3
suma_totales = subtotal_niños + subtotal_adultos + subtotal_adultos_mayores
impuesto_totales = suma_totales * IVA
total_neto = suma_totales + IVA

# GENERACION DE FACTURA
print("\n****************************************************")
print("\t\t\tFACTURA")
print("\nNumero de reserva: ",numero_de_reserva)
print("\nEntradas totales:",suma_de_lista,"\n")
if entrada_tipo1 > 0:
     print("Entrada para niño \n\tCantidad: \t",entrada_tipo1)
     print("subtotal: ", subtotal_niños)
if entrada_tipo2 > 0:
     print("Entrada para adulto \n\tCantidad: \t",entrada_tipo2)
     print("subtotal: ", subtotal_adultos)
if entrada_tipo3 > 0:
     print("Entrada para adulto mayor \n\tCantidad: \t",entrada_tipo3)
     print("subtotal: ", subtotal_adultos_mayores)
print("Subtotal de entradas: ", suma_totales)
print("IVA 4%: ", impuesto_totales)
print("Total: ", total_neto)
print("\nFecha de reservacion: ",end="")
print(dia,mes,year,sep="/")
print("\nEncargado: ", encargado)

print("\n****************************************************")

print("Gracias",encargado,"\nLe esperamos pronto!")