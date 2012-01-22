# -*- coding: utf8 -*-

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