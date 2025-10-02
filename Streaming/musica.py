class Musica(ArquivoDeMidia):
    def __init__(self, titulo, duracao, artista, genero, avaliacoes=None):
        super().__init__(titulo, duracao, artista)
        self.genero = genero
        self.avaliacoes = avaliacoes if avaliacoes else []

    def reproduzir(self):
        print(f"Reproduzindo música: {self.titulo} de {self.artista}")
        self.reproducoes += 1