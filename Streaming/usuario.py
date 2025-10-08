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
        for pl in self.playlists:
            if pl.nome == nome:
                raise ValueError("Já existe uma playlist com esse nome para este usuário.")
        nova = Playlist(nome, self)
        self.playlists.append(nova)
        return nova
    
    # EXTRA
    def gerar_relatorio_pessoal(self):
        print(f"\n=== Relatório Pessoal de {self.nome} ===")

        if not self.historico:
            print("Nenhuma mídia foi reproduzida ainda.")
            return

        # Contagem de cada mídia
        contagem = {}
        tempo_total = 0

        for midia in self.historico:
            contagem[midia.titulo] = contagem.get(midia.titulo, 0) + 1
            tempo_total += midia.duracao

        # Exibe histórico detalhado
        print("\nHistórico de reprodução:")
        for titulo, qtd in contagem.items():
            print(f" - {titulo} → {qtd} reprodução(ões)")

        minutos = tempo_total // 60
        segundos = tempo_total % 60

        # Conta quantas vieram de playlists
        total_de_playlists = sum(1 for p in self.playlists if p.reproducoes > 0)
        print(f"\nTempo total de áudio reproduzido: {minutos}m {segundos}s")
        print(f"Total de mídias ouvidas: {len(self.historico)}")
        print(f"Playlists ouvidas: {total_de_playlists}")

    def __str__(self):
        return f"Usuário: {self.nome} | Playlists: {len(self.playlists)} | Histórico: {len(self.historico)} músicas"

    def __repr__(self):
        return f"Usuario(nome={self.nome})"
