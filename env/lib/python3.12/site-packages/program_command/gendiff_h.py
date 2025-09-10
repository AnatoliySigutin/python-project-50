import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    
    # Позиционные аргументы
    parser.add_argument("first_file", help="First configuration file")
    parser.add_argument("second_file", help="Second configuration file")
    
    # Опции
    parser.add_argument("-f", "--format", default="pretty",
                        help="Output format (default: pretty)")
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Далее идет логика сравнения файлов...
    print(f"Processing {args.first_file} vs {args.second_file}")

if __name__ == "__main__":
    main()