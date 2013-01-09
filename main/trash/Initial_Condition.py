from numpy             import *
from pylab             import *
from scipy             import *
from scipy.special     import *
from read_data         import read_data_initialize_method
from xml.dom.minidom   import parseString
from Gravity_Utilities import getText

def read_data_initialize_Gaussian(file_name = 'parameters/Initial_Condition/Gaussian.xml'):
    file = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag  = data.getElementsByTagName('epsilon')[0]
    epsilon = float(getText(xmlTag.childNodes))
    xmlTag  = data.getElementsByTagName('sigma')[0]
    sigma   = float(getText(xmlTag.childNodes))
    return (sigma,epsilon)

def read_data_initialize_Eigenfunction_modes_non_normalized(file_name = 'parameters/Initial_Condition/Eigenfunction_modes_non_normalized.xml'):
    file = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag  = data.getElementsByTagName('number_of_modes')[0]
    n       = int(getText(xmlTag.childNodes))
    xmlTag  = data.getElementsByTagName('non_normalized_modes_amplitude')[0]
    a       = float(getText(xmlTag.childNodes))
    return (n,a)

def initialize(x):
    #Reading Method
    Method = read_data_initialize_method()

    Phi = zeros(len(x))
    Pi  = zeros(len(x))
    phi = zeros(len(x))  
    
    #Gaussian initial condition
    if (Method == "Gaussian") :
       (sigma,eps) = read_data_initialize_Gaussian()
       for i in range(len(x)):
          phi[i]   = eps*exp(-tan(x[i])**2/sigma**2)
          Phi[i]   = -2.0*sin(x[i])*eps*exp(-tan(x[i])**2/sigma**2)/(sigma**2*cos(x[i])**3)   
       print "Assigned Initial Condition is: Gaussian"
    #Eigenfunction_modes initial condition
    elif (Method == "Eigenfunction_modes_non_normalized") :
       (n,a) = read_data_initialize_Eigenfunction_modes_non_normalized()
       for i in range(len(x)-1):
          for j in range(1,n+1):
             phi[i]  += a*sqrt(16.0*float(j+1)*float(j+2)/pi) * cos(x[i])**3 * hyp2f1(-j,3+j,1.5,sin(x[i])**2)
             Phi[i]  += -a*4.0*sqrt(float(2+3*j+j**2))/(3.0*sqrt(pi)) * (float(4*j*(j+3))*cos(x[i])**4*hyp2f1(1-j,4+j,2.5,sin(x[i])**2) + 9.0*cos(x[i])**2*hyp2f1(-j,3+j,1.5,sin(x[i])**2) )*sin(x[i])
       print "Assigned Initial Condition is: Eigenfunction modes non-normalized"
    else:
       print "YOUR INPUT METHOD IS NOT RIGHT!" 

    return (Pi,Phi,phi)
