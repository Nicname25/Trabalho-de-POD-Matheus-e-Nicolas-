from Streaming.musica import Musica
from Streaming.playlist import Playlist
from Streaming.usuario import Usuario

class Analises:
    @staticmethod
    def top_musicas_reproduzidas(musicas: list[Musica], top_n: int) -> list[Musica]:
        """Retorna as top_n músicas mais reproduzidas"""
        if not musicas:
            return []
        return sorted(musicas, key=lambda m: m.reproducoes, reverse=True)[:top_n]

    @staticmethod
    def playlist_mais_popular(playlists: list[Playlist]) -> Playlist | None:
        """Retorna a playlist mais reproduzida"""
        if not playlists:
            return None
        return max(playlists, key=lambda p: p.reproducoes)

    @staticmethod
    def usuario_mais_ativo(usuarios: list[Usuario]) -> Usuario | None:
        """Retorna o usuário que mais ouviu músicas"""
        if not usuarios:
            return None
        return max(usuarios, key=lambda u: len(u.historico))

    @staticmethod
    def media_avaliacoes(musicas: list[Musica]) -> dict[str, float]:
        """Retorna a média de avaliações de cada música"""
        medias = {}
        for musica in musicas:
            if musica.avaliacoes:  # só calcula se houver avaliações
                medias[musica.titulo] = sum(musica.avaliacoes) / len(musica.avaliacoes)
            else:
                medias[musica.titulo] = 0.0
        return medias

    @staticmethod
    def total_reproducoes(usuarios: list[Usuario]) -> int:
        """Retorna o total de reproduções feitas por todos os usuários"""
        return sum(len(u.historico) for u in usuarios)