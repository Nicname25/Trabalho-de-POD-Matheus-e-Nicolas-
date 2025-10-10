from abc import ABC, abstractmethod

class ArquivoDeMidia(ABC):
    """
    Essa classe serve para ser usada pela música e pelo podcast para criar uma música ou podcast.
    Incluindo titulo, duração, artista a as reproduções.
    """

    def __init__(self, titulo: str, duracao: int, artista: str, reproducoes: int = 0):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista
        self.reproducoes = reproducoes

    @abstractmethod
    def reproduzir(self):
        pass

    def __eq__(self, outro):
        """Dois arquivos de mídia são iguais se tiverem mesmo título e artista"""
        return self.titulo == outro.titulo and self.artista == outro.artista

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracao}s, {self.reproducoes} reproduções)"

    def __repr__(self):

        return f"ArquivoDeMidia(titulo={self.titulo}, artista={self.artista})"
