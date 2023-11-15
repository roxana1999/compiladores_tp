# -*- coding: utf-8 -*-
from gramatica import Gramatica

def ejemplo_8():
    terminales = ['a', 'b']
    no_terminales = ['S']
    gramatica = Gramatica(terminales, no_terminales, 'S')
    lista_producciones_S = [
        ['a', 'S', 'b', 'S'],
        ['b', 'S', 'a', 'S'],
        ['epsilon']
    ]
    gramatica.agregar_producciones('S', lista_producciones_S)
    return gramatica

def ejemplo_7():
    terminales = ['+', '-', 'a']
    no_terminales = ['S']
    gramatica = Gramatica(terminales, no_terminales, 'S')
    lista_producciones_S = [
        ['+', 'S', 'S'],
        ['-', 'S', 'S'],
        ['a']
    ]
    gramatica.agregar_producciones('S', lista_producciones_S)
    return gramatica

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
    gramatica.agregar_producciones('S', lista_producciones_S)
    return gramatica