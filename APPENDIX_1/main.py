from numpy                    import *
from scipy                    import *
from scipy.special            import *
from matplotlib.pyplot        import *
from numpy.fft                import *
from Gamma_mod                import Gamma_coef,Alpha_coef,n_coef
#from matplotlib                   import rc

#rc('text',usetex=False)
#rc('font',family='serif')

#Right handside constractor of Phi
def RH_cons_Phi(Gamma_coe,alpha,Phi,n,nt,index):
    Phi_new = zeros([n,n,nt],complex)
    for i in range(len(alpha[:,0])):
      Phi_new[int(alpha[i,0])-1,int(alpha[i,1])-1,index] += alpha[i,2]*Phi[int(alpha[i,0])-1,int(alpha[i,1])-1,index]
    for i in range(len(Gamma_coe[:,0])):
      Phi_new[int(Gamma_coe[i,0])-1,int(Gamma_coe[i,4])-1,index] +=   Gamma_coe[i,8] \
                                                    * Phi[int(Gamma_coe[i,1])-1,int(Gamma_coe[i,5])-1,index] \
                                                    * Phi[int(Gamma_coe[i,2])-1,int(Gamma_coe[i,6])-1,index] \
                                                    * Phi[int(Gamma_coe[i,3])-1,int(Gamma_coe[i,7])-1,index]
    return Phi_new

#Boundary condition 
def apply_boundary(n,nt):
    Phi = zeros([n,n,nt],complex)
    Phi_var = loadtxt('./input_data/initial_condition.txt', delimiter=',', dtype = complex , unpack=True)
    Phi_var = Phi_var.T 
    for i in range(len(Phi_var[:,0])):
        Phi[int(Phi_var[i,0])-1,int(Phi_var[i,1])-1,0] = Phi_var[i,2]
    return Phi

#Runge-Kutta coefficient
def RK4_cons(Gamma_coe,alpha,Phi,dt,n,nt,index):
    k1 = dt*RH_cons_Phi( Gamma_coe , alpha , Phi        ,n,nt,index)
    k2 = dt*RH_cons_Phi( Gamma_coe , alpha , Phi+0.5*k1 ,n,nt,index)
    k3 = dt*RH_cons_Phi( Gamma_coe , alpha , Phi+0.5*k2 ,n,nt,index)
    k4 = dt*RH_cons_Phi( Gamma_coe , alpha , Phi+    k3 ,n,nt,index)
    return (k1,k2,k3,k4)

#Left handside constractor
def LH_cons(Gamma_coe,alpha,Phi_old,dt,n,nt,index):
    (k1,k2,k3,k4) = RK4_cons(Gamma_coe,alpha,Phi,dt,n,nt,index)
    Phi_new = Phi_old + (k1+2.0*k2+2.0*k3+k4)/6.0
    return Phi_new
  
#RK4 Solver
def RK4_solver(Phi,Gamma,Alpha,t,n,nt):
    dt = t[1]-t[0]
    #Solver
    for i in range(1,len(t)):
        for j in range(n):
           for k in range(n):
              Phi[j,k,i] = LH_cons(Gamma,Alpha,Phi,dt,n,nt,i-1)[j,k,i-1]
        if (i%20 == 0):
           print 'time = ' , t[i]
    return Phi


#########################
####### MAIN CODE #######
#########################

Min_Gamma = input("Please enter Min Gamma : ")
T_max     = input("Please enter final time : ")
mesh_size = input("Please enter mesh size : ")
Amplitude = input("Please enter the amplitude of initial condition : ")


Gamma     = Gamma_coef(Min_Gamma)
Alpha     = Alpha_coef()
n         = int(n_coef())
t         = linspace(0.0,T_max,mesh_size+1)
nt        = mesh_size+1

#Apply Boundary Condition
Phi = Amplitude*apply_boundary(n,nt)
Phi = RK4_solver(Phi,Gamma,Alpha,t,n,nt)

#print Phi[1,1,:]


########################################
######### CREATING OUTPUT ##############
########################################

