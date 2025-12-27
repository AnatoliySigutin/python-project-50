def format_plain(diff_tree):
    def format_value(value):
        if value is None:
            return 'null'
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, (dict, list)):
            return '[complex value]'
        elif isinstance(value, str):
            return f"'{value}'"
        else:
            return str(value)

    lines = []

    def recurse(node, path=''):
        for key, value in node.items():
            property_path = f"{path}.{key}" if path else key
            status = value['status']
            
            if status == 'nested':
                recurse(value['children'], property_path)
            elif status == 'removed':
                lines.append(f"Property '{property_path}' was removed")
            elif status == 'added':
                # Используем 'value' вместо 'new_value'
                val_repr = format_value(value.get('value'))
                lines.append(f"Property '{property_path}' was added with value: {val_repr}")
            elif status == 'updated':
                old_val_repr = format_value(value.get('old_value'))
                new_val_repr = format_value(value.get('new_value'))
                lines.append(
                    f"Property '{property_path}' was updated. From {old_val_repr} to {new_val_repr}"
                )
            # 'unchanged' игнорируем в plain формате

    recurse(diff_tree)
    return '\n'.join(lines)