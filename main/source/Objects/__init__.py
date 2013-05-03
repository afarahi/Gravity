import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_Field_Properties  import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Field_Properties.py",
                  category=ImportWarning)

try:
    from Gravity_Output_Properties import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Output_Properties.py",
                  category=ImportWarning)

try:
    from Gravity_Parameters        import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Parameters.py",
                  category=ImportWarning)

