import json

# Функция для загрузки JSON
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка загрузки '{file_path}': файл не найден.")
        exit(1)
    except json.JSONDecodeError as err:
        print(f"Ошибка загрузки '{file_path}': неверный формат JSON ({err}).")
        exit(1)

# Основная логика программы
def compare_files(file1, file2):
    # Загружаем файлы
    data1 = load_json(file1)
    data2 = load_json(file2)

    # Простое сравнение ключей и значений
    for key in set(data1.keys()) | set(data2.keys()):
        val1 = data1.get(key)
        val2 = data2.get(key)
        if val1 != val2:
            print(f"{key}: {val1 or '<отсутствует>'} → {val2 or '<отсутствует>'}")