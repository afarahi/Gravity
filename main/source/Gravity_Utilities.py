from xml.dom.minidom   import parseString

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def read_data_string(tag_name,file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName(tag_name)[0]
    tag_name_value = getText(xmlTag.childNodes)
    return tag_name_value

def read_data_float(tag_name,file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName(tag_name)[0]
    tag_name_value = float(getText(xmlTag.childNodes))
    return tag_name_value

def read_data_int(tag_name,file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName(tag_name)[0]
    tag_name_value = int(getText(xmlTag.childNodes))
    return tag_name_value

def read_data_bool(tag_name,file_name = 'parameters/parameters.xml'):
    file      = open(file_name,'r')
    data_file = file.read()
    file.close()
    data = parseString(data_file)
    xmlTag = data.getElementsByTagName(tag_name)[0]
    tag_name_value = getText(xmlTag.childNodes)
    if (tag_name_value == "False" or tag_name_value == "false" or tag_name_value == "0"):
       return False
    else: 
        return True
