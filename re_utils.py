import itertools, re

CompiledRegexType = type(re.compile(""))

def is_char(s):
    # BUG: is duplicated in str_utils!
    return len(s) == 1

def make_strings_re(string_list):
    chars = map(re.escape, filter(is_char, string_list))
    strings = map(re.escape, itertools.filterfalse(is_char, string_list))
    
    char_class = ''.join(chars)
    chars_re = (
        '[' + char_class + ']'
        if char_class 
        else ''
    )
    
    str_re = '|'.join(
        '(?:' + string + ')' 
        for string in strings
    )
    
    return str_re + ('|' if (str_re and chars_re) else '') + chars_re

def make_exact(regex):
    return '^(?:{regex})$'.format(regex=regex)

def join_regexes(*regexes):
    enclosed_regexes = map(lambda r: '(?:{0})'.format(r), regexes) 
    return '|'.join(enclosed_regexes)

def capture_groups_removed(regex):
    # BUG: needs tweaking for named capture groups
    if isinstance(regex, CompiledRegexType):
        return re.compile(capture_groups_removed(regex.pattern))
    else:
        return re.sub(r'\((?=[^?])', r'(?:', regex)
