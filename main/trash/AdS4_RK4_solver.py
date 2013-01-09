from numpy                        import *
from pylab                        import *
from scipy                        import *
from scipy.special                import *
from matplotlib.pyplot            import *
from Gravity_AdS4_RH_Construction import *
from Gravity_Output_Construction  import Output_Plot_Construction, Output_Data_Construction

#Initianlization
#Constants:
l         = read_data_float(tag_name = 'Cosmological_cosntant',  file_name = "parameters/parameters.xml")
A_horizon = read_data_float(tag_name = 'A_min',  file_name = "parameters/parameters.xml")

#Delta Solver
def Delta_Solver(x,Phi,Pi):
    delta    = zeros(len(x))
    dx       = x[1]-x[0]
    delta[0] = 0.0
    for i in range(0,len(x)-1):
       k1 = dx*RH_cons_delta( x[i]        ,  Phi[i]               ,  Pi[i]               )
       k2 = dx*RH_cons_delta( x[i]+0.5*dx , (Phi[i+1]+Phi[i])/2.0 , (Pi[i+1]+Pi[i])/2.0  )
       k3 = dx*RH_cons_delta( x[i]+0.5*dx , (Phi[i+1]+Phi[i])/2.0 , (Pi[i+1]+Pi[i])/2.0  )
       k4 = dx*RH_cons_delta( x[i]+dx     ,  Phi[i+1]             ,  Pi[i+1]             )
       delta[i+1] = delta[i] + (k1+2.0*k2+2.0*k3+k4)/6.0 
    return delta

#A Solver
def A_Solver(x,Phi,Pi,phi):
    A    = ones(len(x))
    dx   = x[1]-x[0]
    A[0] = 1.0
    A[1] = A[0]-dx*A[0]*sin(x[1])*cos(x[1])*(Pi[1]**2+Phi[1]**2) - dx*2.0*sin(x[1])*l**2*Potential(phi[1])/cos(x[1])
    for i in range(1,len(x)-2):
       k1 = dx*RH_cons_A( x[i]        , A[i]        ,  Phi[i]               ,  Pi[i]              ,  phi[i]              )
       k2 = dx*RH_cons_A( x[i]+0.5*dx , A[i]+0.5*k1 , (Phi[i+1]+Phi[i])/2.0 , (Pi[i+1]+Pi[i])/2.0 , (phi[i+1]+phi[i])/2.0)
       k3 = dx*RH_cons_A( x[i]+0.5*dx , A[i]+0.5*k2 , (Phi[i+1]+Phi[i])/2.0 , (Pi[i+1]+Pi[i])/2.0 , (phi[i+1]+phi[i])/2.0)
       k4 = dx*RH_cons_A( x[i]+dx     , A[i]+k3     ,  Phi[i+1]             ,  Pi[i+1]            ,  phi[i+1]            )
       A[i+1] = A[i] + (k1+2.0*k2+2.0*k3+k4)/6.0
    return A

#Boundary condition 
def appl_bondary(x,eps,sigma):
    Phi = boundary_Phi(x,eps,sigma)
    Pi_f= boundary_Pi(x)
    return (Phi,Pi_f)

#Runge-Kutta coefficient
def RK4_cons(x,Phi,Pi,phi,delta,A,dt):

    delta_new = delta
    A_new     = A
    kp1 = dt*RH_cons_Phi    ( x ,               Pi                       ,delta_new,A_new)
    kn1 = dt*RH_cons_Pi     ( x , Phi                      , phi         ,delta_new,A_new)
    km1 = dt*RH_cons_phi    (                   Pi                       ,delta_new,A_new)

    delta_new = Delta_Solver( x , Phi+0.5*kp1 , Pi+0.5*kn1                               )
    A_new     = A_Solver    ( x , Phi+0.5*kp1 , Pi+0.5*kn1 , phi+0.5*km1                 )
    kp2 = dt*RH_cons_Phi    ( x ,               Pi+0.5*kn1               ,delta_new,A_new)
    kn2 = dt*RH_cons_Pi     ( x , Phi+0.5*kp1              , phi+0.5*km1 ,delta_new,A_new)
    km2 = dt*RH_cons_phi    (                   Pi+0.5*kn1               ,delta_new,A_new)

    delta_new = Delta_Solver( x , Phi+0.5*kp2 , Pi+0.5*kn2                               )
    A_new     = A_Solver    ( x , Phi+0.5*kp2 , Pi+0.5*kn2 , phi+0.5*km2                 )
    kp3 = dt*RH_cons_Phi    ( x ,               Pi+0.5*kn2               ,delta_new,A_new)
    kn3 = dt*RH_cons_Pi     ( x , Phi+0.5*kp2              , phi+0.5*km2 ,delta_new,A_new)
    km3 = dt*RH_cons_phi    (                   Pi+0.5*kn2               ,delta_new,A_new)

    delta_new = Delta_Solver( x , Phi+kp3     , Pi+kn3                                   )
    A_new     = A_Solver    ( x , Phi+kp3     , Pi+kn3     , phi+km3                     )
    kp4 = dt*RH_cons_Phi    ( x ,               Pi+kn3                   ,delta_new,A_new)
    kn4 = dt*RH_cons_Pi     ( x , Phi+kp3                  , phi+km3     ,delta_new,A_new)
    km4 = dt*RH_cons_phi    (                   Pi+kn3                   ,delta_new,A_new)

    return (kp1,kp2,kp3,kp4,kn1,kn2,kn3,kn4,km1,km2,km3,km4)

