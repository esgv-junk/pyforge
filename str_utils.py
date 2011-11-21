import itertools, re
from pyforge.re_utils import *


def is_char(s):
    return len(s) == 1

def reversed_dict(dict_):
    result = {}
    for k, v in dict_.items():
        result[v] = k
    return result

def multiple_replace(string, replace_dict):
    return re.sub(
        make_strings_re(replace_dict.keys()),
        lambda match_obj: replace_dict[match_obj.group(0)],
        string
    )
    
def multiple_replace_re(string, replace_list):
    for match_re, replace_str in replace_list:
        string = re.sub(match_re, replace_str, string)
    return string
    
escaped_text_re = r'(?:[^\\]|\\.)+?'

def to_id(string):
    return re.sub('[^a-zA-Z\-_]', '_', string)