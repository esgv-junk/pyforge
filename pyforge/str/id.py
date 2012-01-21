import re, collections
from pyforge.str.lang import transliterate

class UniqueIdDispatcher:
    def __init__(self):
        self.taken_ids = collections.defaultdict(lambda: None)
        
    def resolve_id_collision(self, id, prev_collision_info):
        raise NotImplementedError()
    
    def dispatch_id(self, desired_id):
        new_id, new_collision_info = self.resolve_id_collision(
            desired_id,
            self.taken_ids[desired_id]
        )
        
        self.taken_ids[desired_id] = new_collision_info
        return new_id
    
    def reset_id(self, desired_id):
        self.taken_ids[desired_id] = None
        
    def clear(self):
        self.taken_ids.clear()
    
class IdDispatcher(UniqueIdDispatcher):
    def resolve_id_collision(self, id, prev_collision_info):
        if prev_collision_info is None:
            return id, 1
        
        return (id + str(prev_collision_info), prev_collision_info + 1)
    
class NumberDispatcher(UniqueIdDispatcher):
    def resolve_id_collision(self, id, prev_collision_info):
        if prev_collision_info is None:
            return 1, 1
        
        return (prev_collision_info + 1,) * 2

def to_id(string):
    string = transliterate(string)
    return re.sub('[^a-zA-Z0-9\-_]', '_', string)
             