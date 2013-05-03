from Gravity_Report_title           import Report_title
from Gravity_Report_introduction    import Report_introduction
from Gravity_Report_Results         import Report_Results
from Gravity_Report_parameters      import Report_parameters
from Gravity_Report_Acknowledgments import Report_Acknowledgments
from Gravity_Report_bib             import Report_bib

def Report_File(Gravity_object):

    content= Report_title() \
            +Report_introduction()\
            +Report_Results(Gravity_object)\
            +Report_parameters(Gravity_object)\
            +Report_Acknowledgments()\
            +Report_bib()
 
    f1 = open('Report/report.tex','w')
    f1.write(content)
    f1.close

