from pyforge.decorators import *

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
            