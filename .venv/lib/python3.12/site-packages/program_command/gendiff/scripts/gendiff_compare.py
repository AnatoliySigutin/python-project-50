import argparse
from program_command.gendiff.compare import generate_diff

def main():
    # Парсер аргументов
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f", "--format", 
        metavar="FORMAT", 
        default="stylish",    # Значение по умолчанию
        choices=["stylish", "plain", "json"],  # Варианты форматов
        help="set format of output (default: stylish)"
    )

    # Анализируем аргументы
    args = parser.parse_args()

    # Передаем выбранный формат в generate_diff
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)

if __name__ == "__main__":
    main()
