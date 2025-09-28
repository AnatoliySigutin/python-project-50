import json

def load_json(filename):
    """Загружает JSON-файл и возвращает словарь."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def generate_diff(file1, file2):
    """Генерирует отчёт о различиях между двумя JSON-файлами."""
    data1 = load_json(file1)
    data2 = load_json(file2)

    # Определяем все ключи
    all_keys = set(data1.keys()) | set(data2.keys())

    results = []

    for key in sorted(all_keys):
        val1 = data1.get(key)
        val2 = data2.get(key)

        if val1 != val2:
            if val1 is None:
                results.append(f"+ {key}: {val2}")
            elif val2 is None:
                results.append(f"- {key}: {val1}")
            else:
                results.append(f"- {key}: {val1}\n+ {key}: {val2}")
        else:
            # Если ключ общий и значения совпадают, добавляем его в результат
            results.append(f"  {key}: {val1}")

    output = "{}\n{}\n{}".format("{", "\n".join(results), "}")
    return output



