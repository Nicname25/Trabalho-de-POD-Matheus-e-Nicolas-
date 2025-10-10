from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist

class Usuario:
    qntd_instancias = 0 
    def __init__(self, nome: str):
        self.nome = nome
        self.playlists: list[Playlist] = []
        self.historico: list[ArquivoDeMidia] = []
        Usuario.qntd_instancias += 1
        self.playlists_ouvidas: list[str] = []

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
    
    """
    Extra!!
    Essa é a inovação do nosso código, ela gera um relatório pessoal de cada usuário, que só pode ser acessado pelo próprio
    Ele retorna  o tempo das musicas que foram reproduzidas
    retorna as músicas e os podcasts que foram reproduzidos e quantas vezes foram reproduzidas
    A quantidade de playulists tocadas
    """
    def gerar_relatorio_pessoal(self):
        print(f"\n=== Relatório Pessoal de {self.nome} ===")

        if not self.historico:
            print("Nenhuma mídia foi reproduzida ainda.")
            return
        contagem = {}
        tempo_total = 0
        total_musicas = 0
        total_podcasts = 0

        for midia in self.historico:
            contagem[midia.titulo] = contagem.get(midia.titulo, 0) + 1
            tempo_total += midia.duracao

            from Streaming.musica import Musica
            from Streaming.podcast import Podcast
            if isinstance(midia, Musica):
                total_musicas += 1
            elif isinstance(midia, Podcast):
                total_podcasts += 1

        print("\nHistórico de reprodução:")
        for titulo, qtd in contagem.items():
            print(f" - {titulo} → {qtd} reprodução(ões)")

        minutos = tempo_total // 60
        segundos = tempo_total % 60

        total_playlists = sum(1 for p in self.playlists if p.reproducoes > 0)

        print(f"\nTempo total de áudio reproduzido: {minutos}m {segundos}s")
        print(f"Total de mídias ouvidas: {len(self.historico)}")
        print(f" ├─ Músicas: {total_musicas}")
        print(f" ├─ Podcasts: {total_podcasts}")

    def __str__(self):
        return f"Usuário: {self.nome} | Playlists: {len(self.playlists)} | Histórico: {len(self.historico)} músicas"

    def __repr__(self):
        return f"Usuario(nome={self.nome})"

