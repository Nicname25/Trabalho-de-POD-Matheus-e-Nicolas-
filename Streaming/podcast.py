from Streaming.arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    def __init__(self, titulo: str, duracao: int, artista: str, episodio: int, temporada: str, host: str):
        super().__init__(titulo, duracao, artista, reproducoes=0)  # chama construtor da classe ArquivoDeMidia
        self.episodio = episodio
        self.temporada = temporada
        self.host = host

    def reproduzir(self):
        print(f"Reproduzindo podcast: {self.titulo} (Ep. {self.episodio}, Temp. {self.temporada}) - Host: {self.host}")
        self.reproducoes += 1

    def __str__(self):
        return f"Podcast: {self.titulo} | Ep.{self.episodio} Temp.{self.temporada} | Host: {self.host} | {self.reproducoes} reproduções"

    def __repr__(self):
        return f"Podcast(titulo={self.titulo}, episodio={self.episodio}, temporada={self.temporada})"