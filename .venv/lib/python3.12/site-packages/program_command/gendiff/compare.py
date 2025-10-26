import json
import yaml
import os

def load_json_or_yaml(filename):
    """Загружает JSON или YAML файл в зависимости от расширения."""
    ext = os.path.splitext(filename)[1].lower()
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        if not content.strip():
            raise ValueError(f"Файл {filename} пустой")
        # Возвращаем содержимое для дальнейшей обработки
        if ext in ['.json']:
            return json.loads(content)
        elif ext in ['.yml', '.yaml']:
            return yaml.safe_load(content)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")

def generate_diff(file1, file2):
    data1 = load_json_or_yaml(file1)
    data2 = load_json_or_yaml(file2)

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
            results.append(f"  {key}: {val1}")

    output = "{}\n{}\n{}".format("{", "\n".join(results), "}")
    return output