import math
import sys

import functions
from legb import X as LEGB_X, func
import pypackage
from pypackage import pymodule
# import pypackage.pymodule


pi = 3.14
X = 999

print(type(math), math.__name__, math.__doc__)
print(math.pi, math.sqrt(9))

print(pi)

print(type(functions), functions.__name__, functions.__doc__)
functions.greet("Anna")

print(LEGB_X, X)
func(3)

pypackage.other_func()
pymodule.pyfunc()
# pypackage.pymodule.pyfunc()

print(sys.path)
