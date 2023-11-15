# -*- coding: utf-8 -*-
import sys
from gramatica import Gramatica

def ejemplo_6():
    terminales = ['if', 'then', 'else', 'a', 'b']
    no_terminales = ['instr', 'expr']
    gramatica = Gramatica(terminales, no_terminales, 'instr')
    lista_producciones_instr = [
        ['if', 'expr', 'then', 'instr'],
        ['if', 'expr', 'then', 'instr', 'else', 'instr'],
        ['a']
    ]
    lista_producciones_expr = [
        ['b']
    ]
    gramatica.agregar_producciones('instr', lista_producciones_instr)
    gramatica.agregar_producciones('expr', lista_producciones_expr)
    return gramatica

def ejemplo_5():
    terminales = ['+', '*', 'a', 'b']
    no_terminales = ['rexpr', 'rterm', 'rfactor', 'rprimario']
    gramatica = Gramatica(terminales, no_terminales, 'rexpr')
    lista_producciones_rexpr = [
        ['rexpr', '+', 'rterm'],
        ['rterm']
    ]
    lista_producciones_rterm = [
        ['rterm', 'rfactor'],
        ['rfactor']
    ]
    lista_producciones_rfactor = [
        ['rfactor', '*'],
        ['rprimario']
    ]
    lista_producciones_rprimario = [
        ['a', 'b']
    ]
    gramatica.agregar_producciones('rexpr', lista_producciones_rexpr)
    gramatica.agregar_producciones('rterm', lista_producciones_rterm)
    gramatica.agregar_producciones('rfactor', lista_producciones_rfactor)
    gramatica.agregar_producciones('rprimario', lista_producciones_rprimario)
    return gramatica


def ejemplo_4():
    # ! No funciona: recursion indirecta
    terminales = ['+', '*', '(', ')', 'id']
    no_terminales = ['E', 'Eprim', 'T', 'Tprim', 'F']
    gramatica = Gramatica(terminales, no_terminales, 'E')
    lista_producciones_E = [
        ['T', 'Eprim']
    ]
    lista_producciones_Eprim = [
        ['+', 'T', 'Eprim'],
        ['epsilon']
    ]
    lista_producciones_T = [
        ['F', 'Tprim']
    ]
    lista_producciones_Tprim = [
        ['*', 'F', 'Tprim'],
        ['epsilon']
    ]
    lista_producciones_F = [
        ['(', 'E', ')'],
        ['id']
    ]
    gramatica.agregar_producciones('E', lista_producciones_E)
    gramatica.agregar_producciones('Eprim', lista_producciones_Eprim)
    gramatica.agregar_producciones('T', lista_producciones_T)
    gramatica.agregar_producciones('Tprim', lista_producciones_Tprim)
    gramatica.agregar_producciones('F', lista_producciones_F)
    return gramatica


def ejemplo_3():
    terminales = ['a', '(', ')']
    no_terminales = ['S']
    gramatica = Gramatica(terminales, no_terminales, 'S')
    lista_producciones_S = [
        ['S', '(', 'S', ')', 'S'],
        ['a'],
        ['epsilon']
    ]
    gramatica.agregar_producciones('S', lista_producciones_S)
    return gramatica

def ejemplo_2():
    # ! No funciona: recursion indirecta 
    terminales = ['a', ',', '(', ')']
    no_terminales = ['S', 'L']
    gramatica = Gramatica(terminales, no_terminales, 'S')
    lista_producciones_S = [
        ['(', 'L', ')'],
        ['a']
    ]
    lista_producciones_L = [
        ['L', ',', 'S'],
        ['S']
    ]
    gramatica.agregar_producciones('S', lista_producciones_S)
    gramatica.agregar_producciones('L', lista_producciones_L)
    return gramatica

