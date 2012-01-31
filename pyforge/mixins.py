from pyforge.decorators import partial, works_with_module_dict

def gather_list(module, list_name, where_to_mixin):
    if hasattr(module, list_name):
        gathered = getattr(module, list_name)
        where_to_mixin[list_name] += gathered
        
@partial(works_with_module_dict, (0, 'module_dict'))
def get_objects_names(module_dict, types, include_private=False):
    return [
        name
        for name in module_dict.keys()
        if (
            isinstance(module_dict[name], types) and
            (include_private or name[0:1] != '_') and
            name[0:2] != '__'
        )
    ]
         
def drop_first_module(module_path, num_dropped=1):
    return '.'.join(module_path.split('.')[num_dropped:])

def drop_last_module(module_path, num_dropped=1):
    return '.'.join(module_path.split('.')[:-num_dropped])
