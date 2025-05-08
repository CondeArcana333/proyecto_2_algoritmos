# Proyecto1/Grafo.py
import arista as ari
import nodo as nod
import random  
import math
from collections import deque

# import pygame
class Grafo:
    def __init__(self, dirigido=False):

        self.nodos = {}  # Diccionario de nodos {valor: nodo}
        self.aristas = []  # Lista de aristas
        self.dirigido = dirigido

    def agregar_nodo(self, valor):

        if valor not in self.nodos:
            self.nodos[valor] = nod.Nodo(valor)
        return self.nodos[valor]

    def agregar_arista(self, origen, destino):

        nodo_origen = self.agregar_nodo(origen)
        nodo_destino = self.agregar_nodo(destino)
        
        arista = ari.Arista(nodo_origen, nodo_destino, self.dirigido)
        self.aristas.append(arista)
        
        nodo_origen.agregar_vecino(nodo_destino)
        if not self.dirigido:
            nodo_destino.agregar_vecino(nodo_origen)
        
        return arista

    def obtener_nodo(self, valor):

        return self.nodos.get(valor)

    def obtener_aristas(self):

        return self.aristas

    def obtener_nodos(self):

        return list(self.nodos.values())

    def existe_arista(self, origen, destino):

        nodo_origen = self.obtener_nodo(origen)
        nodo_destino = self.obtener_nodo(destino)
        
        if not nodo_origen or not nodo_destino:
            return False
            
        if self.dirigido:
            return nodo_destino in nodo_origen.obtener_vecinos()
        else:
            return (nodo_destino in nodo_origen.obtener_vecinos() or 
                    nodo_origen in nodo_destino.obtener_vecinos())

    def __str__(self):

        tipo = "Dirigido" if self.dirigido else "No dirigido"
        nodos = ", ".join(str(nodo.obtener_valor()) for nodo in self.obtener_nodos())
        aristas = "\n".join(str(arista) for arista in self.obtener_aristas())
        
        return f"Grafo ({tipo})\nNodos: [{nodos}]\nAristas:\n{aristas}"

    def grado_nodo(self, valor):

        nodo = self.obtener_nodo(valor)
        if not nodo:
            return 0
        
        if self.dirigido:
            # Para grafos dirigidos, calculamos grado de entrada y salida
            grado_salida = len(nodo.obtener_vecinos())
            grado_entrada = sum(1 for n in self.obtener_nodos() if nodo in n.obtener_vecinos())
            return ('Entrada='+str(grado_entrada),'Salida='+str( grado_salida))
        else:
            return len(nodo.obtener_vecinos())

    def archivo_grafo(self, valor):

        f = open(str(valor+".dot"), "w")
        f.write(str('graph '+valor+'={\n'))
        f.write(";\n".join(str(nodo.obtener_valor()) for nodo in self.obtener_nodos()))
        f.write(";\n")
        f.write(";\n".join(str(arista) for arista in self.obtener_aristas()))
        f.write(";\n}")
        f.close()
# grafo de malla
    def generar_malla(self,filas,columnas):

        
        # Conectar nodos horizontalmente
        for i in range(filas):
            for j in range(columnas - 1):
                origen = f"{i}_{j}"
                destino = f"{i}_{j+1}"
                self.agregar_arista(origen, destino)
        
        # Conectar nodos verticalmente
        for i in range(filas - 1):
            for j in range(columnas):
                origen = f"{i}_{j}"
                destino = f"{i+1}_{j}"
                self.agregar_arista(origen, destino)

#grafo erdonsreny
    def grafoErdosReny(self,nodos,aristas):

        # Crear nodos
        for i in range(nodos):
            self.agregar_nodo(i)
        
        i=0
        while(i<aristas):
            origen,destino=random.randint(0,nodos-1),random.randint(0,nodos-1)
            if self.existe_arista(origen,destino)==self.dirigido and origen != destino:
                self.agregar_arista(origen,destino)
                i+=1

#grafo gilbert
    def grafoGilbert(self,nodos,pro):

        for i in range(nodos):
            self.agregar_nodo(i)
        
        for i in range(nodos):
            origen = f"{i}"
            for j in range(nodos):
                destino = f"{j}"
                if random.random() < pro and origen != destino and self.existe_arista(origen,destino)==self.dirigido :
                    self.agregar_arista(origen,destino)

#grafo geométrico simple
    def grafoSimple(self,nodos,r):

        for i in range(0,nodos):
            cor_x,cor_y=random.randint(0,nodos),random.randint(0,nodos)
            self.agregar_nodo(f"{cor_x}|{cor_y}")
        
        for origen in self.obtener_nodos():
            cord=(origen.obtener_valor().split("|"))
            corx1,cory1=int(cord[0]),int(cord[1])
            for destino in self.obtener_nodos():
                cord2=(destino.obtener_valor().split("|"))
                corx2,cory2=int(cord2[0]),int(cord2[1])
                if math.dist([corx1, cory1], [corx2, cory2]) <= r and self.existe_arista(origen,destino)==self.dirigido and cord!=cord2:
                    self.agregar_arista(origen.obtener_valor(),destino.obtener_valor())

