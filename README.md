import random

# Define acceptable positive responses for restarting the game
ACCEPT_RESPONSES = ["ok", "si", "sí", "vale", "bien"]

def play_guessing_game():
    """Plays one round of the number guessing game."""
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("\n¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando un número entre 1 y 20. Tienes 5 intentos.")

    while intentos > 0:
        print(f"\nTe quedan {intentos} intentos.")
        
        try:
            intento_usuario = int(input("Introduce tu número: "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
            continue # Skip the rest of the current iteration and ask for input again
            
        if intento_usuario == numero_secreto:
            print(f"¡Felicidades! ¡Has acertado! El número era el {numero_secreto}.")
            return # Game over for this round (won)
        elif intento_usuario < numero_secreto:
            print("El número secreto es MÁS ALTO.")
        else:
            print("El número secreto es MÁS BAJO.")
            
        intentos -= 1

    # If loop finishes, attempts ran out
    print(f"\n¡Oh, te has quedado sin intentos! El número secreto era el {numero_secreto}.")
    # Game over for this round (lost)

# Main game loop to allow multiple rounds
while True:
    play_guessing_game() # Play one full round of the game

    # Ask the user if they want to play again
    while True: # Loop to ensure valid input for "play again" question
        respuesta_jugar_otra_vez = input("¿Quieres volver a jugar? (si/no): ").lower()
        if respuesta_jugar_otra_vez in ACCEPT_RESPONSES:
            print("¡Perfecto, aquí vamos otra vez!")
            break # Break from this inner loop to restart the main game loop
        elif respuesta_jugar_otra_vez == "no":
            print("Ok, ¡gracias por jugar!")
            exit()
        else:
            print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")
