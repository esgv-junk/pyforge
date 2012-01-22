import itertools, re
from pyforge.iter import group_k_forward
from pyforge.string.regexp import make_strings_re

def is_char(s):
    return len(s) == 1

def reversed_dict(dict_):
    result = {}
    for k, v in dict_.items():
        if v in result:
            raise ValueError(
                "Dict is not reversable: value {0} encountered twice".format(v)
            ) 
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
    
backslash_escaped_text_re = r"(?:[^\\]|\\.)+?"

def split_string(string, split_positions):
    split_positions = itertools.chain([-1], split_positions, [len(string)])
    return (
        string[begin+1:end]
        for (begin, end) in 
            group_k_forward(split_positions, lookahead=1)
    )