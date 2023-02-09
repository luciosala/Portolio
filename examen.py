
"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""


def max_num(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'error'

''''2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.

'''

def max_num3(n1,n2,n3):
    n = max_num(n1,n2)
    post = max_num(n, n3)
    return post





'''''
''''''
Args:
    n1:primer numero a comparar
    n2: segundo numero a acomoparar
    n3: tercer numero a comparar
Returns:
    int: numero mayor de los 3
guia: a > b > c
      b > c
      a > c

'''''






''''
Escribi una funcion que diga el largo de un string '''
def lenght(str):
    char = 0
    for  i in str:
        char += 1
    return char



'''' Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

'''

def is_vocal(char):
    if char.lower() in 'aeiou':
        return True
    else:
        return False



"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"'''"""''






"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range(longitud, 0):
        n = abs(n)
        nueva_cadena += cadena[n]
    return nueva_cadena
   



def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True
    else:
        return False
print(es_palindromo('arenera'))



