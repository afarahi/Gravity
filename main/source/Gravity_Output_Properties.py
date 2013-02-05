from Gravity_Utilities  import read_data_string, read_data_float, read_data_int, read_data_bool 

class Output_parameters:

      def __init__(self):
         
         self.Output_status         = read_data_bool(tag_name = 'Output_Status',file_name = 'parameters/output.xml')
         self.Report_status         = read_data_bool(tag_name = 'Report_Status',file_name = 'parameters/output.xml')
         self.Power_Spectrum_status = read_data_bool(tag_name = 'Power_Spectrum_Status',file_name = 'parameters/output.xml')

         self.Frame_time_step       = read_data_int(tag_name = 'n_frame',file_name = 'parameters/output.xml')
         self.Number_of_data_points = read_data_int(tag_name = 'n_data_size',file_name = 'parameters/output.xml')
        
         #Output
         self.Pi_Field              = read_data_bool(tag_name = 'Pi_Field',file_name = 'parameters/output.xml')
         self.Pi_Field_max          = read_data_float(tag_name = 'Pi_Field_max',file_name = 'parameters/output.xml')
         self.Phi_Field             = read_data_bool(tag_name = 'Phi_Field',file_name = 'parameters/output.xml')
         self.Phi_Field_max         = read_data_float(tag_name = 'Phi_Field_max',file_name = 'parameters/output.xml')
         self.phi_Field             = read_data_bool(tag_name = 'phi_Field',file_name = 'parameters/output.xml')
         self.phi_Field_max         = read_data_float(tag_name = 'phi_Field_max',file_name = 'parameters/output.xml')
         self.Frame_format          = read_data_string(tag_name = 'Frame_format',file_name = 'parameters/output.xml')
         self.Data_file_name        = read_data_string(tag_name = 'Data_file_name',file_name = 'parameters/output.xml')
         
         #Power Spectrum
         self.Power_Spectrum_points = read_data_int(tag_name = 'Power_Spectrum_data_size',file_name = 'parameters/output.xml')
         self.Power_Spectrum_file_name = read_data_string(tag_name = 'Power_Spectrum_file_name',file_name = 'parameters/output.xml')
         self.Power_Spectrum_Setting_number = read_data_int(tag_name = 'Power_Spectrum_setting_number',file_name = 'parameters/output.xml')
                
         
