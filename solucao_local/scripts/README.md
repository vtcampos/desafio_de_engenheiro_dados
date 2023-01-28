O Desafio foi solucionado parcialmente de forma local
Os arquivos .dbc foram baixados, convertidos para .csv e carregados em banco local postgres

A solução é estrutura nos seguintes passos:
1. Roda o download_format_aqruivos_ans.py para baixar e salvar os arquivos
2. Dentro do script anterior é chamado um script em R que converte os dados de .dbc para .csv
3. Roda o load_postgre_table.py que concatena todas as tabelas salvas em .csv e carrega no postgre

Os pontos de tratar os dados com dbt e fazer a consulta não foram satisfeito, já que não foi possível instalar o 
dbt-postgres de forma local(problema particular da minha máquina) e então foi tentada uma solução via docker para 
satisfazer todos os pontos do desafio.