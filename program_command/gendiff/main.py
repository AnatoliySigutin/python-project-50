import argparse

def gendiff_h():
    # Создаем объект парсера
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    
    # Позиционные аргументы (обязательные)
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
   

    
    # Опция помощи (-h, --help) добавляется автоматически
    
    # Парсим аргументы
    args = parser.parse_args()
    
    # Тут идёт логика обработки аргументов и собственно сама разница между файлами
    print(f"Processing comparison between '{args.first_file}' and '{args.second_file}'.")

