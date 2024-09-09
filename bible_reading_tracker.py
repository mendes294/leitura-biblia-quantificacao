import csv
from datetime import datetime

# Nome do arquivo CSV onde os dados serão armazenados
FILENAME = 'bible_reading_log.csv'

def log_reading(pages_read):
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Abre o arquivo CSV e adiciona uma nova linha com a data e as páginas lidas
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, pages_read])

def view_log():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Data: {row[0]}, Páginas Lidas: {row[1]}")
    except FileNotFoundError:
        print("O arquivo de log não existe. Comece a registrar suas leituras.")

def main():
    print("Bem-vindo ao Rastreador de Leitura da Bíblia")
    print("1. Registrar leitura")
    print("2. Ver log de leitura")
    choice = input("Escolha uma opção (1 ou 2): ")
    
    if choice == '1':
        pages = input("Quantas páginas você leu hoje? ")
        try:
            pages = int(pages)
            log_reading(pages)
            print("Leitura registrada com sucesso!")
        except ValueError:
            print("Por favor, insira um número válido de páginas.")
    elif choice == '2':
        view_log()
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    main()
git init
git add bible_reading_tracker.py
git commit -m "Commit inicial com o script de rastreamento de leitura da Bíblia"


