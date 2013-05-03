import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_Power_Spectrum_Real_Space import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Power_Spectrum_Real_Space.py (need scipy.special & matplotlib)",
                  category=ImportWarning)

try:
    from Gravity_Power_Spectrum            import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Power_Spectrum.py (need matplotlib)",
                  category=ImportWarning)

