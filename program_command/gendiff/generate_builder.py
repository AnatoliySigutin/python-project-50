# program_command/gendiff/diff_builder.py

def build_diff(left, right):
    """
    Строит дерево различий между двумя словарями
    """
    diff = {}
    all_keys = sorted(set(left.keys()) | set(right.keys()))
    
    for key in all_keys:
        val1 = left.get(key)
        val2 = right.get(key)
        
        if key not in right:
            diff[key] = {'status': 'removed', 'value': val1}
        elif key not in left:
            diff[key] = {'status': 'added', 'value': val2}
        elif isinstance(val1, dict) and isinstance(val2, dict):
            diff[key] = {'status': 'nested', 'children': build_diff(val1, val2)}
        elif val1 != val2:
            diff[key] = {
                'status': 'updated', 
                'old_value': val1, 
                'new_value': val2
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': val1}
            
    return diff