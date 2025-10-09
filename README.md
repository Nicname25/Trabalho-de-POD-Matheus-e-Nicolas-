Este projeto implementa um sistema de streaming de músicas e podcasts, inspirado no Spotfy.

O sistema permite criar usuários, playlists, reproduzir mídias (músicas e podcasts) e acompanhar estatísticas de reprodução.

Todas as informações de inicialização (usuários, playlists e mídias) são carregadas automaticamente a partir de arquivos markdown (Exemplo de Entrada 1 e 2).

O sistema possui um menu completo que carrega esses arquivos markdown e depois inicializa com o menu principal. Após o usuário entrar na sua conta será aberto o menu do usuario que terá mais opções. 

O sistema gera relatórios e análises automáticas sobre o uso da plataforma, contabilizando reproduções, usuários mais ativos e estatísticas personalizadas.

Análise de Dados: Na classe Analises tem métodos como Top músicas mais reproduzidas, playlist mais popular, usuário mais ativo, Média de avaliações, Total de reproduções do sistema.

Relatórios Automatizados: Todos os dados são exportados em um arquivo relatorio.txt dentro da pasta relatorios/.

Sistema de Logs: Qualquer erro na leitura do arquivo markdown ou dado inconsistente é registrado em logs/erros.log.

Histórico do Usuário: Mostra todas as músicas e podcasts ouvidos, tempo total reproduzido, número de playlists ouvidas e total de mídias.
