def Report_parameters(Gravity_object):
    S = r'''

\section{Parameters}

The following parameters are used in this run, \\

Field proparties:
\begin{verbatim}
  Geometry  = ''' + Gravity_object.Geometry_type_name + r'''
  Cosmological constant  = ''' + str(Gravity_object.Cosmological_cosntant) + r'''
  Potential = ''' + Gravity_object.Potential_type_name + r'''
\end{verbatim}

Initial Conditions:
\begin{verbatim}
  Initial Condition = ''' + Gravity_object.Initial_Condition_type_name + r'''
\end{verbatim}

Numerical method:
\begin{verbatim}
  Solver = ''' + Gravity_object.Solver_type_name + r'''
  Grid size = ''' + str(Gravity_object.Grid_size) + r'''
\end{verbatim}

Ending conditions:
\begin{verbatim}
  Horizon condition (A_min) = ''' + str(Gravity_object.A_min) + r'''
  Maximum number of iteration = ''' + str(Gravity_object.Max_interation) + r'''
\end{verbatim}

'''
    return S

