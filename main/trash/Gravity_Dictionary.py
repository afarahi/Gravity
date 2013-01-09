from Potential_definition         import *
from Initial_Condition_definition import *

Gravity_Dictionary = \
{
 "Potential":
 {
   "Massless_Scalar":[Massless_Scalar_Potential , Massless_Scalar_dPotential] ,
   "Massive_Scalar":[Massive_Scalar_Potential , Massive_Scalar_dPotential] ,
   "Higgs":[Higgs_Potential , Higgs_dPotential] ,
   "String1":[String1_Potential , String1_dPotential] ,
   "String2":[String2_Potential , String2_dPotential]
 },
 "Initial_Condition":
 {
   "Eigenfunction_modes_non_normalized":Initial_Condition_Eigenfunction_modes_non_normalized ,
   "Gaussian":Initial_Condition_Gaussian
 }
} 


