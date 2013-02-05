#from Gravity_Parameters.Gravity_prop   import *
from Gravity_Parameters                import *
from Gravity_Dictionary                import *
from Gravity_Field_Properties          import *

b = Gravity_prop()
print b.Initial_Condition_type
print b.Potential_func(1.0,1.0,1.0)
print b.Potential_dfunc(1.0,1.0,1.0)

#print b.field.phi
a = Gravity_Dictionary
print a["Potential"]["Massless_Scalar"][1]#,type(a["Massless_Scalar"][1])
print a["Initial_Condition"]["Gaussian"]#,type(a["Massless_Scalar"][1])
