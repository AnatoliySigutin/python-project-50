import argparse
from program_command.gendiff.compare import compare_files

# Основной поток исполнения программы
def main():
    # Парсер аргументов
    parser = argparse.ArgumentParser(description="Программа для сравнения двух JSON-файлов.")
    parser.add_argument("file1", type=str)
    parser.add_argument("file2", type=str)

    # Анализируем аргументы
    args = parser.parse_args()

    # Вызываем основную логику
    compare_files(args.file1, args.file2)

if __name__ == "__main__":
    main()