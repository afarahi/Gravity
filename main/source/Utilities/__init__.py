import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_Utilities  import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Utilities.py",
                  category=ImportWarning)

try:
    from Gravity_Utility_Best_Fit_Line import Linear_Fit_Line
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Utility_Best_Fit_Line.py",
                  category=ImportWarning)
