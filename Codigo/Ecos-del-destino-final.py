#Inicio
print("="*45)
print("              ECOS DEL DESTINO")
print("="*45)

# Registro del jugador
nombre = input("\nIngresa tu nombre: ")

# Sistema de pistas
pistas = 0

def mensaje():
    print("\n¿Qué deseas hacer?\n")
#Funciones para final
def final_bueno():
    print("""
Gracias a las pistas descubres cómo detener el experimento.

La sombra recupera su libertad.

Ambos logran salir de la ciudad.

🏆 FINAL BUENO
""")

def final_neutral():
    print("""
No logras descubrir toda la verdad.

Consigues escapar de la ciudad,
pero quedan muchas preguntas sin responder.

😐 FINAL NEUTRAL
""")

def final_alternativo():
    print("""
Abandonas el laboratorio.

Escapas con vida,
pero la verdad permanece oculta.

🏃 FINAL ALTERNATIVO
""")

def final_malo():
    print("""
La niebla cubre todo.

Pierdes el conocimiento y vuelves a olvidar quién eres.

💀 FINAL MALO
""")
#Funcion para laboratorio
def laboratorio():
    global pistas

    print("""
Encuentras un laboratorio secreto.

Los documentos revelan que un experimento tecnológico salió mal.

La sombra aparece frente a ti.

"No pude escapar... pero tú aún puedes hacerlo."
""")

    mensaje()

    print("1. Ayudar a la sombra")
    print("2. Escapar inmediatamente")

    opcion = input("Escribe tu respuesta: ")

    if opcion == "1":
        if pistas >= 3:
            final_bueno()
        else:
            final_neutral()

    elif opcion == "2":
        final_alternativo()

    else:
        print("Opción inválida")
        return
#Función para ciudad
def ciudad():
    global pistas

    print("\nBienvenido/a", nombre, ", has despertado en un lugar desconocido.")

    print("""
No recuerdas quién eres ni cómo llegaste allí.
El silencio es extraño y algo no parece estar bien.

Tú misión es reunir al menos tres pistas para descubrir la verdad.
Tus decisiones determinarán tu destino.
""")

    mensaje()

    print("1. Explorar los alrededores")
    print("2. Salir del juego")

    opcion = input("Escribe tu respuesta: ")
#Bucle
    while opcion != "1" and opcion != "2":
        print("Opción inválida")
        opcion = input("Escribe tu respuesta: ")

    if opcion == "2":
        print("""Gracias por jugar.
              
              GAME OVER
              """)
        return

    print("\nComienzas a explorar la ciudad.")

    mensaje()

    print("1. Revisar edificios abandonados")
    print("2. Buscar en la plaza central")
    print("3. Seguir un ruido extraño")

    ruta = input("Escribe tu respuesta: ")
#Primera decisión
    if ruta == "1":
        print("""
Entras a una casa en ruinas.

Encuentras una libreta vieja con información
sobre sucesos extraños en el hospital.
""")
        pistas += 1
        print("Obtienes una pista:", pistas)

    elif ruta == "2":
        print("""
La plaza parece congelada en el tiempo.

No encuentras información,
pero observas huellas que llevan hacia el bosque.
""")

    elif ruta == "3":

        print("""
Escuchas pasos a la distancia.

Una sombra aparece entre los edificios.
""")
        mensaje()

        print("1. Correr")
        print("2. Esconderte")
        print("3. Investigar")

        decision = input("Escribe tu respuesta: ")

        if decision == "1":

            print("""
Escapas rápidamente.

Pero pierdes la oportunidad
de descubrir qué ocurrió.
""")

        elif decision == "2":

            print("""
Te escondes detrás de unos escombros.

La sombra deja caer un documento
con una marca del hospital.
""")

            pistas += 1
            print("Obtienes una pista:", pistas)

        elif decision == "3":

            print("""
Te acercas lentamente.

La figura desaparece,
pero encuentras marcas que llevan al hospital.
""")

            pistas += 1
            print("Obtienes una pista:", pistas)

        else:
            print("Opción inválida")

    else:
        print("Opción inválida")
    
    print("\n¿Dónde deseas continuar tu búsqueda?")
#Decisión de hospital o bosque
    print("1. Hospital abandonado")
    print("2. Bosque cubierto de niebla")

    ruta_final = input("Escribe tu respuesta: ")

    if ruta_final == "1":
        hospital()

    elif ruta_final == "2":
        bosque()

    else:
        print("Opción inválida")
def hospital():
    global pistas

    print("""
Te acercas al hospital abandonado.

Las ventanas están rotas y el lugar parece estar vacío.
""")

    mensaje()

    print("1. Revisar archivos")
    print("2. Bajar al sótano")

    if pistas >= 1:
        print("3. Revisar laboratorio")

    decision = input("Escribe tu respuesta: ")

    if decision == "1":

        print("""
Encuentras documentos antiguos.

Hablan de un experimento tecnológico
que salió mal y provocó el abandono de la ciudad.
""")

        pistas += 1
        print("Obtienes una pista:", pistas)

        print("""
Entre los documentos encuentras un plano.

El plano muestra una puerta oculta.
""")

        laboratorio()


    elif decision == "2":

        print("""
Bajas lentamente al sótano.

El lugar está oscuro y escuchas un ruido extraño.
""")

        mensaje()

        print("1. Escapar")
        print("2. Investigar")
        print("3. Ocultarte")

        opcion = input("Escribe tu respuesta: ")


        if opcion == "1":

            final_neutral()


        elif opcion == "2":

            print("""
Sigues el sonido.

Encuentras documentos secretos
sobre el experimento.
""")

            pistas += 1
            print("Obtienes una pista:", pistas)

            laboratorio()

        elif opcion == "3":

            print("""
Te escondes y esperas.

El ruido desaparece.

Decides abandonar el hospital.
""")
            final_neutral()

        else:
            print("Opción inválida")

    elif decision == "3" and pistas >= 1:

        laboratorio()

    else:
        print("Opción inválida")
#Bosque
def bosque():
    global pistas

    print("""
Te adentras en el bosque.

La niebla dificulta ver el camino
y extraños sonidos resuenan entre los árboles.
""")

    mensaje()

    print("1. Seguir una luz misteriosa")
    print("2. Explorar el bosque")
    print("3. Ignorar los sonidos")

    camino = input("Escribe tu respuesta: ")

    if camino == "1":

        print("""
Sigues una luz entre los árboles.

Después de varios minutos...

¡Has llegado al hospital!
""")
        hospital()

    elif camino == "2":

        print("""
Encuentras una mochila abandonada.

Dentro hay documentos
que hablan del hospital.
""")

        pistas += 1
        print("Obtienes una pista:", pistas)

        print("""
Las huellas continúan...

Llegas al hospital.
""")

        hospital()

    elif camino == "3":

        final_malo()

    else:

        print("Opción inválida")
ciudad()