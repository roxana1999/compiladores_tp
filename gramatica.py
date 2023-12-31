# -*- coding: utf-8 -*-
NRO_MAXIMO_DE_RECURSIONES = 3
NRO_MAXIMO_DE_RECURSIONES_INDIRECTAS = 1 
class Gramatica:
    def __init__(self, terminales, no_terminales, simbolo_inicial):
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.gramatica = {}
        self.simbolo_inicial = simbolo_inicial
    
    def agregar_producciones(self, no_terminal, lista_producciones):
        self.gramatica[no_terminal] = lista_producciones
        self.tabla_transiciones = {}
        self.tabla_afd = {}
        header = ['']
        fila = [0]
        for c in self.terminales:
            header.append(c)
            fila.append([])
        header.append('epsilon')
        fila.append([])
        self.tabla_transiciones['cabecera'] = header
        self.tabla_transiciones['filas'] = [fila]

        header = ['']
        fila = [[0]]
        for c in self.terminales:
            header.append(c)
            fila.append([])
        self.tabla_afd['cabecera'] = header
        self.tabla_afd['filas'] = [fila]
    
    def crear_nueva_fila(self, estado_siguiente):
        nueva_fila = []
        nueva_fila.append(estado_siguiente)
        for t in self.terminales:
            nueva_fila.append([])
        nueva_fila.append([]) # para la transicion epsilon
        return nueva_fila

    def generar_tabla_transiciones(self, estado_inicial, no_terminal, recursiones_restantes, recursiones_indirectas_restantes, simbolos_predecesores):
        estados_finales = []
        print "Simbolo no terminal: " + no_terminal
        lista_producciones = self.gramatica[no_terminal]
        for produccion in lista_producciones:
            print "-> La produccion es: " + str(produccion)
            estado_actual = estado_inicial
            for i,char in enumerate(produccion):
                print "----> char es " + char
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
                        print "----> cumple la codicion de recursion al final de la produccion"
                        lista_estados.append(estado_inicial)
                    else:
                        estado_siguiente = len(self.tabla_transiciones['filas'])
                        lista_estados.append(estado_siguiente)
                        nueva_fila = self.crear_nueva_fila(estado_siguiente)
                        self.tabla_transiciones['filas'].append(nueva_fila)
                        estado_actual = estado_siguiente
                        if char != no_terminal:
                            estado_actual = self.generar_tabla_transiciones(estado_actual, char, NRO_MAXIMO_DE_RECURSIONES, NRO_MAXIMO_DE_RECURSIONES_INDIRECTAS, simbolos_predecesores)
                        else: 
                            print "----> cumple la condicion de recursion al inicio o en medio de la produccion"
                            #* char es sigual al símbolo no terminal, hacer recursión
                            if recursiones_restantes > 0:
                                print "----> Nueva fila agregada a la tabla: ",
                                print self.tabla_transiciones['filas'][estado_actual]
                                print "----> Llamar a recursion para " + no_terminal + "con recursiones restantes = " + str(recursiones_restantes)
                                estado_actual = self.generar_tabla_transiciones(estado_actual, char, recursiones_restantes - 1, NRO_MAXIMO_DE_RECURSIONES_INDIRECTAS, simbolos_predecesores)
                                print "----> Fin de llamado a recursion para " + no_terminal + "con recursiones restantes = " + str(recursiones_restantes)
                            else:
                                #* Se llegó al límite de recursiones
                                print "----> Se llego al limite de recursiones"                            
                        if i == len(produccion) - 1:
                            estados_finales.append(estado_actual)
                print "----> Nueva fila agregada a la tabla: ",
                print self.tabla_transiciones['filas'][estado_actual]
                        
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
        estado_inicial = 0
        simbolos_predecesores= {}
        #print "la clave es " + key
        self.generar_tabla_transiciones(estado_inicial, self.simbolo_inicial, NRO_MAXIMO_DE_RECURSIONES, NRO_MAXIMO_DE_RECURSIONES_INDIRECTAS, simbolos_predecesores)
        
    
    def imprimir_tabla_afn(self):
        print "\n\n--------------------TABLA AFN-------------------"
        print "------------------------------------------------"
        for titulo in self.tabla_transiciones['cabecera']:
            print("{:^{}}".format(str(titulo), 10)+"|"),
        print "\n------------------------------------------------"

        for fila in self.tabla_transiciones['filas']:
            for item in fila:
                print("{:^{}}".format(str(item), 10)+"|"),
            print "\n------------------------------------------------"
    
    # def generar_afd(self):
    #     Destados = [self.cerradura_e(0)] #Inicializar Destados con c-e(0)
    #     hay_estados_sin_marcar = True

    #     while hay_estados_sin_marcar:
    #         for i, item in enumerate(Destados):
    #             print ("i es", i)
    #             if item["marcado"] == "no":
    #                 item["marcado"] = "si" # marcar T
    #                 for char in self.terminales:
    #                     cerradura_e = []
    #                     lista_mover = self.mover(item["cerradura"], char)
    #                     for estado in lista_mover:
    #                         cerradura_para_estado = self.cerradura_e(estado)
    #                         for c in cerradura_para_estado:
    #                             if c not in cerradura_e:
    #                                 cerradura_e.append(c)
    #                     cerradura_e.sort()
    #                     if !self.cerradura_e_ya_existe(cerradura_e, Destados):
    #                         posicion_char = self.terminales.index(char)+1
    #                         index_de_mi_simbolo_padre = self.tabla_afd['filas']

    #                         nueva_fila = []
    #                         nueva_fila.append(cerradura_e)
    #                         for t in self.terminales:
    #                             nueva_fila.append([])
    #                         self.tabla_afd['filas'].append(nueva_fila)
    #                         Destados.append({"cerradura": cerradura_e, "marcado": "no"})
    #                         # es nueva cerradura y debo añadir nueva fila           


    def cerradura_e_ya_existe(self, cerradura_e, Destados):
        for item in Destados:
            if item["cerradura"] == cerradura_e:
                return True
        return False
    
    def mover(self, cerradura, char):
        print "-> Mover " + str(cerradura) + " con char " + char 
        lista_mover = []
        for estado in cerradura:
            estados_accesibles_con_char = self.tabla_transiciones['filas'][estado][self.terminales.index(char)+1]
            for e in estados_accesibles_con_char:
                if e not in lista_mover:
                    lista_mover.append(e)
        return lista_mover.sort()

    def cerradura_e(self, estado):
        cerradura_e = {"cerradura": [estado], "marcado": "no"}
        estados_desde_e = self.obtener_estados_desde_e(estado)
        self.agregar_estados(estados_desde_e, cerradura_e)
        print "cerradura_e para el estado "+str(estado)+": "+str(cerradura_e)
        cerradura_e["cerradura"].sort()
        print "cerradura_e ordenada: " + str(cerradura_e["cerradura"])
        return cerradura_e
    
    def obtener_estados_desde_e(self, estado):
        fila = self.tabla_transiciones['filas'][estado]
        columna_e = len(self.terminales)+1
        return fila[columna_e]

    def agregar_estados(self, estados_desde_e, cerradura_e):
        for estado in estados_desde_e:
            if estado not in cerradura_e["cerradura"]:
                cerradura_e["cerradura"].append(estado)
                estados_desde_e = self.obtener_estados_desde_e(estado)
                self.agregar_estados(estados_desde_e, cerradura_e)