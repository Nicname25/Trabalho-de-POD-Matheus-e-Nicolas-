from Streaming.arquivo_de_midia import ArquivoDeMidia

class Musica(ArquivoDeMidia):
    def __init__(self, titulo: str, duracao: int, artista: str, genero: str, avaliacoes: list[int] = None):
        super().__init__(titulo, duracao, artista, reproducoes=0)  # chama construtor da classe ArquivoDeMidia
        self.genero = genero
        self.avaliacoes = avaliacoes if avaliacoes else []  # inicia lista vazia se não for passada

    def reproduzir(self):
        print(f"Reproduzindo música: {self.titulo} - {self.artista} [{self.genero}]")
        self.reproducoes += 1

    def avaliar(self, nota: int):
        """Adiciona uma nota de 0 a 5 à lista de avaliações"""
        if 0 <= nota <= 5:
            self.avaliacoes.append(nota)
        else:
            raise ValueError("A nota deve estar entre 0 e 5.")

    def __str__(self):
        return f"Música: {self.titulo} ({self.genero}) | {self.artista} | {self.reproducoes} reproduções"

    def __repr__(self):
        return f"Musica(titulo={self.titulo}, artista={self.artista}, genero={self.genero})"