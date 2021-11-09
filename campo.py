class Campo:
    def _init_(self):
        self.coordenadas_de_borrachos = {}
    
    def añadir_borracho(self, Borracho, coordenada):
        self.coordenadas_de_borrachos[Borracho] = coordenada
    
    def mover_borracho(self, Borracho):
        delta_x, delta_y = Boracho_camina()
        coordenada_actual = self.coordenadas_de_borrachos[Borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)

        self.coordenadas_de_borrachos[Borracho] = nueva_coordenada
    
    def obtener_coordenada(self, Borracho):
        return self.coordenadas_de_borrachos[Borracho]
