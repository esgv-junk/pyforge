def gather_list(module, list_name, where_to_mixin):
    if hasattr(module, list_name):
        gathered = getattr(module, list_name)
        where_to_mixin[list_name] += gathered