from Utilities         import Linear_Fit_Line 
from Objects           import Gravity_obj
from numpy             import linspace, loadtxt, zeros, pi, sin, cos, log, exp
from matplotlib.pyplot import *
from matplotlib        import rc

rc('font',family='serif')

def Power_Spectrum_1D_Cal(t,x,Setting_number):
    n = int(len(t)/Setting_number)
    if (n<2):
       print "ERROR: It can not calculate the power spectrum because the number of input points are not enough."
       return 0
    elif (len(x) != len(t)):
       print "ERROR: It can not calculate the power spectrum because the dimentionality of input parameters does not match."
       return 0
    else:
       omega = linspace(0.0,float(n-1)*pi/t[len(t)-1],n)
       pk= zeros(n)
       k = zeros(n)

       for j in range(1,len(t)):
          pk[0] += 0.5*(t[j]-t[j-1])*(x[j]+x[j-1])/2.0

       for i in range(1,n):
          A = 0.0
          B = 0.0
          for j in range(1,len(t)):
             A += (t[j]-t[j-1])*(x[j]*sin(2.0*float(i)*pi*t[j]/t[len(t)-1])+x[j-1]*sin(2.0*float(i)*pi*t[j-1]/t[len(t)-1]))/2.0
             B += (t[j]-t[j-1])*(x[j]*cos(2.0*float(i)*pi*t[j]/t[len(t)-1])+x[j-1]*cos(2.0*float(i)*pi*t[j-1]/t[len(t)-1]))/2.0
          pk[i] = (A**2 + B**2)/2.0
          k[i]  = float(i)
       return (k,pk)
    

def Power_Spectrum_Plot_Construction(Gravity_obj,file_loc_save="Report/",file_loc_load="Output/Power_Spectrum_data/"):
    rc('text',usetex=True)    

    Setting_number = Gravity_obj.output.Power_Spectrum_Setting_number

    (t , r , Ricci) = loadtxt(file_loc_load+Gravity_obj.output.Power_Spectrum_file_name,dtype='float',comments='#',unpack=True)

    for i in range(Gravity_obj.output.Power_Spectrum_points):
       t_local     = zeros(len(t)/Gravity_obj.output.Power_Spectrum_points)
       Ricci_local = zeros(len(t)/Gravity_obj.output.Power_Spectrum_points)

       for j in range(len(t)/Gravity_obj.output.Power_Spectrum_points):
          t_local[j]     = t[j*Gravity_obj.output.Power_Spectrum_points+i]
          Ricci_local[j] = Ricci[j*Gravity_obj.output.Power_Spectrum_points+i]

       (k,pk) = Power_Spectrum_1D_Cal(t_local,Ricci_local,Setting_number)       
       clf()
       loglog(k,pk/pk[1])

       coef   = Linear_Fit_Line(log(k[len(k)/10:len(k)-1]),log(pk[len(k)/10:len(k)-1]/pk[1]))
       Gravity_obj.field.Power_Spec_n.append(coef[0])
       loglog(k,coef[1]*k**coef[0],label=r'$\propto k^{ %0.2f }$'%Gravity_obj.field.Power_Spec_n[i])

       legend()
       xlabel(r'$\omega$',fontsize = 20)
       ylabel(r'$P(\omega)$',fontsize = 20)
       title(r'$r = '+str(r[i])+r'$',fontsize = 20)
       fdir  = file_loc_save
       fname = 'Power_Spectrum%02d.pdf'%(i+1)
       print 'n = ', Gravity_obj.field.Power_Spec_n[i]
       print 'Saving plot', fname
       savefig(fdir+fname)

    rc('text',usetex=False)  

