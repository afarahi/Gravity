import warnings

try:
    ImportWarning
except NameError:
    class ImportWarning(Warning):
        pass

try:
    from Gravity_AdS4_RH_Construction import RK4_solver
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_AdS4_RH_Construction.py (need numpy)",
                  category=ImportWarning)

try:
    from Gravity_Solver_definition    import *
except ImportError:
    warnings.warn("Warning: Cannot import Gravity_Solver_definition.py ",
                  category=ImportWarning)

