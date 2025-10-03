from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist

class Usuario:
    qntd_instancias = 0  # contador global de usuários

    def __init__(self, nome: str):
        self.nome = nome
        self.playlists: list[Playlist] = []
        self.historico: list[ArquivoDeMidia] = []
        Usuario.qntd_instancias += 1

    def ouvir_midia(self, midia: ArquivoDeMidia):
        """Reproduz a mídia e adiciona ao histórico"""
        midia.reproduzir()
        self.historico.append(midia)

    def criar_playlist(self, nome: str) -> Playlist:
        """Cria uma nova playlist do usuário"""
        # impede duplicação de playlists com o mesmo nome
        for pl in self.playlists:
            if pl.nome == nome:
                raise ValueError("Já existe uma playlist com esse nome para este usuário.")
        nova = Playlist(nome, self)
        self.playlists.append(nova)
        return nova

    def __str__(self):
        return f"Usuário: {self.nome} | Playlists: {len(self.playlists)} | Histórico: {len(self.historico)} músicas"

    def __repr__(self):
        return f"Usuario(nome={self.nome})"
