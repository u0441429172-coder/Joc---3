import random

# Defineix respostes positives acceptables per reiniciar el joc
ACCEPT_RESPONSES = ["ok", "si", "sí", "d'acord", "bé"]

def play_guessing_game():
    """Juga una ronda del joc d'endevinar el número."""
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("\nBenvingut al joc d'endevinar el número!")
    print("Estic pensant en un número entre 1 i 20. Tens 5 intents.")

    while intentos > 0:
        print(f"\nEt queden {intentos} intents.")
        
        try:
            intento_usuario = int(input("Introdueix el teu número: "))
        except ValueError:
            print("Entrada no vàlida. Si us plau, introdueix un nombre enter.")
            continue # Salta la resta de la iteració actual i torna a demanar entrada
            
        if intento_usuario == numero_secreto:
            print(f"Felicitats! Has encertat! El número era el {numero_secreto}.")
            return # Fi del joc per aquesta ronda (guanyada)
        elif intento_usuario < numero_secreto:
            print("El número secret és MÉS ALT.")
        else:
            print("El número secret és MÉS BAIX.")
            
        intentos -= 1

    # Si es completa el bucle, s'han acabat els intents
    print(f"\nOh, t'has quedat sense intents! El número secret era el {numero_secreto}.")
    # Fi del joc per aquesta ronda (perdut)

# Bucle principal per permetre múltiples rondes
while True:
    play_guessing_game() # Juga una ronda completa del joc

    # Pregunta a l'usuari si vol tornar a jugar
    while True: # Bucle per assegurar una entrada vàlida per la pregunta "tornar a jugar"
        respuesta_jugar_otra_vez = input("Vols tornar a jugar? (si/no): ").lower()
        if respuesta_jugar_otra_vez in ACCEPT_RESPONSES:
            print("Perfecte, som-hi una altra vegada!")
            break # Trenca aquest bucle interior per reiniciar el bucle principal
        elif respuesta_jugar_otra_vez == "no":
            print("D'acord, gràcies per jugar!")
            exit()
        else:
            print("Resposta no vàlida. Si us plau, escriu 'si' o 'no'.")
