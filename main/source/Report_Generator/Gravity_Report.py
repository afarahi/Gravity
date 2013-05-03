import subprocess
import os
import shlex
from matplotlib.pyplot            import *
from matplotlib                   import rc
from Gravity_tex_Construction     import Report_File

rc('font',family='serif')

def Report_Plot_Construction(Gravity_object):
    rc('text',usetex=True)    

    clf()
    plot(Gravity_object.field.r,Gravity_object.field.Pi)
    xlabel(r'$r$',fontsize = 20)
    ylabel(r'$\Pi$',fontsize = 20)
    fdir  = 'Report/'
    fname = 'PivrR.pdf'
    print 'Saving plot (r , Pi) ', fname
    savefig(fdir+fname)

    clf()
    plot(Gravity_object.field.r,Gravity_object.field.Phi)
    xlabel(r'$r$',fontsize = 20)
    ylabel(r'$\Phi$',fontsize = 20)
    fdir  = 'Report/'
    fname = 'PhivrR.pdf'
    print 'Saving plot (r , Phi)', fname
    savefig(fdir+fname)

    clf()
    plot(Gravity_object.field.r,Gravity_object.field.phi)
    xlabel(r'$r$',fontsize = 20)
    ylabel(r'$\phi$',fontsize = 20)
    fdir  = 'Report/'
    fname = 'phivrR.pdf'
    print 'Saving plot (r , phi)', fname
    savefig(fdir+fname)

    rc('text',usetex=False)    

def Reprt_Data_Construction(Gravity_object):
    f1 = open("Report/data.txt", "w")
    #column names
    f1.write("#     r             phi             Phi             Pi             Ricci\n")
    for k in range(0,Gravity_object.Grid_size):
       f1.write('%12.10f%16.10f%16.10f%16.10f%16.10f\n'%(Gravity_object.field.r[k], Gravity_object.field.phi[k], Gravity_object.field.Phi[k], Gravity_object.field.Pi[k], Gravity_object.field.Ricci_Scalar[k]))
    f1.close()

def Creat_Report(Gravity_object):
    print "Creating report ..."
    Report_Plot_Construction(Gravity_object)
    Reprt_Data_Construction(Gravity_object)
    print "Creating tex file ..."
    Report_File(Gravity_object)

    proc=subprocess.Popen(shlex.split('pdflatex Report/report.tex'))
    proc.communicate()
    proc=subprocess.Popen(shlex.split('pdflatex Report/report.tex'))
    proc.communicate()
    proc=subprocess.Popen(shlex.split('cp report.pdf Report'))
    proc.communicate()
    os.unlink('report.aux')
    os.unlink('report.log')
    os.unlink('report.out')
    os.unlink('report.pdf')
    
    print "Report is created successfully."
    
