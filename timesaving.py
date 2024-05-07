import datetime

# Função para obter a data e a hora atuais
def get_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Função para registrar a data e hora em um arquivo de log
def log_datetime(date_time):
    with open("log.txt", "a") as file:
        file.write(date_time + "\n")

# Função para ler e retornar o conteúdo do log
def read_log():
    try:
        with open("log.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Arquivo de log não encontrado."

def main():
    # Obter a data e a hora atuais
    current_date_time = get_current_datetime()

    # Registrar a data e a hora no log
    log_datetime(current_date_time)

    # Retornar o conteúdo do log
    print("Log:")
    print(read_log())

if __name__ == "__main__":
    main()