#Time Evolution
for i in range(n):
   for j in range(n):
      istr = str(i+1)
      jstr = str(j+1)
      f = open("./saved_data/data/Phi_"+istr+"_"+jstr+"_real", "w")
      f.write("#        time                    Phi_"+istr+"_"+jstr+"_real\n")
      savetxt(f, array([t,Phi[i,j,:].real]).T)
      f.close()
      f = open("./saved_data/data/Phi_"+istr+"_"+jstr+"_imag", "w")
      f.write("#        time                    Phi_"+istr+"_"+jstr+"_imag\n")
      savetxt(f, array([t,Phi[i,j,:].imag]).T)
      f.close()
      clf()
      plot(t,Phi[i,j,:].real)
#      xlabel(r'$r$',fontsize = 16)
#      ylabel(r'$\phi$',fontsize = 16)
      fname = "./saved_data/plot/Time_Evolution/Phi_"+istr+"_"+jstr+"_real.png"
      print 'Saving frame', fname
      savefig(fname)
      clf()
      plot(t,Phi[i,j,:].imag)
#      xlabel(r'$r$',fontsize = 16)
#      ylabel(r'$\phi$',fontsize = 16)
      fname = "./saved_data/plot/Time_Evolution/Phi_"+istr+"_"+jstr+"_imag.png"
      print 'Saving frame', fname
      savefig(fname)


#Max & Min Evolution
for i in range(len(Phi[:,0,0])):
   for j in range(len(Phi[0,:,0])):
      istr = str(i+1)
      jstr = str(j+1)
      ExpPhiReal = []
      TimeReal   = []
      ExpPhiImag = []
      TimeImag   = []
      if ( Phi[i,j,0].real < Phi[i,j,1].real):
         Breal = True
      else:
         Breal = False
      if ( Phi[i,j,0].imag < Phi[i,j,1].imag):
         Bimag = True
      else:
         Bimag = False
      for k in range(1,len(Phi[0,0,:])):
         if (Breal):
            if ( Phi[i,j,k-1].real <= Phi[i,j,k].real):
                ExpPhiReal.append(abs(Phi[i,j,k].real))
                TimeReal.append(t[k])
                Breal = False
         else:
            if ( Phi[i,j,k-1].real >= Phi[i,j,k].real):
                ExpPhiReal.append(abs(Phi[i,j,k].real))
                TimeReal.append(t[k])
                Breal = True
         if (Bimag):
            if ( Phi[i,j,k-1].imag <= Phi[i,j,k].imag):
                ExpPhiImag.append(abs(Phi[i,j,k].imag))
                TimeImag.append(t[k])
                Bimag = False
         else:
            if ( Phi[i,j,k-1].imag >= Phi[i,j,k].imag):
                ExpPhiImag.append(abs(Phi[i,j,k].imag))
                TimeImag.append(t[k])
                Bimag = True
      ExpPhiReal.pop(0)
      TimeReal.pop(0)
      ExpPhiImag.pop(0)
      TimeImag.pop(0)

      clf()
      print 'Saving frame', fname
      plot(TimeReal,ExpPhiReal)
      fname = "./saved_data/plot/Max_Evolution/Phi_"+istr+"_"+jstr+"_real.png"
      savefig(fname)

      clf()
      print 'Saving frame', fname
      plot(TimeImag,ExpPhiImag)
      fname = "./saved_data/plot/Max_Evolution/Phi_"+istr+"_"+jstr+"_imag.png"
      savefig(fname)


#Power Spectrum Evolution
for i in range(len(Phi[:,0,0])):
   for j in range(len(Phi[0,:,0])):
      istr = str(i+1)
      jstr = str(j+1)

      w     = rfft(Phi[i,j,:].real)
      ps    = abs(w)**2
      omega = linspace(0.0,2.0*pi*len(ps)/t[len(t)-1],len(ps))
      clf()
      print 'Saving frame', fname
      loglog(omega[1:len(ps)-1],ps[1:len(ps)-1])
      fname = "./saved_data/plot/Power_Spectrum/Phi_"+istr+"_"+jstr+"_real.png"
      savefig(fname) 

      w     = rfft(Phi[i,j,:].imag)
      ps    = abs(w)**2
      omega = linspace(0.0,2.0*pi*len(ps)/t[len(t)-1],len(ps))
      clf()
      print 'Saving frame', fname
      loglog(omega[1:len(ps)-1],ps[1:len(ps)-1])
      fname = "./saved_data/plot/Power_Spectrum/Phi_"+istr+"_"+jstr+"_imag.png"
      savefig(fname) 

