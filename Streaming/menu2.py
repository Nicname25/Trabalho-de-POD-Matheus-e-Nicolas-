from Streaming.usuario import Usuario
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast


class Menu2:
    def menu_principal(self):
        while True:
            print("1 - Reproduzir uma música")
            print("2 - Listar músicas")
            print("3 - Listar podcasts")
            print("4 - Listar playlists")
            print("5 - Reproduzir uma playlist")
            print("6 - Criar nova playlist")
            print("7 - Concatenar playlists")
            print("8 - Gerar relatório")
            print("9 - Sair")
            opcao_usuario = input("Escolha uma opção: ")
            if opcao_usuario == "1":
                self.reproduzir_musica()
            elif opcao_usuario == "2":
                self.listar_musicas()
            elif opcao_usuario == "3":
                self.listar_podcasts()
            elif opcao_usuario == "4":
                self.listar_playlists()
            elif opcao_usuario == "5":
                self.reproduzir_playlist()
            elif opcao_usuario == "6":
                self.criar_playlist()
            elif opcao_usuario == "7":
                self.concatenar_playlists()
            elif opcao_usuario == "8":
                self.gerar_relatorio()
            elif opcao_usuario == "9":
                break
            else:
                    print("Opção inválida")