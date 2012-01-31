"""
Import all ``pyforge`` functions at once.

Do ``from pyforge.all import *``, to import all ``pyforge`` functions in one 
command. Eg.::
    
    from pyforge.all import *
    # Use function from pyforge.string.id
    to_id('Awesome!')
    
"""


from pyforge.decorators import *
from pyforge.io         import *
from pyforge.iter       import *
from pyforge.mixins     import *

from pyforge.string        import *
from pyforge.string.id     import * 
from pyforge.string.line   import *
from pyforge.string.regexp import *
from pyforge.string.lang   import *
