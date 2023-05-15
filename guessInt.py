# Это игра по угадыванию чисел
import random

guessesTaken = 0

def getRandomInt():
    number = random.randint(1, 20)
    return number

    for number in range(6):
        return('Попробуй угадать.')
        guess = input()
        guess = int(guess)

        if guess < number:
            return('Твое число слишком маленькое.')

        elif guess > number:
            return('Твое число слишком большое.')

        elif guess == number:
            break

        elif guess == number:
        elif guessesTaken < 5:
            guessesTaken = str(guessesTaken + 1)
            return('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попытки!')
        guessesTaken = int(guessesTaken)
        elif guessesTaken > 4:
            guessesTaken = str(guessesTaken + 1)
            return('Отлично, ' + myName + '! Ты справился за ' + guessesTaken + ' попыток!')

    if guess != number:
        number = str(number)
        return('Увы. Я загадала число ' + number + '.')

number = 0
