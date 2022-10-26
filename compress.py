class Compress():

    def compress(self, text):
        self.compressed = []
        self.values = {}
        indice = 1
        lista_cadenas = text.split(' ') 
        
        for token in lista_cadenas:
            if not token in self.values:
                self.values[token] = indice
                indice = indice + 1

        for x in lista_cadenas:
            if x in self.values:
                y = self.values[x]
                self.compressed.append
        return self.compressed ,self.values

    def uncompress(self,compressed,values):
        text = ''
        lista_claves = list(values.keys())

        for token in compressed:
            token = token - 1 
            palabra = lista_claves[token]
            text = text + ' ' + palabra
            elimino_espacio = text.replace(text[0], '', 1)
        return elimino_espacio