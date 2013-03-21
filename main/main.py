import sys
sys.path.insert(0,sys.path[0]+'/source')
sys.path.insert(0,sys.path[1]+'/source/Objects')
sys.path.insert(0,sys.path[2]+'/source/Solvers')
sys.path.insert(0,sys.path[3]+'/source/Utilities')
sys.path.insert(0,sys.path[4]+'/source/Power_Spectrum')
sys.path.insert(0,sys.path[5]+'/source/tests')

from Gravity_Tasks import main_tasks

main_tasks()

