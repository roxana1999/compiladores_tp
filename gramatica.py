# -*- coding: utf-8 -*-
class Gramatica:
    def __init__(self, terminales, no_terminales):
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.gramatica = {}
    
    def agregar_producciones(self, no_terminal, lista_producciones):
        self.gramatica[no_terminal] = lista_producciones
        self.tabla_transiciones = {}
        header = ['']
        fila = [0]
        for c in self.terminales:
            header.append(c)
            fila.append([])
        header.append('epsilon')
        fila.append([])
        self.tabla_transiciones['cabecera'] = header
        self.tabla_transiciones['filas'] = [fila]
    
    def crear_nueva_fila(self, estado_siguiente):
        nueva_fila = []
        nueva_fila.append(estado_siguiente)
        for t in self.terminales:
            nueva_fila.append([])
        nueva_fila.append([]) # para la transicion epsilon
        return nueva_fila

    def generar_tabla_transiciones(self, estado_inicial, no_terminal):
        estados_finales = []
        print "la clave es" + no_terminal
        lista_producciones = self.gramatica[no_terminal]
        for produccion in lista_producciones:
            print "la produccion es " + str(produccion)
            estado_actual = estado_inicial
            for i,char in enumerate(produccion):
                print "char es " + char
                fila_actual = self.tabla_transiciones['filas'][estado_actual]
                if char in self.terminales or char == 'epsilon':
                    if char == 'epsilon':
                        posicion_terminal = len(self.terminales)+1
                    else:
                        posicion_terminal = self.terminales.index(char)+1
                    lista_estados = fila_actual[posicion_terminal]
                    estado_siguiente = len(self.tabla_transiciones['filas'])
                    lista_estados.append(estado_siguiente)                    
                    nueva_fila = self.crear_nueva_fila(estado_siguiente)
                    self.tabla_transiciones['filas'].append(nueva_fila)
                    estado_actual = estado_siguiente
                    # verificar si es el último caracter
                    if i == len(produccion) - 1:
                        estados_finales.append(estado_actual)
                elif char in self.no_terminales:
                    posicion_terminal = len(self.terminales)+1
                    lista_estados = fila_actual[posicion_terminal]
                    if i == len(produccion) - 1 and char == no_terminal:
                        print "cumple la codicion de recursion al final de la produccion"
                        lista_estados.append(estado_inicial)
                    else:
                        print "no cumple la condicion de recursion al final de la produccion"
                        estado_siguiente = len(self.tabla_transiciones['filas'])
                        lista_estados.append(estado_siguiente)
                        nueva_fila = self.crear_nueva_fila(estado_siguiente)
                        self.tabla_transiciones['filas'].append(nueva_fila)
                        estado_actual = estado_siguiente
                        if char != no_terminal:
                            estado_actual = self.generar_tabla_transiciones(estado_actual, char)
                        else:
                            pass
                            # no voy a hacer recursion por el momento
                            # todo: hacer recursion
                        if i == len(produccion) - 1:
                            estados_finales.append(estado_actual)
                        
        # * Actualizar estados finales
        estado_ultimo = len(self.tabla_transiciones['filas'])
        nueva_fila = self.crear_nueva_fila(estado_ultimo)
        self.tabla_transiciones['filas'].append(nueva_fila)        
        for estado in estados_finales:
            posicion_terminal = len(self.terminales)+1
            fila_actual = self.tabla_transiciones['filas'][estado]
            lista_estados = fila_actual[posicion_terminal]
            lista_estados.append(estado_ultimo)
        estado_actual = estado_ultimo
        
        return estado_actual

    def generar(self):
        for key, value in self.gramatica.items():
            estado_inicial = 0
            #print "la clave es " + key
            self.generar_tabla_transiciones(estado_inicial, key)
            break
    
    def imprimir_tabla_afn(self):
        print "--------------------TABLA AFN-------------------"
        print "------------------------------------------------"
        for titulo in self.tabla_transiciones['cabecera']:
            print("{:^{}}".format(str(titulo), 10)+"|"),
        print "\n------------------------------------------------"

        for fila in self.tabla_transiciones['filas']:
            for item in fila:
                print("{:^{}}".format(str(item), 10)+"|"),
            print "\n------------------------------------------------"