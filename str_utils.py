import itertools, re
from pyforge.re_utils import *
from pyforge.iter_utils import *

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

transliterations = {
    'а': 'a' , 'б': 'b' , 'в': 'v'  , 'г': 'g', 'д': 'd', 'е': 'e',
    'ё': 'e' , 'ж': 'zh', 'з': 'z'  , 'и': 'i', 'й': 'j', 'к': 'k',
    'л': 'l' , 'м': 'm' , 'н': 'n'  , 'о': 'o', 'п': 'p', 'р': 'r',
    'с': 's' , 'т': 't' , 'у': 'u'  , 'ф': 'f', 'х': 'h', 'ц': 'c',
    'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '_', 'ы': 'y',  'ь': "'",
    'э': 'e' , 'ю': 'yu', 'я': 'ja'
}

def transliterate(string):
    upper_pairs = (
        (key.upper(), value.capitalize()) 
        for key, value in transliterations.items()
    )
    upper_transliterations = dict(upper_pairs)
    
    string = multiple_replace(string, transliterations)
    return multiple_replace(string, upper_transliterations)

def to_id(string):
    string = transliterate(string)
    return re.sub('[^a-zA-Z\-_]', '_', string)

def split_string(string, split_positions):
    split_positions = itertools.chain([-1], split_positions, [len(string)])
    return (
        string[begin+1:end]
        for (begin, end) in 
            group_k_forward(split_positions, lookahead=1)
    )