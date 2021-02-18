import random
import string

def password_generation(numbers, symbols, lenght):

    characters = string.ascii_letters
    if numbers:
        characters = characters + string.digits

    if symbols:
        characters = characters + string.punctuation

    generator = random.choices(characters,k=lenght)
    generator = " ".join(generator)

    return generator

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# characteres=(string.ascii_letters + string.digits + string.punctuation)

# slova=input('unesite 1 ako zelite slova ')
# brojevi=input('unesite 2 ako hocete brojeve i slova ')
# simboli=input('unesite 3 ako zelite simbole,slova i brojeve ')
# duzina=int(input('unesite duzinu: '))

# if slova == 1:
#     print(random.choices(string.ascii_letters , k=duzina))
# elif brojevi == 2:
#     print(random.choices(string.digits + string.ascii_letters, k=duzina))
# else :
#     print(random.choices(string.punctuation + string.ascii_letters + string.digits, k=duzina))
