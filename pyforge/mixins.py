from pyforge.decorators import partial, works_with_module_dict

def gather_list(module, list_name, where_to_mixin):
    if hasattr(module, list_name):
        gathered = getattr(module, list_name)
        where_to_mixin[list_name] += gathered
        
@partial(works_with_module_dict, (0, 'module_dict'))
def get_objects_names(module_dict, types, include_private=False):
    return [
        list_name 
        for list_name in module_dict.keys()
        if (
            isinstance(module_dict[list_name], types) and
            (include_private or list_name[0:1] != '_') and
            list_name[0:2] != '__'
        )
    ]
         
def import_module(module_name):
    # 3to2 fix
    # added bytes(), so it would translate to str()
    return __import__(module_name, fromlist=[bytes(module_name)])
    
import_cache = {}

def eval_with_import(dotted_value, use_cache=True):
    parts = dotted_value.split('.')
    value_module_name = '.'.join(parts[:-1])
    value_name = parts[-1]
    
    if not use_cache or value_module_name not in import_cache:
        import_cache[value_module_name] = import_module(value_module_name)
        
    return getattr(import_cache[value_module_name], value_name)       