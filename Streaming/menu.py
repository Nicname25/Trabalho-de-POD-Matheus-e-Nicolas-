from Streaming.usuario import Usuario
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.menu2 import Menu2

class Menu:
    def __init__(self):
        self.__usuarios = []
        self.__playlists = []
        self.__musicas = []
        self.__podcasts = []
        self.__historico = []

    def menu_principal(self):
        while True:
            print("1 - Entrar como usuário")
            print("2 - Criar novo usuário")
            print("3 - Listar usuários")
            print("4 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.menu_usuario()
            elif opcao == "2":
                self.criar_usuario()
                Menu2().menu_principal()
            elif opcao == "3":
                self.listar_usuarios()
            elif opcao == "4":
                break
            else:
                print("Opção inválida")

