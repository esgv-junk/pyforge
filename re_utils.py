import itertools, re
from pyforge.decorators import *

@cache_iterable_argument
def make_strings_re(string_list):
    def is_char(s):
        return len(s) == 1
    
    chars = map(re.escape, filter(is_char, string_list))
    strings = map(re.escape, itertools.filterfalse(is_char, string_list))
    
    chars_re = '[' + ''.join(chars) + ']'
    if chars_re == '[]':
        chars_re = ''
        
    str_re = join_regexes(strings)
    delimiter = (str_re and chars_re) and '|' or ''
    
    return str_re + delimiter + chars_re

@works_with_string_regex
def regex_to_string(regex):
    return regex

@works_with_string_regex
def make_exact(regex):
    return '^(?:{regex})$'.format(regex=regex)

@works_with_string_regex
def capture_groups_removed(regex):
    return re.sub(r'\((?=[^?])', r'(?:', regex)

def join_regexes(regex_strings):
    enclosed_regexes = map(lambda r: '(?:{0})'.format(r), regex_strings) 
    return '|'.join(enclosed_regexes)
