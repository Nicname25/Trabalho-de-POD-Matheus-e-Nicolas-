from Streaming.arquivo_de_midia import ArquivoDeMidia


class Playlist:
    def __init__(self, nome: str, usuario):
        self.nome = nome
        self.usuario = usuario
        self.itens: list[ArquivoDeMidia] = []
        self.reproducoes = 0

    def adicionar_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        if midia in self.itens:
            self.itens.remove(midia)

    def reproduzir(self, usuario_que_ouve=None):
        """Reproduz todas as mídias na playlist e registra no histórico do usuário"""
        for midia in self.itens:
            midia.reproduzir()
            if usuario_que_ouve:
                usuario_que_ouve.historico.append(midia)
        self.reproducoes += 1

    def __add__(self, outra):
        """Concatenar duas playlists em uma nova playlist com nome da primeira"""
        nova = Playlist(self.nome, self.usuario)
        nova.itens = self.itens + outra.itens
        nova.reproducoes = self.reproducoes + outra.reproducoes
        return nova

    def __len__(self):
        return len(self.itens)

    def __getitem__(self, indice: int):
        return self.itens[indice]

    def __eq__(self, outra):
        return (
            self.nome == outra.nome and
            self.usuario == outra.usuario and
            [m.titulo for m in self.itens] == [m.titulo for m in outra.itens]
        )

    def __str__(self):
        return f"Playlist: {self.nome} | Criada por {self.usuario.nome} | {len(self.itens)} itens | {self.reproducoes} reproduções"

    def __repr__(self):
        return f"Playlist(nome={self.nome}, usuario={self.usuario.nome}, itens={len(self.itens)})"