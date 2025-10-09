Este projeto implementa um sistema de streaming de músicas e podcasts, com foco em orientação a objetos, herança, composição e polimorfismo.

O sistema permite criar usuários, playlists e reproduzir mídias (músicas e podcasts).
Todas as informações de inicialização (usuários, playlists e mídias) são carregadas automaticamente a partir de arquivos de configuração Markdown (.md).

Além disso, o sistema gera relatórios e análises automáticas sobre o uso da plataforma, contabilizando reproduções, usuários mais ativos e estatísticas personalizadas.

Histórico Detalhado do Usuário:
Mostra todas as músicas e podcasts ouvidos, tempo total reproduzido, número de playlists ouvidas e total de mídias.

Contabilização de Playlists de Outros Usuários:
Agora o histórico registra corretamente quando o usuário ouve playlists criadas por outras pessoas.

Análise de Dados:
Classe Analises gera estatísticas como:

Top músicas mais reproduzidas

Playlist mais popular

Usuário mais ativo

Média de avaliações

Total de reproduções do sistema

Relatórios Automatizados:
Todos os dados são exportados para arquivos .txt dentro da pasta relatorios/.

Sistema de Logs:
Qualquer erro de leitura de arquivo ou dado inconsistente é registrado em logs/erros.log.

Os arquivos .md dentro da pasta Streaming/config/ inicializam o sistema automaticamente.  
