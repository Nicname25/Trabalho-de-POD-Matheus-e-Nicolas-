class ArquivoDeMidia:
    def __init__(self,titulo:str,duracao:int,artista:str,reproducoes:int):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista
        self.reproducoes = reproducoes
    def reproduzir(self):
        print(f"Reproduzindo {self.titulo} de {self.artista}")
    def __eq__(self,outro):
        return self.titulo == outro.titulo and self.artista == outro.artista