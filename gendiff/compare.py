from gendiff.formatters.json import json_format
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.generate_builder import build_diff
from gendiff.parser import load_json_or_yaml


def generate_diff(file_left: str, file_right: str, format_name="stylish"):
    data1 = load_json_or_yaml(file_left)
    data2 = load_json_or_yaml(file_right)
    diff_tree = build_diff(data1, data2)

    if format_name == "stylish":
        return format_stylish(diff_tree)
    elif format_name == "plain":
        return format_plain(diff_tree)
    elif format_name == "json":
        return json_format(diff_tree)
