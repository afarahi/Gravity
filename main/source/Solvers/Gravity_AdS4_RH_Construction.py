from scipy            import *
from scipy.special    import *
from Objects          import Gravity_Dictionary
from Utilities        import read_data_string

Potential_type_name    = read_data_string(tag_name = 'Potential',file_name = 'parameters/parameters.xml')
Potential_func         = Gravity_Dictionary["Potential"][Potential_type_name][0]
Potential_dfunc        = Gravity_Dictionary["Potential"][Potential_type_name][1]

#Potential Definition
def Potential(phi):
    return Potential_func(phi)

#Derivative of Potential Definition
def dPotential(phi):
    return Potential_dfunc(phi)

#Right handside constractor of Phi
def RH_cons_Phi(x,Pi,delta,A):
    phipp = zeros(len(A))
    h     = x[1]-x[0]
    phipp[0] = 0.0
    for i in range(1,len(A)-1):
       phipp[i] = (A[i+1]*exp(-delta[i+1])*Pi[i+1] - A[i-1]*exp(-delta[i-1])*Pi[i-1])/(2.0*h)
    phipp[len(A)-1] = 0.0
    return phipp

#Right handside constractor of Pi
def RH_cons_Pi(x,Phi,phi,delta,A):
    pipp = zeros(len(A))
    h     = x[1]-x[0]
    for i in range(1,len(A)-1):
       pipp[i] = (A[i+1]*exp(-delta[i+1])*Phi[i+1]*tan(x[i+1])**2 - A[i-1]*exp(-delta[i-1])*Phi[i-1]*tan(x[i-1])**2)/(2.0*h*tan(x[i])**2) - exp(-delta[i])*dPotential(phi[i])/(cos(x[i])**2)
    pipp[1] = pipp[2]
    pipp[0] = pipp[1]
    pipp[len(A)-1] = 0.0
    return pipp

#Right handside constractor of Delta
def RH_cons_delta(x,Phi,Pi):
    RH_delta = -sin(x)*cos(x)*(Pi**2+Phi**2)
    return RH_delta

#Right handside constractor of A
def RH_cons_A(x,A,Phi,Pi,phi):
    RH_A = -A*sin(x)*cos(x)*(Pi**2+Phi**2) + (1.0-A)*(1.0+2.0*sin(x)**2)/(sin(x)*cos(x)) - 2.0*sin(x)*Potential(phi)/cos(x)
    return RH_A

#Right handside constractor of phi
def RH_cons_phi(Pi,delta,A):
    RH_phi = A*Pi*exp(-delta)
    return RH_phi

#Ricci Scalar
def Ricci_cal(x,Phi,Pi,phi,delta,A):
    R = -12.0 + 2.0*A*cos(x)**2*(Phi**2-Pi**2) + 8.0*Potential(phi)
    return R