#Left handside constractor
def LH_cons(x,Phi,Pi,phi,delta,A,dt):
    (kp1,kp2,kp3,kp4,kn1,kn2,kn3,kn4,km1,km2,km3,km4) = RK4_cons(x,Phi,Pi,phi,delta,A,dt)
    Phi_new = Phi + (kp1+2.0*kp2+2.0*kp3+kp4)/6.0
    Pi_new  = Pi  + (kn1+2.0*kn2+2.0*kn3+kn4)/6.0
    phi_new = phi + (km1+2.0*km2+2.0*km3+km4)/6.0
    return (Phi_new,Pi_new,phi_new)

#dt: Courant Condition
def dt_cal(dt,dx,A,delta):
    courant_con = min(exp(delta)*dx/A)
    if (dt < 0.5*abs(courant_con)):
        dtp = dt
    else:
        dtp = 0.25*abs(courant_con)
    return dtp

#Horizon Condition
def Horizon_con(A):
    if (abs(min(A)) < A_horizon):
      b = True
    else:
      b = False
    return b 
  
#RK4 Solver for AdS4
def AdS4_RK4_solver(Gravity_object):

    #Grid size
    Grid_size  = Gravity_object.Grid_size
    #Number of node for data saving
    # x is changing from 0 to 2pi x = [0,pi/2]
    x          = Gravity_object.field.r
    time = 0.0
    dt   = (x[1]-x[0])/4.0
    dx   = x[1]-x[0]
    i    = 0

    #Writting data
    f1 = open("saved_data/"+Gravity_object.output.Data_file_name, "w")
    #column names
    f1.write("#  time               r              phi             Phi             Pi            delta              A            Ricci\n")
    f1.close()

    #Apply Initial condition

    delta   = Delta_Solver(x,Gravity_object.Phi,Gravity_object.Pi)
    A       = A_Solver(x,Gravity_object.Phi,Gravity_object.Pi,Gravity_object.phi)

    #Plot initial condition
#    plot(x,A)
#    show()
#    plot(x,delta)
#    show()
#    plot(x,Gravity_object.phi)
#    show()

    #Solver
    Phi_new = zeros(len(x))
    Pi_new  = zeros(len(x))
    phi_new = zeros(len(x))
    while(True):
       dt_c                     = dt_cal(dt,dx,A,delta)
       (Phi_new,Pi_new,phi_new) = LH_cons(x,Gravity_object.field.Phi,Gravity_object.field.Pi,Gravity_object.field.phi,delta,A,dt_c)
       delta                    = Delta_Solver(x,Phi_new,Pi_new)
       A                        = A_Solver(x,Phi_new,Pi_new,phi_new)
    #Test and Save data
#       if (i%50==0):
#	  plot(x,A)
#      	  show()
#         plot(x,delta)
#         show()
#         plot(x,Phi_new)
#         show()
#         plot(x,Pi_new)
#         show()
       
       Gravity_object.field.Phi = Phi_new
       Gravity_object.field.Pi  = Pi_new
       Gravity_object.field.phi = phi_new

       i      += 1
       time   += dt

       if (i%Gravity_object.output.Frame_time_step==0):
          Output_Plot_Construction(Gravity_object,x,Phi_new,Pi_new,phi_new)

          Gravity_object.field.Ricci_Scalar = Ricci_cal(x,Phi_new,Pi_new,phi_new,delta,A)
          Output_Data_Construction(Gravity_object,x,delta,A,time+dt)

       #Ending Loop
       if Horizon_con(A):
          Gravity_object.field.Horizon      = True
          Gravity_object.field.Horizon_time = time
          break

       if(i == Gravity_object.Max_interation):
          break
    
    Gravity_object.field.Ricci_Scalar = Ricci_cal(x,Phi_new,Pi_new,phi_new,delta,A)
         
