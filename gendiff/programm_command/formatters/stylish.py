# program_command/gendiff/formatters/stylish.py


def format_stylish(diff_tree):
    """
    Форматирует дерево различий в стиле stylish
    """

    def format_diff(diff, depth=1):
        lines = []
        indent = "  " * depth
        for key, node in diff.items():
            status = node["status"]

            if status == "nested":
                lines.append(f"{indent}  {key}: {{")
                lines.extend(format_diff(node["children"], depth + 2))
                lines.append(f"{indent}  }}")

            elif status == "removed":
                value = format_value(node["value"], depth + 2)
                lines.append(f"{indent}- {key}: {value}")

            elif status == "added":
                value = format_value(node["value"], depth + 2)
                lines.append(f"{indent}+ {key}: {value}")

            elif status == "updated":
                old_value = format_value(node["old_value"], depth + 2)
                new_value = format_value(node["new_value"], depth + 2)
                lines.append(f"{indent}- {key}: {old_value}")
                lines.append(f"{indent}+ {key}: {new_value}")

            elif status == "unchanged":
                value = format_value(node["value"], depth + 2)
                lines.append(f"{indent}  {key}: {value}")

        return lines

    def format_value(value, depth):
        if isinstance(value, dict):
            indent = "  " * depth
            lines = ["{"]
            for k, v in sorted(value.items()):
                formatted_v = format_value(v, depth + 2)
                lines.append(f"{indent}  {k}: {formatted_v}")
            lines.append("  " * (depth - 1) + "}")
            return "\n".join(lines)
        elif value is None:
            return "null"
        elif isinstance(value, bool):
            return str(value).lower()
        else:
            return str(value)

    # Собираем результат
    result_lines = ["{"]
    result_lines.extend(format_diff(diff_tree))
    result_lines.append("}")

    return "\n".join(result_lines)
