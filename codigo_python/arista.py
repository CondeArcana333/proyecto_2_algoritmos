#prueba_git
#creacion de la clase arista

class Arista:
    def __init__(self, origen, destino, dirigida=False):

        self.origen = origen
        self.destino = destino
        self.dirigida = dirigida
    
    def obtener_nodos(self):

        return (self.origen, self.destino)
    
    def es_dirigida(self):

        return self.dirigida
    
    def __str__(self):
 
        direccion = "->" if self.dirigida else "--"
        return f"{self.origen.obtener_valor()} {direccion} {self.destino.obtener_valor()}"
    