def ejemplo_1():
    terminales = ['0','1']
    no_terminales = ['S']
    gramatica = Gramatica(terminales, no_terminales, 'S')
    lista_producciones_S = [
        ['0', 'S', '1'],
        ['0', '1'],
        ['1', '0'],
        ['epsilon']
    ]
    #* La siguiente instrucción se realiza para cada no terminal
    gramatica.agregar_producciones('S', lista_producciones_S)

    return gramatica    

gramatica_seleccionada = ejemplo_6()
gramatica_seleccionada.generar()
gramatica_seleccionada.imprimir_tabla_afn()
print 'im done'

#tabla_transiciones = [['','0','1', 'epsilon'], [0, [], [], []]];


# gramatica_1 = {'S' : lista_producciones}

# def generar_tabla_transiciones(gramatica, tabla, terminales, no_terminales):
#     for key, value in gramatica.items():
#         estado_inicial = 0
#         print "la clave es " + key
#         lista_producciones = value
#         for produccion in lista_producciones:
#             estado_actual = estado_inicial
#             print "la produccion es " + str(produccion)
#             for i,c in enumerate(produccion):
#                 print "c es " + c
#                 if c in terminales:
#                     posicion_terminal = terminales.index(c)+1
#                     estado_siguiente = len(tabla) - 1
#                     fila_actual = tabla[estado_actual+1]
#                     lista_estados = fila_actual[posicion_terminal]
#                     lista_estados.append(estado_siguiente)                    
#                     nueva_fila = []
#                     nueva_fila.append(estado_siguiente)
#                     for t in terminales:
#                         nueva_fila.append([])
#                     nueva_fila.append([]) # para la transicion epsilon
#                     tabla.append(nueva_fila)
#                     estado_actual = estado_siguiente
#                 elif c == 'epsilon':
#                     posicion_terminal = len(terminales)+1
#                     fila_actual = tabla[estado_actual+1]
#                     lista_estados = fila_actual[posicion_terminal]
#                     estado_siguiente = len(tabla) - 1
#                     lista_estados.append(estado_siguiente)
#                     nueva_fila = []
#                     nueva_fila.append(estado_siguiente)
#                     for t in terminales:
#                         nueva_fila.append([])
#                     nueva_fila.append([]) # para la transicion epsilon
#                     tabla.append(nueva_fila)
#                     estado_actual = estado_siguiente
#                 elif c in no_terminales:
#                     posicion_terminal = len(terminales)+1
#                     fila_actual = tabla[estado_actual+1]
#                     lista_estados = fila_actual[posicion_terminal]
#                     if i == len(produccion) - 1:
#                         print "cumple la codicion"
#                         lista_estados.append(estado_actual)
#                     else:
#                         print "no cumple la condicion"
#                         estado_siguiente = len(tabla) - 1
#                         lista_estados.append(estado_siguiente)
#                         nueva_fila = []
#                         nueva_fila.append(estado_siguiente)
#                         for t in terminales:
#                             nueva_fila.append([])
#                         nueva_fila.append([]) # para la transicion epsilon
#                         tabla.append(nueva_fila)
#                         estado_actual = estado_siguiente
#                             # no voy a hacer recursion por el momento
#         break
    
#     print "im done for now"

# def generar_gramatica_1():
#     terminales = ['0','1']
#     no_terminales = ['S']
#     tabla_transiciones = [['','0','1', 'epsilon'], [0, [], [], []]];
#     e1 = ['0', 'S', '1']
#     e2 = ['0', '1']
#     e3 = ['1', '0']
#     e4 = ['epsilon']
#     lista_producciones = [e1, e2, e3, e4]
#     gramatica_1 = {'S' : lista_producciones}

#     generar_tabla_transiciones(gramatica_1, tabla_transiciones, terminales, no_terminales)
#     for fila in tabla_transiciones:
#         for item in fila:
#             print("{:>{}}".format(str(item)+"|", 10)),
#         print "\n------------------------------------------------"
# generar_gramatica_1()