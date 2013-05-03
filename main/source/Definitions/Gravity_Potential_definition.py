from numpy     import cosh, sinh, exp, sqrt
from Utilities import read_data_float

#################################################
#CONSTANTS:
l = 1.0
mass_S = read_data_float(tag_name = 'Mass',  file_name = "parameters/Potential_Parameters/Massive_Scalar.xml")
mass_H = read_data_float(tag_name = 'Mass',  file_name = "parameters/Potential_Parameters/Higgs.xml")
Lambda = read_data_float(tag_name = 'Lambda',file_name = "parameters/Potential_Parameters/Higgs.xml")

#################################################
#Potential Definitions

#Massless Scalar 
def Massless_Scalar_Potential(phi):
    return 0.0

#Massive Scalar 
def Massive_Scalar_Potential(phi):
    p = 0.5*mass_S*phi**2
    return p

#Higgs
def Higgs_Potential(phi):
    p = 0.5*mass_H*phi**2 + Lambda*phi**4/24.0
    return p

#String1
def String1_Potential(phi):
    p = -3.0/(2.0*l**2) * cosh(phi/2.0)**2 * (5.0 - cosh(phi)) + 6.0/(l**2)
    return p

#String2
def String2_Potential(phi):
    p = -2.0/(l**2) * ( exp(-2.0*phi/sqrt(6.0)) + 2.0*exp(phi/sqrt(6.0)) ) + 6.0/(l**2)
    return p

#################################################
#Derivative of Potential Definitions

#Massless Scalar 
def Massless_Scalar_dPotential(phi):
    return 0.0

#Massive Scalar 
def Massive_Scalar_dPotential(phi):
    dp = mass_S*phi
    return dp

#Higgs 
def Higgs_dPotential(phi):
    dp =  mass_H*phi + Lambda*phi**3/6.0
    return dp

#String1
def String1_dPotential(phi):
    dp = 3.0/(2.0*l**2)*cosh(phi/2.0)**2*sinh(phi) - 3.0/(2.0*l**2)*cosh(phi/2.0)*sinh(phi/2.0)*(5.0-cosh(phi))
    return dp

#String2
def String2_dPotential(phi):
    dp = -4.0/(sqrt(6.0)*l**2) * ( - exp(-2.0*phi/sqrt(6.0)) + exp(phi/sqrt(6.0)) )
    return dp

