character1 = 'x'
character2 = "a"


def crypt(phrase, character):
    crypt =""
    for letra in phrase:
        if letra in "aeiouóéíáú":
            if letra.isupper():
               crypt = crypt + character.upper
            else:
                crypt = crypt + character
            
        else:
                crypt = crypt + letra
    for letra in phrase:
        if letter in "bcdfghjklmnpqrstvwxyz":
            crypt = crypt + character2
        else:
            crypt = crypt + letter
    return crypt
while True :

        print(crypt(input("ingresa una frase: \n"), character))

        print("\n Ingresa 1 para seguir")
        print('ingresa 2 para terminar')
        opcion = input('>')
        if opcion == '2':
            break







        
           