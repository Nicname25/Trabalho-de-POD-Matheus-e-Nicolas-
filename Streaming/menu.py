from Streaming.usuario import Usuario
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.menu2 import Menu2

from pathlib import Path
import os


class Menu:
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.playlists: list[Playlist] = []
        self.musicas: list[Musica] = []
        self.podcasts: list[Podcast] = []

        self.carregar_config()

    def log_erro(self, mensagem: str):
        os.makedirs("logs", exist_ok=True)
        with open("logs/erros.log", "a", encoding="utf-8") as arq:
            arq.write(mensagem + "\n")

    def carregar_config(self):
        """Carrega usuários, músicas, podcasts e playlists do arquivo Markdown"""
        caminho = Path("config/dados.md")
        if not caminho.exists():
            print("Arquivo config/dados.md não encontrado!")
            return

        with open(caminho, "r", encoding="utf-8") as arq:
            linhas = [l.strip() for l in arq if l.strip()]

        secao = None
        bloco = {}

        def salvar_bloco(secao, dados):
            try:
                if secao == "usuários":
                    nome = dados.get("nome")
                    if any(u.nome == nome for u in self.usuarios):
                        self.log_erro(f"Usuário duplicado: {nome}")
                        return
                    self.usuarios.append(Usuario(nome))

                elif secao == "músicas":
                    dur = int(dados.get("duracao", 0))
                    if dur <= 0:
                        self.log_erro(f"Duração inválida para música: {dados}")
                        return
                    self.musicas.append(Musica(
                        dados.get("titulo"),
                        dur,
                        dados.get("artista"),
                        dados.get("genero", "Desconhecido")
                    ))

                elif secao == "podcasts":
                    try:
                        ep = int(dados.get("episodio"))
                    except:
                        self.log_erro(f"Episódio inválido: {dados}")
                        return
                    dur = int(dados.get("duracao", 0))
                    if dur <= 0:
                        self.log_erro(f"Duração inválida: {dados}")
                        return
                    self.podcasts.append(Podcast(
                        dados.get("titulo"),
                        dur,
                        dados.get("host", "Desconhecido"),
                        ep,
                        dados.get("temporada", "Desconhecida"),
                        dados.get("host", "Desconhecido")
                    ))

                elif secao == "playlists":
                    nome = dados.get("nome")
                    usuario_nome = dados.get("usuario")
                    itens = [x.strip() for x in dados.get("itens", "").split(",")]
                    usuario = next((u for u in self.usuarios if u.nome == usuario_nome), None)
                    if not usuario:
                        self.log_erro(f"Usuário {usuario_nome} não encontrado para playlist {nome}")
                        return
                    playlist = Playlist(nome, usuario)
                    for item in itens:
                        midia = next((m for m in self.musicas if m.titulo == item), None)
                        if not midia:
                            midia = next((p for p in self.podcasts if p.titulo == item), None)
                        if midia:
                            playlist.adicionar_item(midia)
                        else:
                            self.log_erro(f"Mídia '{item}' não encontrada em {nome}")
                    self.playlists.append(playlist)

            except Exception as e:
                self.log_erro(f"Erro ao processar {secao}: {e}")

        for linha in linhas:
            if linha.startswith("#"):
                secao = linha.replace("#", "").strip().lower()
            elif linha.startswith("- "):
                if bloco:
                    salvar_bloco(secao, bloco)
                    bloco = {}
            elif ":" in linha:
                chave, valor = linha.split(":", 1)
                bloco[chave.strip()] = valor.strip()
        if bloco:
            salvar_bloco(secao, bloco)

        print("Configuração carregada com sucesso!")

    # --- MENU PRINCIPAL ---
    def menu_principal(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1 - Entrar como usuário")
            print("2 - Criar novo usuário")
            print("3 - Listar usuários")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.entrar_usuario()
            elif opcao == "2":
                self.criar_usuario()
            elif opcao == "3":
                self.listar_usuarios()
            elif opcao == "4":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")

    def criar_usuario(self):
        nome = input("Digite o nome do novo usuário: ")
        if any(u.nome == nome for u in self.usuarios):
            print("Usuário já existe!")
            return
        novo = Usuario(nome)
        self.usuarios.append(novo)
        print(f"Usuário '{nome}' criado com sucesso!")

    def listar_usuarios(self):
        print("\n=== Lista de Usuários ===")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for i, u in enumerate(self.usuarios, start=1):
                print(f"{i}. {u.nome}")

    def entrar_usuario(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado!")
            return
        self.listar_usuarios()
        try:
            escolha = int(input("Escolha o número do usuário: ")) - 1
            if 0 <= escolha < len(self.usuarios):
                usuario = self.usuarios[escolha]
                print(f"\nBem-vindo, {usuario.nome}!")
                Menu2(usuario, self.musicas, self.podcasts, self.playlists).menu_principal()
            else:
                print("Usuário inválido!")
        except ValueError:
            print("Entrada inválida!")