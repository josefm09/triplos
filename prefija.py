# -*- coding: utf-8 -*-
import sys
import re
#example (6+4)*8(7+4)
print('Declare una expresion')
#ex = str(input()) #se almacena la expresion
ex = '(6+4)*8(7+4)'
valid = False #se inicializa una variable en falso, luego se utilizara
pila = [] #se inicializa la pila 
resultado = [] #se inicializa el arreglo de resultados
orderRes = '' #se inicializa el string del resultado ordenado
def prefija(value): #se declara la funcion prefija que lleva por parametro un valor
    for i in value: #se inicia un ciclo con el tamaño de la expresion
        if re.match('[a-zA-Z0-9-/?+?*?(?)]',i): #se pregunta si es una expresion correcta con expresiones regjulares
            valid = True #se cambia el valor a verdadero para seguir
        else: #si no termina el programa
            print('ingrese una expresion valida') 
            sys.exit()
    if valid:#si es valido continua la funcion
        value = value[::-1] #se invierte el orden de la expresion
        for j in value: #se inicia un ciclo para recorrer la expresion 
            if j in '+-*/)': #se buscan los operadores en la expresion
                pila.append(j) #si se encuentran se agregan a la pila
            if re.match('[a-zA-Z0-9]',j): #se buscan los numeros en la expresionm y las letras
                resultado.append(j) #se agregan al resultado
            if j == '(': #se busca en cierre de parentesis
                while pila: #se inicia un ciclo que mientras haya elementos en la pila 
                    resultado.append(pila.pop()) #se añadiran los elementos ultimos de la pila al resultado
        for n in resultado: #se recorre el resultado para eliminar los parentesis de cierre
            if n == ')':#si se encuentra 
                resultado.remove(n)#se elimina
prefija(ex)# se ejecuta la funcion
for n in reversed(resultado): #se recorre el resultado invertido 
    orderRes += n#para añadir los valores a un string

triplo(orderRes)# se ejecuta la función para imprimir los triplos

def triplo(value): #se declara la función que regresa las variables intermedias

print('Notacion infija ', ex)#se imprime la expresion original
print('Notacion prefija ',orderRes)#se imprime la expresion en prefija




                
