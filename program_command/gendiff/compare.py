from program_command.type_mapper import JsonDict
from program_command.gendiff.parser import load_json_or_yaml
from program_command.gendiff.generate_builder import build_diff
from program_command.gendiff.formatters.stylish import format_stylish
from program_command.gendiff.formatters.plain import format_plain




def generate_diff(file_left: str, file_right: str, format_name = "stylish"):
    data1 = load_json_or_yaml(file_left)
    data2 = load_json_or_yaml(file_right)
    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
    else:
        return format_stylish(diff_tree)
    