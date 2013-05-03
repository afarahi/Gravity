import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_Report import Creat_Report
except ImportError:
    warnings.warn("Warning: Cannot import Creat_Report.py ",
                  category=ImportWarning)

