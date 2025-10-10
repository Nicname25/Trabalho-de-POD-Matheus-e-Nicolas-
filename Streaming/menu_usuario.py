from Streaming.usuario import Usuario
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.analises import Analises


class MenuUsuario:
    def __init__(self, usuario: Usuario, musicas: list[Musica], podcasts: list[Podcast], playlists: list[Playlist], usuarios: list[Usuario]):
        self.usuario = usuario
        self.musicas = musicas
        self.podcasts = podcasts
        self.playlists = playlists
        self.usuarios = usuarios

    def menu_principal(self):
        while True:
            print(f"\n=== MENU DO USUÁRIO: {self.usuario.nome} ===")
            print("1 - Reproduzir uma música")
            print("2 - Listar músicas")
            print("3 - Listar podcasts")
            print("4 - Listar playlists")
            print("5 - Reproduzir uma playlist")
            print("6 - Criar nova playlist")
            print("7 - Concatenar playlists")
            print("8 - Gerar relatório")
            print("9 - Ver histórico detalhado")
            print("10 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.reproduzir_musica()
            elif opcao == "2":
                self.listar_musicas()
            elif opcao == "3":
                self.listar_podcasts()
            elif opcao == "4":
                self.listar_playlists()
            elif opcao == "5":
                self.reproduzir_playlist()
            elif opcao == "6":
                self.criar_playlist()
            elif opcao == "7":
                self.concatenar_playlists()
            elif opcao == "8":
                Analises.gerar_relatorio(self.musicas, self.playlists, self.usuarios)
            elif opcao == "9":
                self.usuario.gerar_relatorio_pessoal()
            elif opcao == "10":
                break
            else:
                print("Opção inválida!")

    # ===== Métodos de interface (apenas chamam as classes) =====
    def reproduzir_musica(self):
        self.listar_musicas()
        nome = input("Digite o título da música: ")
        for m in self.musicas:
            if m.titulo == nome:
                self.usuario.ouvir_midia(m) 
                return
        print("Música não encontrada!")

    def listar_musicas(self):
        print("\n=== Músicas Disponíveis ===")
        for m in self.musicas:
            print("-", m)

    def listar_podcasts(self):
        print("\n=== Podcasts Disponíveis ===")
        for p in self.podcasts:
            print("-", p)

    def reproduzir_podcast(self):
        if not self.podcasts:
            print("Nenhum podcast disponível.")
            return

        print("\n=== Lista de Podcasts ===")
        for i, p in enumerate(self.podcasts, start=1):
            print(f"{i}. {p.titulo} - {p.artista}")

        try:
            escolha = int(input("Escolha o número do podcast: ")) - 1
            if 0 <= escolha < len(self.podcasts):
                podcast = self.podcasts[escolha]
                print(f"\nReproduzindo podcast: {podcast.titulo} - {podcast.artista}")
                podcast.reproduzir()
                self.usuario.historico.append(podcast)
            else:
                print("Podcast inválido.")
        except ValueError:
            print("Entrada inválida.")

    def listar_playlists(self):
        print("\n=== Playlists ===")
        for pl in self.playlists:
            print("-", pl)

    def reproduzir_playlist(self):
        self.listar_playlists()
        nome = input("Digite o nome da playlist: ")
        for pl in self.playlists:
            if pl.nome == nome:
                pl.reproduzir(usuario_que_ouve=self.usuario)
                print(f"\nPlaylist '{pl.nome}' reproduzida por {self.usuario.nome}!")
                return
        print("Playlist não encontrada!")

    def criar_playlist(self):
        nome = input("Digite o nome da nova playlist: ")
        try:
            nova = self.usuario.criar_playlist(nome) 
            self.playlists.append(nova)
            print(f"Playlist '{nome}' criada com sucesso!")
        except ValueError as e:
            print(f"{e}")

    def concatenar_playlists(self):
        self.listar_playlists()
        p1 = input("Digite o nome da primeira playlist: ")
        p2 = input("Digite o nome da segunda playlist: ")

        pl1 = next((pl for pl in self.playlists if pl.nome == p1), None)
        pl2 = next((pl for pl in self.playlists if pl.nome == p2), None)

        if pl1 and pl2:
            nova = pl1 + pl2 
            self.playlists.append(nova)
            print(f"Nova playlist criada: {nova.nome}")
        else:
            print("Uma das playlists não existe!")

    