#grafo dorogovtsev mendes
    def GrafoDorogovtsevMendes(self,nodos):

        A,B,C = "0|0", "10|0", "5|10"
        self.agregar_arista(A,B)
        self.agregar_arista(B,C)
        self.agregar_arista(C,A)
        CorNodos=[]
        i=1
        while i<= nodos:
            AristaAle=random.choice(self.obtener_aristas())
            for nodo in AristaAle.obtener_nodos():
                CorNodos.append(nodo.obtener_valor())
            newNod=str(random.randint(-20,20))+'|'+str(random.randint(-20,20))
            if self.existe_arista(newNod,CorNodos[0])==self.dirigido:
                self.agregar_arista(newNod,CorNodos[0])
            if self.existe_arista(newNod,CorNodos[1])==self.dirigido:
                self.agregar_arista(newNod,CorNodos[1])
            CorNodos.pop()
            CorNodos.pop()
            i+=1

#grafo barabasi albert
    def grafoBarabasiAlbert(self,nodos,costomax):

        for valnodo in range(1,nodos+1):
            self.agregar_nodo(valnodo)
            for exisN in self.obtener_nodos():
                if self.grado_nodo(exisN.obtener_valor())<costomax and exisN.obtener_valor()!=valnodo:
                    Pv=1-((self.grado_nodo(exisN.obtener_valor()))/costomax)
                    if random.random() < Pv:
                        self.agregar_arista(exisN.obtener_valor(),valnodo)


    def BFS(self, inicio):
        """
        Busqueda a lo ancho 
        Explorar desde s y hacia fuera en todas las direcciones posibles, 
        añadiendo nodos una “capa” a la vez
        
        Args:
            nodo: Nodo inicial
        """ 
        arbolBFS= Grafo()
        
        nodo_inicio = self.obtener_nodo(inicio)
        if not nodo_inicio:
            return arbolBFS
        
        # Estructuras para BFS
        visitados = set()
        cola = deque()
        
        # Inicializar BFS
        cola.append(nodo_inicio)
        visitados.add(nodo_inicio.obtener_valor())
        
        while cola:
            nodo_actual = cola.popleft()
            
            # Explorar vecinos
            for vecino in nodo_actual.obtener_vecinos():
                valor_vecino = vecino.obtener_valor()
                if valor_vecino not in visitados:
                    visitados.add(valor_vecino)
                    cola.append(vecino)
                    arbolBFS.agregar_arista(nodo_actual.obtener_valor(),valor_vecino)
        return arbolBFS

    def DfsR(self, inicio):
        '''
        Busqueda a profundidad. Recursivamente
        Args:
            nodo: Nodo inicial
        '''
        nodo_inicio = self.obtener_nodo(inicio)
        if not nodo_inicio:
            return Grafo
        
        visitados = set()
        ArbolDfsR = Grafo()
        
        def Dfs(nodo):
            valor = nodo.obtener_valor()
            visitados.add(valor)
            
            for vecino in nodo.obtener_vecinos():
                if vecino.obtener_valor() not in visitados:
                    ArbolDfsR.agregar_arista(valor,vecino.obtener_valor())
                    Dfs(vecino)
        Dfs(nodo_inicio)
        return ArbolDfsR

    def DfsIte(self, inicio):
        """
        Búsqueda a profundidad iterativa que construye el árbol DFS.
        
        Args:
            grafo: Objeto de la clase Grafo
            inicio: Valor del nodo inicial

        Returns:
            Grafo que representa el árbol DFS construido
        """
        nodo_inicio = self.obtener_nodo(inicio)
        if not nodo_inicio:
            return Grafo()

        visitados = set()
        pila = [nodo_inicio]
        ArbolDfsI = Grafo()
        ArbolDfsI.agregar_nodo(nodo_inicio.obtener_valor())

        while pila:
            nodo_actual = pila.pop()
            valor_actual = nodo_actual.obtener_valor()
            if valor_actual not in visitados and nodo_actual not in ArbolDfsI.obtener_nodos():
                ArbolDfsI.agregar_nodo(valor_actual)
                visitados.add(valor_actual)
                for vecino in (nodo_actual.obtener_vecinos()):
                    valor_vecino = vecino.obtener_valor()
                    if valor_vecino not in visitados and vecino not in pila:
                        ArbolDfsI.agregar_nodo(valor_vecino)
                        pila.append(vecino)
                        ArbolDfsI.agregar_arista(valor_actual, valor_vecino)
        return ArbolDfsI

        