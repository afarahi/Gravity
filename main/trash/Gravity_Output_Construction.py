from matplotlib.pyplot            import *
from Gravity_AdS4_RH_Construction import *
#from matplotlib                   import rc

#rc('text',usetex=True)
#rc('font',family='serif')

def Output_Plot_Construction(Gravity_object,x,Phi_new,Pi_new,phi_new):

      if (Gravity_object.output.Pi_Field):
         clf()
         plot(x,Pi_new)
         ylim([-Gravity_object.output.Pi_Field_max,Gravity_object.output.Pi_Field_max])
#         xlabel(r'$r$',fontsize = 16)
#         ylabel(r'$\Pi$',fontsize = 16)
         fdir  = 'saved_plots/Pi/'
         fname = 'Pi_frame%04d.'%(i/Gravity_object.output.Frame_time_step)+Gravity_object.output.Frame_format
         print 'Saving frame', fname
         savefig(fdir+fname)

      if (Gravity_object.output.Phi_Field):
         clf()
         plot(x,Phi_new)
         ylim([-Gravity_object.output.Phi_Field_max,Gravity_object.output.Phi_Field_max])
#         xlabel(r'$r$',fontsize = 16)
#         ylabel(r'$\Phi$',fontsize = 16)
         fdir  = 'saved_plots/Phi/'
         fname = 'Phi_frame%04d.'%(i/Gravity_object.output.Frame_time_step)+Gravity_object.output.Frame_format
         print 'Saving frame', fname
         savefig(fdir+fname)

      if (Gravity_object.output.phi_Field):
         print Gravity_object.output.phi_Field
         clf()
         plot(x,phi_new)
         ylim([-Gravity_object.output.phi_Field_max,Gravity_object.output.phi_Field_max])
#         xlabel(r'$r$',fontsize = 16)
#         ylabel(r'$\phi$',fontsize = 16)
         fdir  = 'saved_plots/phi/'
         fname = 'phi_frame%04d.'%(i/Gravity_object.output.Frame_time_step)+Gravity_object.output.Frame_format
         print 'Saving frame', fname
         savefig(fdir+fname)

def Output_Data_Construction(Gravity_object,x,Phi_new,Pi_new,phi_new,Ricci,delta,A,time):
    f1 = open("saved_data/"+Gravity_object.output.Data_file_name, "a")
    Grid_size   = Gravity_object.Grid_size
    n_data_size = Gravity_object.output.Number_of_data_points
    n_co        = int(Grid_size/(n_data_size+1)) 
    for k in range(1,n_data_size+1):
       pp = n_co*k
       f1.write('%12.10f%16.10f%16.10f%16.10f%16.10f%16.10f%16.10f%16.10f\n'%(time,x[pp],phi_new[pp],Phi_new[pp],Pi_new[pp],delta[pp],A[pp],Ricci[pp]))
    f1.close()

