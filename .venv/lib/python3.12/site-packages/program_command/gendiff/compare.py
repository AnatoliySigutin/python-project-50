from program_command.type_mapper import JsonDict
from program_command.gendiff.parser import load_json_or_yaml
from program_command.gendiff.generate_builder import build_diff
from program_command.gendiff.formatters.stylish import format_stylish

def generate_diff(file_left: JsonDict, file_right: JsonDict):
    """
    Основная функция генерации различий
    """
    # Загрузка данных
    data1 = load_json_or_yaml(file_left)
    data2 = load_json_or_yaml(file_right)
    
    # Построение дерева различий
    diff_tree = build_diff(data1, data2)
    
    # Форматирование результата
    return format_stylish(diff_tree)
    