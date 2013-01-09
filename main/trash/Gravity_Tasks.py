from matplotlib.pyplot    import *
from AdS4_RK4_solver      import AdS4_RK4_solver
from Gravity_Parameters   import Gravity_obj

def main_tasks():

    Gravity_object = Gravity_obj()

    AdS4_RK4_solver(Gravity_object)

    if Gravity_object.field.Horizon :
       print "Horizon time is : ", Gravity_object.field.Horizon_ime
    else:
       print "Horizon is not created ...! (You may want to increase i_max)"

    #figure(1)
    #plot(Gravity_object.field.r,Gravity_object.field.Pi)
    #show()
    #figure(2)
    #plot(Gravity_object.field.r,Gravity_object.field.Phi)
    #show()
