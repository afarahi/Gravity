from matplotlib.pyplot            import *
#from matplotlib                   import rc

#rc('text',usetex=False)
#rc('font',family='serif')

def Output_Plot_Construction(Gravity_object,i):

      if (Gravity_object.output.Pi_Field):
         clf()
         plot(Gravity_object.field.r,Gravity_object.field.Pi)
         ylim([-Gravity_object.output.Pi_Field_max,Gravity_object.output.Pi_Field_max])
#         xlabel(r'$r$',fontsize = 16)
#         ylabel(r'$\Pi$',fontsize = 16)
         fdir  = 'Output/saved_plots/Pi/'
         fname = 'Pi_frame%04d.'%(i/Gravity_object.output.Frame_time_step)+Gravity_object.output.Frame_format
         print 'Saving frame', fname
         savefig(fdir+fname)

      if (Gravity_object.output.Phi_Field):
         clf()
         plot(Gravity_object.field.r,Gravity_object.field.Phi)
         ylim([-Gravity_object.output.Phi_Field_max,Gravity_object.output.Phi_Field_max])
#         xlabel(r'$r$',fontsize = 16)
#         ylabel(r'$\Phi$',fontsize = 16)
         fdir  = 'Output/saved_plots/Phi/'
         fname = 'Phi_frame%04d.'%(i/Gravity_object.output.Frame_time_step)+Gravity_object.output.Frame_format
         print 'Saving frame', fname
         savefig(fdir+fname)

      if (Gravity_object.output.phi_Field):
         clf()
         plot(Gravity_object.field.r,Gravity_object.field.phi)
         ylim([-Gravity_object.output.phi_Field_max,Gravity_object.output.phi_Field_max])
#         xlabel(r'$r$',fontsize = 16)
#         ylabel(r'$\phi$',fontsize = 16)
         fdir  = 'Output/saved_plots/phi/'
         fname = 'phi_frame%04d.'%(i/Gravity_object.output.Frame_time_step)+Gravity_object.output.Frame_format
         print 'Saving frame', fname
         savefig(fdir+fname)

def Output_Data_Construction(Gravity_object,delta,A,file_loc = "Output/saved_data/"):
    f1 = open(file_loc+Gravity_object.output.Data_file_name, "a")
    Grid_size   = Gravity_object.Grid_size
    n_data_size = Gravity_object.output.Number_of_data_points
    n_co        = int(Grid_size/(n_data_size+1)) 
    for k in range(1,n_data_size+1):
       pp = n_co*k
       f1.write('%12.10f%16.10f%16.10f%16.10f%16.10f%16.10f%16.10f%16.10f\n'%(Gravity_object.field.time,Gravity_object.field.r[pp],Gravity_object.field.phi[pp],Gravity_object.field.Phi[pp],Gravity_object.field.Pi[pp],delta[pp],A[pp],Gravity_object.field.Ricci_Scalar[pp]))
    f1.close()

def Power_Spectrum_Data_Construction(Gravity_object,file_loc = "Output/Power_Spectrum_data/"):
    f1 = open(file_loc+Gravity_object.output.Power_Spectrum_file_name, "a")
    Grid_size   = Gravity_object.Grid_size
    n_data_size = Gravity_object.output.Power_Spectrum_points
    n_co        = int(Grid_size/(n_data_size+1)) 
    for k in range(1,n_data_size+1):
       pp = n_co*k
       f1.write('%14.12f%26.20f%26.20f\n'%(Gravity_object.field.time,Gravity_object.field.r[pp],Gravity_object.field.Ricci_Scalar[pp]))
    f1.close()

