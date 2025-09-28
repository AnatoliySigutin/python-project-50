import argparse
from program_command.gendiff.compare import generate_diff

# Основной поток исполнения программы
def main():
    # Парсер аргументов
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')

    # Анализируем аргументы
    args = parser.parse_args()

    # Если достигнут этот момент, значит, не было запроса справки
    # Значит, можно запускать сравнение
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == "__main__":
    main()