from read_data            import read_data_potential
from xml.dom.minidom      import parseString
from Gravity_Utilities    import getText
from Potential_definition import *

def read_data_mass(file_name):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('Mass')[0]
    mass   = float(getText(xmlTag.childNodes))
    return mass

def read_data_Lambda(file_name):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('Lambda')[0]
    Lambda = float(getText(xmlTag.childNodes))
    return Lambda

class Potential_def:

      def __init__(self):

         func        = 0.0
         dfunc       = 0.0
         self.mass   = 0.0
         self.Lambda = 0.0

         pot_name = read_data_potential()
         if (pot_name == "Massive_Scalar"):
            self.name  = Massive_Scalar_Potential
            self.dname = Massive_Scalar_dPotential
            self.mass  = read_data_mass("parameters/Potential_Parameters/Massive_Scalar.xml")
            print "Assigned Potential is: P(phi) = 1/2 m phi^2 "
            print "mass = " , self.mass
         elif (pot_name == "Higgs"):
            self.name  = Higgs_Potential
            self.dname = Higgs_dPotential
            self.mass  = read_data_mass("parameters/Potential_Parameters/Higgs.xml")
            self.Lambda= read_data_Lambda("parameters/Potential_Parameters/Higgs.xml")
            print "Assigned Potential is: P(phi) = 1/2 m phi^2 + Lambda phi^4 / 24"
            print "Lambda = " , self.Lambda
            print "mass   = " , self.mass
         elif (pot_name == "String1"):
            self.name  = String1_Potential
            self.dname = String1_dPotential
            print "Assigned Potential is: P(phi) = -3/(2l^2) cosh(phi/2)^2 (5 - cosh[phi]) + 6/l^2"
         elif (pot_name == "String2"):
            self.name  = String2_Potential
            self.dname = String2_dPotential
            print "Assigned Potential is: P(phi) = -2/l^2 ( exp[-2phi/sqrt(6)] + 2exp[phi/sqrt(6)] ) + 6/l^2"
         else:
            self.name  = Massless_Scalar_Potential
            self.dname = Massless_Scalar_dPotential
            print "Assigned Potential is: P(phi) = 0"

      def set_value(self,phi):
         Potential_def.func  = self.name(self.mass,self.Lambda,phi)
         Potential_def.dfunc = self.dname(self.mass,self.Lambda,phi)

