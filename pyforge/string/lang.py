# -*- coding: utf8 -*-

from os.path import join
import re
import hyphenator
from pyforge.string import multiple_replace

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

hyphen_dict_base = hyphenator.__path__[0]
_hyphenators = [
    hyphenator.Hyphenator(join(hyphen_dict_base, 'hyph_ru_RU.dic'))
]

def hyphenate_word(word, hyphen='-'):
    for hyphenator in _hyphenators:
        word = hyphenator.inserted(word, hyphen)
    return word

def hyphenate(text, hyphen='-'):
    return re.sub(
        '\w+',
        lambda match_obj: hyphenate_word(match_obj.group(0), hyphen),
        text
    )
