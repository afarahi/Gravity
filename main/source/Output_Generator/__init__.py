import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_Output_Construction  import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Output_Construction.py (need matplotlib)",
                  category=ImportWarning)

