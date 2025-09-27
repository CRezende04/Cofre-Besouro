import random

def lancar_dados():
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    total = dado1 + dado2
    return total