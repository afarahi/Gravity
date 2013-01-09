from scipy.special     import *
from Gravity_Utilities import read_data_float, read_data_int

#Gaussian Initial Condition
def Initial_Condition_Gaussian(x):

    Phi = zeros(len(x))
    Pi  = zeros(len(x))
    phi = zeros(len(x))  
        
    sigma = read_data_float(tag_name = 'sigma' , file_name = 'parameters/Initial_Condition/Gaussian.xml')
    eps   = read_data_float(tag_name = 'epsilon' , file_name = 'parameters/Initial_Condition/Gaussian.xml')

    for i in range(len(x)):
       phi[i]   = eps*exp(-tan(x[i])**2/sigma**2)
       Phi[i]   = -2.0*sin(x[i])*eps*exp(-tan(x[i])**2/sigma**2)/(sigma**2*cos(x[i])**3)   
    print "Assigned Initial Condition is: Gaussian"
    return (phi , Phi , Pi)


#Non normalized Eigenfunction Modes Initial Condition
def Initial_Condition_Eigenfunction_modes_non_normalized(x):

    Phi = zeros(len(x))
    Pi  = zeros(len(x))
    phi = zeros(len(x))  

    n = read_data_int(tag_name = 'number_of_modes' , file_name = 'parameters/Initial_Condition/Eigenfunction_modes_non_normalized.xml')
    a = read_data_float(tag_name = 'non_normalized_modes_amplitude' , file_name = 'parameters/Initial_Condition/Eigenfunction_modes_non_normalized.xml')

    for i in range(len(x)-1):
       for j in range(1,n+1):
          phi[i]  += a*sqrt(16.0*float(j+1)*float(j+2)/pi) * cos(x[i])**3 * hyp2f1(-j,3+j,1.5,sin(x[i])**2)
          Phi[i]  += -a*4.0*sqrt(float(2+3*j+j**2))/(3.0*sqrt(pi)) * (float(4*j*(j+3))*cos(x[i])**4*hyp2f1(1-j,4+j,2.5,sin(x[i])**2) + 9.0*cos(x[i])**2*hyp2f1(-j,3+j,1.5,sin(x[i])**2) )*sin(x[i])
    print "Assigned Initial Condition is: Eigenfunction modes non-normalized"
    return (phi , Phi , Pi)
