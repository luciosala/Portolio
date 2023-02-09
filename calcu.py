



def multiplicacion(n1,n2):
   result =  n1 * n2 
   return result
def suma(n1,n2):
    result = n1 + n2
    return result
def resta(n1,n2):
    result = n1 - n2
    return result
def potencia(n1,n2):
    result = n1 ** n2
    return result
def  division(n1,n2):
    result = n1 / n2
    return result
def calcu():
    operacion = input('Que operacion queres hacer \n')
    n1 = input('Primer numero? \n')
    n2 = input('Segundo Numero? \n')
    if operacion.lower() == 'suma' or '+':
        print(suma(n1,n2))
    elif operacion.lower() == 'resta' or '-':
        print(resta(n1,n2))
    elif operacion.lower() == 'division' or '/' or '\ ' or '%':
        print(division(n1,n2))
    elif operacion.lower() == '**' or 'potencia' or 'elevado':
        print(potencia(n1,n2))
    elif operacion.lower() == 'multiplicacion' or '**' or 'x':
        print(multiplicacion(n1,n2))
print(calcu)
