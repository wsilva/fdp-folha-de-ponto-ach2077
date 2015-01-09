from .base import *

try:
    from .dev import *
    live = False
except:
    from .prod import *
    live = True
