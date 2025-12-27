def format_diff(diff_tree, format_name="stylish"):
    """
    Выбирает форматтер по имени
    """
    if format_name == "stylish":
        from .stylish import format_stylish

        return format_stylish(diff_tree)
    elif format_name == "plain":
        from .stylish import format_plain

        return format_plain(diff_tree)
    else:
        raise ValueError(f"Unknown format: {format_name}")
