from Streaming.usuario import Usuario
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.menu_usuario import MenuUsuario

from pathlib import Path
import os
import re


class Menu:
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.playlists: list[Playlist] = []
        self.musicas: list[Musica] = []
        self.podcasts: list[Podcast] = []
        self._playlists_pendentes = []  # usado para popular depois
        os.makedirs(Path.cwd() / "logs", exist_ok=True)
        os.makedirs(Path.cwd() / "relatorios", exist_ok=True)
        self.carregar_config()

    # ---------- UTILITÁRIOS ----------
    def log_erro(self, mensagem: str):
        caminho = Path.cwd() / "logs" / "erros.log"
        with open(caminho, "a", encoding="utf-8") as arq:
            arq.write(mensagem + "\n")

    def _find_config_md(self) -> list[Path]:
        possiveis = [
            Path.cwd() / "config",
            Path(__file__).parent / "config",
            Path(__file__).resolve().parents[1] / "config"
        ]
        arquivos = []
        for d in possiveis:
            if d.exists() and d.is_dir():
                arquivos.extend(sorted(d.glob("*.md")))
        return arquivos

    # ---------- CARREGAMENTO ----------
    def carregar_config(self):
        arquivos = self._find_config_md()
        if not arquivos:
            print("Nenhum arquivo .md encontrado.")
            return

        for arq in arquivos:
            try:
                texto = arq.read_text(encoding="utf-8")
            except Exception as e:
                self.log_erro(f"Falha ao abrir {arq}: {e}")
                continue

            secoes = re.split(r"(?m)^#\s*", texto)
            for sec in secoes:
                sec = sec.strip()
                if not sec:
                    continue
                linhas = [l.rstrip() for l in sec.splitlines() if l.strip()]
                titulo = linhas[0].lower()
                conteudo = linhas[1:]
                blocos = self._extrair_blocos(conteudo)

                if "usu" in titulo:
                    for b in blocos:
                        self._process_usuario(b, arq)
                elif "mús" in titulo or "mus" in titulo:
                    for b in blocos:
                        self._process_musica(b, arq)
                elif "podcast" in titulo:
                    for b in blocos:
                        self._process_podcast(b, arq)
                elif "playlist" in titulo: 
                    for b in blocos: 
                        self._process_playlist(b, arq)

        # agora preenche as playlists pendentes (itens)
        self._preencher_playlists()

        print("\nConfiguração carregada com sucesso!")
        print(f"Usuários carregados: {[u.nome for u in self.usuarios]}")
        print(f"Músicas carregadas: {[m.titulo for m in self.musicas]}")
        print(f"Podcasts carregados: {[p.titulo for p in self.podcasts]}")
        print(f"Playlists carregadas: {[p.nome for p in self.playlists]}")

    # ---------- PARSER ----------
    def _extrair_blocos(self, linhas):
        blocos = []
        bloco = {}
        for linha in linhas:
            s = linha.strip()
            if s.startswith("- "):
                if bloco:
                    blocos.append(bloco)
                    bloco = {}
                s = s[2:]
            if ":" in s:
                chave, valor = s.split(":", 1)
                chave = chave.strip()
                valor = valor.strip()
                if valor.startswith("[") and valor.endswith("]"):
                    valor = [v.strip() for v in valor[1:-1].split(",") if v.strip()]
                bloco[chave] = valor
        if bloco:
            blocos.append(bloco)
        return blocos

    # ---------- PROCESSADORES ----------
    def _process_usuario(self, dados, arq):
        nome = str(dados.get("nome") or "").strip()
        #print(nome)
        if not nome:
            self.log_erro(f"{arq}: Usuário sem nome -> {dados}")
            return
        if any(u.nome == nome for u in self.usuarios):
            #print("JAbuti")
            return  # evita duplicata
        #4print("Arara")
        self.usuarios.append(Usuario(nome))

    def _process_musica(self, dados, arq):
        titulo = str(dados.get("titulo") or "").strip()
        artista = str(dados.get("artista") or "").strip()
        genero = str(dados.get("genero") or "Desconhecido").strip()
        duracao = int(dados.get("duracao") or 0)
        if not titulo:
            return
        self.musicas.append(Musica(titulo, duracao, artista, genero))

    def _process_podcast(self, dados, arq):
        try:
            titulo = str(dados.get("titulo") or "").strip()
            artista = str(dados.get("artista") or "").strip()
            duracao = int(dados.get("duracao") or 0)
            episodio = int(dados.get("episodio") or 0)
            temporada_str = str(dados.get("temporada") or "1").strip()
            temporada = int(temporada_str) if temporada_str.isdigit() else 1
            host = str(dados.get("host") or artista).strip()

            if not titulo:
                return
            self.podcasts.append(Podcast(titulo, duracao, artista, episodio, temporada, host))

        except Exception as e:
            self.log_erro(f"{arq}: erro ao processar podcast {dados} -> {e}")

    def _process_playlist(self, dados, arq):
        
        nome = str(dados.get("nome") or "").strip()
        usuario_nome = str(dados.get("usuario") or "").strip()
        itens = dados.get("itens", [])
        if isinstance(itens, str):
            itens = [i.strip() for i in itens.split(",") if i.strip()]
        self._playlists_pendentes.append((nome, usuario_nome, itens))

    def _preencher_playlists(self):
        for nome, usuario_nome, itens in self._playlists_pendentes:
            usuario = next((u for u in self.usuarios if u.nome == usuario_nome), None)
            if not usuario:
                self.log_erro(f"Usuário '{usuario_nome}' não encontrado para playlist '{nome}'")
                continue
            pl = Playlist(nome, usuario)
            for item_nome in itens:
                midia = next((m for m in self.musicas if m.titulo == item_nome), None)
                if not midia:
                    midia = next((p for p in self.podcasts if p.titulo == item_nome), None)
                if midia:
                    pl.adicionar_midia(midia)
                else:
                    self.log_erro(f"Item '{item_nome}' não encontrado para playlist '{nome}'")
            usuario.playlists.append(pl)
            self.playlists.append(pl)

    # ---------- MENUS ----------
    def menu_principal(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1 - Entrar como usuário")
            print("2 - Criar novo usuário")
            print("3 - Listar usuários")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ").strip()
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
        nome = input("Digite o nome do novo usuário: ").strip()
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
                MenuUsuario(usuario, self.musicas, self.podcasts, self.playlists).menu_principal()
            else:
                print("Usuário inválido!")
        except ValueError:
            print("Entrada inválida!")