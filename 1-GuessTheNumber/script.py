"""
Guess the Number uses several basic programming concepts: loops, if-
else statements, functions, method calls, and random numbers. Python’s
random module generates pseudorandom numbers—numbers that look ran-
dom but are technically predictable. Pseudorandom numbers are easier for
computers to generate than truly random numbers, and they’re considered
“random enough” for applications such as video games and some scientific
simulations.
Python’s random module produces pseudorandom numbers from a seed
value, and each stream of pseudorandom numbers generated from the
same seed will be the same. For example, enter the following into the inter-
active shell:
"""

import random 

# Función principal
def askForGuess():
    while True: 
        guess = input('> ') # Introduce el número

        if guess.isdecimal():
            return int(guess) # Convierte el número a un entero
        print('Introduce un número entre 1 y 100')

# Inicio del juego
print('GuessTheNumber, by Yw4rf https://yw4rf.vercel.app')
print()
secretNumber = random.radint(1,100) # Selecciona un número random
print('Elige un número entre el 1 y el 100')
