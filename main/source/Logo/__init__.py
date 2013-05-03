import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

from Gravity_logo     import Print_logo
from Gravity_ending   import Print_ending
