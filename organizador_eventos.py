"""
ORGANIZADOR DE EVENTOS
Objetivo: Usar funciones con parámetros y retorno para planificar un evento y calcular los costos.
Instrucciones:
1) Crea una función llamada «calcular_costo» que reciba como parámtros:
• num_personas (número de asistentes)
• costo_por_persona (costo por persona, con valor predeterminado de 1000)
• Retorne el costo total del evento.
2) Crea otra función llamada «crear_resumen» que reciba:
• nombre_evento (nombre del evento)
• num_personas (número de asistentes)
• costo_total (resultado de la función anterior)
• Retorne un resumen del evento como una cadena de texto.
3) Crear una función llamada «mostrar_resumen» que reciba el resumen del evento y lo imprima (sin retorno)
4) Diseña un programa que solicite al usuario los datos del evento y muestre el resumen final.
"""

# Función para calcular el costo del evento
def calcular_costo(num_personas, costo_por_persona):
    costo = num_personas * costo_por_persona
    return costo

# Función para crear un resumen del evento
def crear_resumen(nombre_evento, num_personas, costo_total):
    resumen = f'El evento "{nombre_evento}" recibirá {num_personas} visitantes. Dicho evento recaudará un total de ${costo_total}.'
    return resumen

# Función para mostrar el resumen del evento una vez que hayan valores para «nombre_evento», «num_personas» y «costo_total»
def mostrar_resumen(resumen):
    print(resumen)
    

print("ORGANIZADOR DE EVENTOS ♥")

# Ingreso de datos
evento = input('Ingrese el nombre del evento: ').capitalize()

while True:
    try:
        cantidad_personas = int(input(f'Ingrese la cantidad de personas que asistirán a "{evento}": '))
        break
    except ValueError:
        print("¡Error! El dato ingresado no es válido. Solo se aceptan números. Intente nuevamente.")

while True:
    try:
        precio_persona = int(input(f'Ingrese el valor por persona para asistir a "{evento}": $'))
        break
    except ValueError:
        print("¡Error! El dato ingresado no es válido. Solo se aceptan números. Intente nuevamente.")


costo_total = calcular_costo(cantidad_personas, precio_persona)

resumen_evento = crear_resumen(evento, cantidad_personas, costo_total)

mostrar_resumen(resumen_evento)

print('Gracias por utilizar "Organizador de eventos". ¡Adiós!')