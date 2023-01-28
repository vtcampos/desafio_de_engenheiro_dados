O Desafio foi solucionado parcialmente em um container Docker
A ideia era de baixas os arquivos .dbc converter para .csv e carregar em banco local postgres

A solução é estruturada nos seguintes passos:
1. Roda o download_format_aqruivos_ans.py para baixar e salvar os arquivos
2. Dentro do script anterior é chamado um script em R que converte os dados de .dbc para .csv
3. Roda o load_postgre_table.py que concatena todas as tabelas salvas em .csv e carrega no postgre

No entanto, não foi possível rodar os script R, que converte os arquivos, no container e então a solução não 
executa a estrutura desejada

Os pontos seguintes de tratar os dados com dbt e fazer a consulta também não foram satisfeitos