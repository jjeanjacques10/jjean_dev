import random

from string import ascii_letters, digits, punctuation

caracteres = ascii_letters + digits + punctuation

senha_randomica = random.SystemRandom()

senha = "".join(senha_randomica.choice(caracteres) for i in range(10))

print(senha)