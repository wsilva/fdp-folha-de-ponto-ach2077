from .base import *

try:
    from .dev import *
    live = False
except:
    live = True

if live:
    from .prod import *
