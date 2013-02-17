from numpy                    import *
from scipy                    import *

def Gamma_reader(filename = 'GammaMatrix.txt'):
    Gamma_var = loadtxt('./input_data/'+filename, delimiter=',', dtype = complex , unpack=True)
    Gamma_var = Gamma_var.T
    return Gamma_var


def Modify_Gamma(Gamma_old,Min_Gamma):
    Gamma_new = []
    f = open("./input_data/Gamma_new.txt", "w")
    for i in range(len(Gamma_old[:,0])):
       if ( abs(Gamma_old[i,8]) >= abs(Min_Gamma) ):
          f.write(    str(int(Gamma_old[i,0]))\
                +','+str(int(Gamma_old[i,1]))\
                +','+str(int(Gamma_old[i,2]))\
                +','+str(int(Gamma_old[i,3]))\
                +','+str(int(Gamma_old[i,4]))\
                +','+str(int(Gamma_old[i,5]))\
                +','+str(int(Gamma_old[i,6]))\
                +','+str(int(Gamma_old[i,7]))\
                +','+str(float(Gamma_old[i,8]))+'\n' )
    f.close()
    Gamma_new = loadtxt('./input_data/Gamma_new.txt', delimiter=',', dtype = float , unpack=True)
    Gamma_new = Gamma_new.T
    return Gamma_new


def Gamma_coef(Min_Gamma = 0.0,filename = 'GammaMatrix.txt'):
    Gamma_old = Gamma_reader(filename)
    Gamma_new = Modify_Gamma(Gamma_old,Min_Gamma)
    return Gamma_new

def Alpha_coef(filename = 'alpha_coe.txt'):
    Alpha_var = loadtxt('./input_data/'+filename, delimiter=',', dtype = complex , unpack=True)
    Alpha_var = Alpha_var.T
    return Alpha_var

def n_coef(filename = 'GammaMatrix.txt'):
    Gamma_var = loadtxt('./input_data/'+filename, delimiter=',', dtype = float , unpack=True)
    Gamma_var = Gamma_var.T
    n     = max(Gamma_var[:,0])
    return n

#print Gamma_coef(8.0)
#print Alpha_coef()
#print n_coef()
