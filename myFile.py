import random
import datetime
import csv
import time

# Função para gerar o nome fictício
def gerar_nome():
    nomes = ["Ana", "João", "Maria", "Carlos", "Lucas", "Fernanda", "Rafael", "Júlia", "Pedro", "Gabriela"]
    return random.choice(nomes)

# Função para gerar o número aleatório
def gerar_numero():
    return random.randint(1, 100)

# Lista para armazenar as linhas criadas
linhas = []

# Gerando as 100 linhas
for _ in range(100):
    nome = gerar_nome()
    numero = gerar_numero()
    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = [nome, numero, horario]
    linhas.append(linha)
    time.sleep(1)

# Caminho do arquivo CSV
arquivo_csv = 'dados.csv'

# Escrevendo os dados no arquivo CSV
with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Número", "Horário"])  # Cabeçalho
    writer.writerows(linhas)  # Escreve todas as linhas

print(f"Arquivo CSV '{arquivo_csv}' criado com sucesso!")