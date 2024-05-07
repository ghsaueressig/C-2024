#include <stdio.h>
#include <time.h>

// Função para obter a data e a hora atuais
void getCurrentDateTime(char *dateTime) {
    time_t rawtime;
    struct tm *info;

    time(&rawtime);
    info = localtime(&rawtime);

    strftime(dateTime, 80, "%Y-%m-%d %H:%M:%S", info);
}

// Função para registrar a data e hora em um arquivo de log
void logDateTime(const char *dateTime) {
    FILE *file;
    file = fopen("log.txt", "a");

    if (file != NULL) {
        fprintf(file, "%s\n", dateTime);
        fclose(file);
    } else {
        printf("Erro ao abrir o arquivo de log.\n");
    }
}

int main() {
    char dateTime[80];

    // Obter a data e a hora atuais
    getCurrentDateTime(dateTime);

    // Registrar a data e a hora no log
    logDateTime(dateTime);

    // Retornar o log
    printf("Log:\n");

    FILE *file;
    file = fopen("log.txt", "r");

    if (file != NULL) {
        char c;
        while ((c = getc(file)) != EOF) {
            putchar(c);
        }
        fclose(file);
    } else {
        printf("Erro ao abrir o arquivo de log.\n");
    }

    return 0;
}
