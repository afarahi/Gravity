from numpy import polyfit

def Linear_Fit_Line(x,y):
    coef = polyfit(x,y,1)
    return coef
