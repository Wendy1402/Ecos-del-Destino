print("ECOS DEL DESTINO \n")
#Registro del jugador
Nombre = input("Ingresa tu nombre: ")
pistas = 0
#Historia principal
print("Bienvenido/a", Nombre, ", haz  despertado en un lugar desconocido. \n")
print("""
      No recuerdas quién eres ni como llegaste allí. El silencio es extraño y algo no parece estar bien.  
      Tú misión es descubrir la verdad detrás de los misteriosos sucesos y encontrar una forma de escapar.
      """)
#Exploración de la ciudad
print("\n ¿Qué deseas hacer?")
print("\n1. Explorar los alrededores")
print("2. Salir del juego \n")
explorar = 1
salir = 2
opcion = input("Escribe tu respuesta: ")
while opcion != "1" and opcion!= "2":
    print ("Opción in válida")
    opcion = input("Escribe tu respuesta: ")
if opcion == "1":
    print("Comienzas a explorar la ciudad, en busca de respuestas.")
    print("\n ¿Qué deseas hacer?")
    print("\n 1. Revisar edificios abandonados")
    print(" 2. Buscar en la plaza central.")
    print(" 3. Seguir un ruido extraño \n")
    edificios = 1
    plaza = 2
    ruido = 3
    ruta = input("Escribe tu respuesta: ")
    #Exploración de edificios abandonados
    if ruta == "1":
        print("""
              Entras a una casa en ruinas, entre muebles cubiertos de polvo encuentras una libreta vieja.
              En una de sus páginas aparece una referencia acerca de extraños sucesos en el hospital ocurrido años atrás.
              """)
        pistas = pistas + 1
        print("Obtienes una pista ", pistas)
    # Exploración de plaza central
    elif ruta =="2":
        print("""
              La plaza parece haber quedado congelada en el tiempo. 
              Buscas durante varios minutos, pero no encuentras información útil.
              Pero observas huellas que se dirigen hacia el bosque.
              Quizá allí haya respuestas 
              """)
    # Explora ruido extraño
    elif ruta == "3":
        print("""
              Mientras avanzas por una calle oscura escuchas pasos a la distancia. 
              De repente observas una sombra moviéndose entre los edificios.
              """)
        print("¿Qué deseas hacer?\n")
        print("1. Correr")
        print("2. Esconderte")
        print("3. Investigar \n")
        correr = 1
        esconderte = 2
        investigar = 3
        elegir = input("Escribe tu respuesta:")
        # Acontecimiento al correr
        if elegir == "1":
            print("Decides alejarte lo más rápido posible.")
            print("Logras escapar, pero pierdes la oportunidad de averiguar qué estaba ocurriendo.")
        # Acontecimiento al esconderse
        elif elegir == "2":
            print("Te ocultas detrás de unos escombros.")
            print("La sombra pasa cerca y deja caer un documento antes de desaparecer.")
            print("El documento parece ser un mapa antiguo con una marca sobre el hospital.")
            pistas = pistas + 1
            print("Obtienes una pista", pistas)
        # Acontecimiento al investigar
        elif elegir== "3":
            print("Decides acercarte con cautela")
            print("La figura parece haberse detenido.\n")
            print("¿Qué deseas hacer?\n")
            print("1. Acercarse lentamente")
            print("2. Gritar para llamar su atención \n")
            acercar= 1
            gritar = 2
            figura = input("Escribe tu respuesta:\n")
        # Descición respecto a la sombra
            if figura == "1":
                print("La figura desaparece entre la niebla, pero descubres marcas en el suelo que conducen a un lugar importante.")
                print("Al seguirlas, encuentras el símbolo del hospital grabado en una pared.")
                pistas = pistas + 1
                print("Obtienes una pista", pistas)
            elif figura == "2":
                print("La sombra nota tu presencia y huye.")
                print("Intentas seguirla, pero desaparece entre la niebla.")
                print ("Pierdes una pista importante")
            else:
                print ("Opción inválida")
                
    else: 
        print ("Opción inválida")
    #elegir ruta 
    print("\nDónde deseas continuar tu búsqueda?")
    print ("\n1. Hospital abandonado")
    print ("2. Bosque cubierto de niebla \n")
    hospital=1
    bosque=2
    ruta_final= input("Escribe tu respuesta: \n")
    #Ruta del hospital
    if ruta_final=="1":
        print("Te acercas al hospital abandonado")
        print("Las ventanas están rotas y el silencio resulta inquitante")
        print("¿Qué deseas hacer?\n")
        print("1. Revisar archivos")
        print("2. Bajar al sótano")
        if pistas >= 1:
            print("3. Revisar laboratorio")
        else:
            print("Parece que existe un área oculta en el hospital, pero no tienes suficiente información para encontrarla")
        archivos = 1
        sotano = 2
        laboratorio = 3
        decision = input("Escribe tu respuesta: \n")
        if decision == "1":
            print("Encuentras documentos ocultos entre los archivos del hospital")
            print("Los registros hablan de experimentos realizados en secreto hace varios años.")
        elif decision == "2":
            print("Desciendes lentamente por las escaleras")
            print("El aire se vuelve mas frío y una tenue luz parpadea al fondo del pasillo.")
            print("De repente escuchas un ruido extraño.\n")
            print("Qué deseas hacer?\n")
            print("1. Escapar")
            print("2. Investigar")
            print("1. Ocultarte\n")
            escapar=1
            invest=2
            ocultar=3
            hacer=input("Escribe tu respuesta: \n")
            if hacer == "1":
                print("Decides regresar rápidamente a la planta superior.")
                print("Logras ponerte a salvo, pero abandonas el lugar antes de descubrir que provoco el ruido.")
                print("Pierdes información importante.")
            elif hacer == "2":
                print ("Avanzas con cautela hacia el origen del sonido.")
                print("Encuentras documentos ocultos que confirman que se realizaron experimentos secretos.")
                print("Obtienes una pista clave.", pistas)
            elif hacer =="3":
                print("Te escondes detrás de unos estantes deteriorados.")
                print("Permaneces inmóvil durante varios minutos.")
                print("El ruido desaparece y consigues evitar cualquier peligro.")
                print("Evitaste el riesgo, pero no obtuviste información nueva.")
        elif decision == "3":
            print("Gracias a las pistas encontradas descubres una puerta oculta")
            print("Al entrar encuentras un laboratorio secreto")
            print("Los registros revelan que la ciudad fue abandonada después de que un experimento saliera mal.")
        else:
            print("Opción inválida")
    elif ruta_final == "2":
        print("Te adentras en el bosque")
        print("La niebla dificulta ver el camino y extraños sonidos resuenan entre los árboles.")
        print("\nQué deseas hacer?\n")
        print("1. Seguir una luz misteriosa")
        print("2. Explorar el bosque")
        print("3. Ignorar los sonidos")
        luz=1
        continuar=2
        ignorar=3
        camino=input("\nEscribe tu respuesta: \n")
        if camino =="1":
            print("Decides seguir una luz tenue entre los árboles")
            print("Después de camniar varios minutos, la niebla comienza a disiparse")
            print("Al salir del bosque descubres un edificio abandonado")
            print("Has llegado al hospital!")
            #llevar a hospital de nuevo
        elif camino == "2":
            print("Mientras exploras encuentras una mochila abandonada")
            print("Dentro hay documentos que mencionan al hospital")
            print("Obtienes una pista", pistas)
        elif camino == "3":
            print("Decides ignorar los extraños sonidos y continuar caminando.")
            print("La niebla se vuelve cada vez más espesa.")
            print("De repente, el suelo ced<e bajo tus pies.")
            #mandarlo a game over
        

elif opcion == "2":
    print("Game over ")

else:
    print("Opción inválida")