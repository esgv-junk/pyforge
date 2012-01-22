"""
Import all ``pyforge`` functions at once.

Do ``from pyforge.all import *``, to import all ``pyforge`` functions in one 
command. Eg.::
    
    from pyforge.all import *
    # Use function from pyforge.str.id
    to_id('Awesome!')
    
"""

from pyforge.decorators   import *
from pyforge.iter         import *
from pyforge.mixins       import *

from pyforge.str          import *
from pyforge.str.id       import * 
from pyforge.str.line     import *
from pyforge.str.regexp   import *
from pyforge.str.lang     import *