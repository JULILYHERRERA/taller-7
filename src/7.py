from dataclasses import dataclass

class Elemento: 
    nombre: str 

def __eq__(self, other):
    return self.nombre== other.nombre

class Conjunto: 
    contador= contador

    def __init__(self, nombre_conjunto:str ):
        self.elementos= []
        self.nombre = nombre_conjunto

        Conjunto.contador += 1

    @property
    def __id(self):
        return self._id    

    def contiene (self, elemento:Elemento )-> bool :
        for e in self.elementos:
            if e.nombre == elementos:
                return True
    
        return False

    def agregar_elemento(self, elemento: Elemento):
            if not self.contiene(elemento):
                self.elementos.append(elemento)
                return True
            else:
                 return False

    def unir(self, otro_conjunto):
            for elemento in otro_conjunto.elementos:
                if not self.contiene(elemento):
                    self.elementos.append(elemento)
            
    def _add_(self, otro_conjunto):
                conjunto_2 = Conjunto(f"{self.nombre}_{otro_conjunto.nombre}")
                conjunto_2.elementos = self.elementos.copy()
                conjunto_2.unir(otro_conjunto)
                return conjunto_2

    @classmethod
   def intersectar(cls, conjunto, otro_conjunto):
        if (conjunto, Conjunto) and (otro_conjunto, Conjunto):
            interseccion_elementos = [elem for elem in conjunto.elementos if otro_conjunto.contiene(elem)]
            interseccion_nombre = f"{conjunto.nombre} INTERSECTADO {otro_conjunto.nombre}"
            interseccion_conjunto = Conjunto(interseccion_nombre)
            interseccion_conjunto.elementos = interseccion_elementos
            return interseccion_conjunto 

    def _str_(self):
        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"



