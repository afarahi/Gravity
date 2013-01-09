from matplotlib.pyplot    import *
from Solver_definition    import *
from Gravity_Parameters   import Gravity_obj
from Gravity_Utilities    import read_data_string
from Gravity_Report       import Creat_Report

def Gravity_Solver():
    #Solver Type
    Geometry_type_name = read_data_string(tag_name='Geometry_type',file_name='parameters/parameters.xml')
    Solver_type_name   = read_data_string(tag_name = 'Solver_type',file_name = 'parameters/parameters.xml')
    Solver_type        = Geometry_type_name + "+" + Solver_type_name
    if (Solver_type == "AdS4+RK4"):
       return AdS4_RK4_solver
    else:
       print "ERROR : THE SOLVER IS NOT DEFINED FOR THIS GEOMETRY + SOLVER TYPE"
       return NO_SOLVER


def main_tasks():

    Gravity_object = Gravity_obj()    
    Solver         = Gravity_Solver() 
    Solver(Gravity_object)

    if Gravity_object.field.Horizon :
       print "Horizon time is : ", Gravity_object.field.time
    else:
       print "Horizon is not formed ...! (You may want to increase i_max)"

    Creat_Report(Gravity_object)

    #figure(1)
    #plot(Gravity_object.field.r,Gravity_object.field.Pi)
    #show()
    #figure(2)
    #plot(Gravity_object.field.r,Gravity_object.field.Phi)
    #show()


