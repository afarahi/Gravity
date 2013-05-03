from Utilities         import Linear_Fit_Line 
from Objects           import Gravity_obj
from numpy             import linspace, loadtxt, zeros, pi, sin, cos, log, exp, sqrt, tan
from scipy.special     import hyp2f1
from matplotlib.pyplot import *
from matplotlib        import rc

rc('font',family='serif')

def Power_Spectrum_Real_Space_e1(f,x,modes_number):
    n = modes_number + 1
    if (n<2):
       print "ERROR: It can not calculate the power spectrum of real space because the number of input points are not enough."
       return 0
    else:
       mode = zeros(n)
       amp  = zeros(n)

       amp[0] = float('inf')
#       for j in range(1,len(t)):
#          pk[0] += 0.5*(t[j]-t[j-1])*(x[j]+x[j-1])/2.0

       for i in range(1,n):
          A = 0.0
          B = 0.0
          for j in range(1,len(x)-1):
             A += ( f[j]*sqrt(16.0*float(i+1)*float(i+2)/pi)*cos(x[j])**3*hyp2f1(-i,3+i,1.5,sin(x[j])**2)*tan(x[j])**2 \
            + f[j-1]*sqrt(16.0*float(i+1)*float(i+2)/pi)*cos(x[j-1])**3*hyp2f1(-i,3+i,1.5,sin(x[j-1])**2)*tan(x[j-1])**2 ) \
                  * (x[j]-x[j-1])/2.0
#             B += -4.0*sqrt(2.0+3.0*float(i)+float(i)**2)/(3.0*(3.0+2.0*float(i))*sqrt(pi)) \
#                 *( f[j]*sin(x[j])*(4.0*float(i)*(3.0+float(i))*cos(x[j])**4*hyp2f1(1-i,4+i,2.5,sin(x[j])**2) \
#                                + 9.0*cos(x[j])**2*hyp2f1(-i,3+i,1.5,sin(x[j])**2) )*tan(x[j])**2\
#                   +f[j-1]*sin(x[j-1])*(4.0*float(i)*(3.0+float(i))*cos(x[j-1])**4*hyp2f1(1-i,4+i,2.5,sin(x[j-1])**2) \
#                                + 9.0*cos(x[j-1])**2*hyp2f1(-i,3+i,1.5,sin(x[j-1])**2) )*tan(x[j-1])**2 )\
#                  * (x[j]-x[j-1])/2.0

          mode[i]= float(i)
          amp[i] = (A**2 + B**2)/2.0

          print "mode = ", mode[i], " & Amplitude = ", amp[i]

       return (mode,amp)

def Power_Spectrum_Real_Space_e2(f,x,modes_number):
    n = modes_number + 1
    if (n<2):
       print "ERROR: It can not calculate the power spectrum of real space because the number of input points are not enough."
       return 0
    else:
       mode = zeros(n)
       amp  = zeros(n)

       amp[0] = float('inf')

       for i in range(1,n):
          A = 0.0
          B = 0.0
          for j in range(1,len(x)-1):
             B += -4.0*sqrt(2.0+3.0*float(i)+float(i)**2)/(3.0*(3.0+2.0*float(i))*sqrt(pi)) \
                 *( f[j]*sin(x[j])*(4.0*float(i)*(3.0+float(i))*cos(x[j])**4*hyp2f1(1-i,4+i,2.5,sin(x[j])**2) \
                                + 9.0*cos(x[j])**2*hyp2f1(-i,3+i,1.5,sin(x[j])**2) )*tan(x[j])**2\
                   +f[j-1]*sin(x[j-1])*(4.0*float(i)*(3.0+float(i))*cos(x[j-1])**4*hyp2f1(1-i,4+i,2.5,sin(x[j-1])**2) \
                                + 9.0*cos(x[j-1])**2*hyp2f1(-i,3+i,1.5,sin(x[j-1])**2) )*tan(x[j-1])**2 )\
                  * (x[j]-x[j-1])/2.0

          mode[i]= float(i)
          amp[i] = (A**2 + B**2)/2.0

          print "mode = ", mode[i], " & Amplitude = ", amp[i]

       return (mode,amp)

    

def Real_Space_Power_Spectrum_Plot_Construction(Gravity_obj,file_loc_save="Output/Real_Space_Power_Spectrum/"):

    rc('text',usetex=True)    

    modes_number = Gravity_obj.output.Real_Space_Power_Spectrum_modes_number
    function     = Gravity_obj.field.Pi
    x            = Gravity_obj.field.r

    (mode,amp) = Power_Spectrum_Real_Space_e1(function,x,modes_number)       
    clf()
    semilogy(mode,amp/amp[1])

#    coef   = Linear_Fit_Line(log(k[len(k)/10:len(k)-1]),log(pk[len(k)/10:len(k)-1]/pk[1]))
#    Gravity_obj.field.Power_Spec_n.append(coef[0])
#    loglog(k,coef[1]*k**coef[0],label=r'$\propto k^{ %0.2f }$'%Gravity_obj.field.Power_Spec_n[i])

#    legend()
    xlabel(r'Mode',fontsize = 20)
    ylabel(r'$log($Amp$)$',fontsize = 20)
#    title(r'$r = '+str(r[i])+r'$',fontsize = 20)
    fdir  = file_loc_save
    fname = 'Real_Space_Power_Spectrum_Pi.pdf'
#    print 'n = ', Gravity_obj.field.Power_Spec_n[i]
    print 'Saving plot', fname
    savefig(fdir+fname)


    function     = Gravity_obj.field.Phi
    x            = Gravity_obj.field.r

    (mode,amp) = Power_Spectrum_Real_Space_e2(function,x,modes_number)       
    clf()
    semilogy(mode,amp/amp[1])

    xlabel(r'Mode',fontsize = 20)
    ylabel(r'$log($Amp$)$',fontsize = 20)
    fdir  = file_loc_save
    fname = 'Real_Space_Power_Spectrum_Phi.pdf'
    print 'Saving plot', fname
    savefig(fdir+fname)


    rc('text',usetex=False)  

