from Streaming.musica import Musica
from Streaming.playlist import Playlist
from Streaming.usuario import Usuario
import os
from datetime import datetime

class Analises:
    @staticmethod
    def top_musicas_reproduzidas(musicas: list[Musica], top_n: int) -> list[Musica]:
        """ 
        Esse método retorna as 3 músicas mais reproduzidas.
        """
        if not musicas:
            return []
        return sorted(musicas, key=lambda m: m.reproducoes, reverse=True)[:top_n]

    @staticmethod
    def playlist_mais_popular(playlists: list[Playlist]) -> Playlist | None:
        """
        Esse método retorna a playlist mais reproduzida
        """
        if not playlists:
            return None
        return max(playlists, key=lambda p: p.reproducoes)

    @staticmethod
    def usuario_mais_ativo(usuarios: list[Usuario]) -> Usuario | None:
        """
        Esse método retorna o usuário que reproduziu mais minutos de músicas
        """
        if not usuarios:
            return None
        return max(usuarios, key=lambda u: len(u.historico))

    @staticmethod
    def media_avaliacoes(musicas: list[Musica]) -> dict[str, float]:
        """
        Esse método retorna a média das avaliações da música
        """
        medias = {}
        for musica in musicas:
            if musica.avaliacoes:
                medias[musica.titulo] = sum(musica.avaliacoes) / len(musica.avaliacoes)
            else:
                medias[musica.titulo] = 0.0
        return medias

    @staticmethod
    def total_reproducoes(usuarios: list[Usuario]) -> int:
        """
        Esse método retorna o total de reproduções por certo usuário
        """
        return sum(len(u.historico) for u in usuarios)



    # Novo método para gerar relatório em arquivo
    @staticmethod
    def gerar_relatorio(musicas: list[Musica], playlists: list[Playlist], usuarios: list[Usuario], top_n: int = 3):

        """
        Esse método gera o relatório de tudo que ocorreu na execução.
        incluindo:
        top músicas
        usuário mais ativo
        playlist mais popular
        média de avaliações
        """
        # Garante que a pasta existe
        os.makedirs("relatorios", exist_ok=True)

        caminho = os.path.join("relatorios", "relatorio.txt")
        with open(caminho, "w", encoding="utf-8") as arq:
            arq.write("=== RELATÓRIO DO SISTEMA DE STREAMING ===\n")
            arq.write(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")

            # Top músicas
            arq.write("Top músicas mais reproduzidas:\n")
            for m in Analises.top_musicas_reproduzidas(musicas, top_n):
                arq.write(f" - {m.titulo} ({m.artista}) | Reproduções: {m.reproducoes}\n")
            arq.write("\n")

            # Playlist mais popular
            playlist = Analises.playlist_mais_popular(playlists)
            if playlist:
                arq.write(f"Playlist mais popular: {playlist.nome} ({playlist.reproducoes} reproduções)\n\n")

            # Usuário mais ativo
            usuario = Analises.usuario_mais_ativo(usuarios)
            if usuario:
                arq.write(f"Usuário mais ativo: {usuario.nome} ({len(usuario.historico)} execuções)\n\n")

            # Médias de avaliações
            arq.write("Média de avaliações das músicas:\n")
            medias = Analises.media_avaliacoes(musicas)
            for titulo, media in medias.items():
                arq.write(f" - {titulo}: {media:.2f}\n")
            arq.write("\n")

            # Total de reproduções
            total = Analises.total_reproducoes(usuarios)
            arq.write(f"Total de reproduções no sistema: {total}\n")


        print(f"Relatório gerado em: {caminho}")
