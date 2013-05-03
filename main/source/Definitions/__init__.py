import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_Initial_Condition_definition import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Initial_Condition_definition.py (need numpy & scipy.special)",
                  category=ImportWarning)

try:
    from Gravity_Potential_definition         import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Potential_definition.py (need numpy)",
                  category=ImportWarning)

