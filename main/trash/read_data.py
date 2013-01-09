from xml.dom.minidom   import parseString
from Gravity_Utilities import getText

def read_data_initialize_method(file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('Initial_Condition_Method')[0]
    Method = getText(xmlTag.childNodes)
    return Method

def read_data_potential(file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('Potential')[0]
    p      = getText(xmlTag.childNodes)
    return p

def read_data_grid_size(file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag    = data.getElementsByTagName('Grid_size')[0]
    Grid_size = float(getText(xmlTag.childNodes))
    return Grid_size

def read_data_horizon_con(file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('A_min')[0]
    A_min  = float(getText(xmlTag.childNodes))
    return A_min

def read_data_i_max(file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('i_max')[0]
    i_max  = int(getText(xmlTag.childNodes)) 
    return i_max

def read_data_frame_time_step(file_name = 'parameters/output.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('n_frame')[0]
    n      = int(getText(xmlTag.childNodes))
    return n

def read_data_n_data_size(file_name = 'parameters/output.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName('n_data_size')[0]
    n      = int(getText(xmlTag.childNodes))
    return n

def read_data_frame_format(file_name = 'parameters/output.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data      = parseString(data_file)
    xmlTag    = data.getElementsByTagName('Frame_format')[0]
    f_format  = getText(xmlTag.childNodes)
    return f_format

