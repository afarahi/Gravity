from numpy import loadtxt

def Report_Results(Gravity_object):
    if Gravity_object.field.Horizon :
       S1= r''' In this run the black hole is formed at time, $ t = ''' + str(Gravity_object.field.time) + r'''$. And the field stops its evolution. '''
    else:
       S1=r''' In this run the black hole was not formed and the field stoped its evolution at time, $ t = ''' + str(Gravity_object.field.time) + r'''$. There maybe two resoan why black hole did not form. First the number of iteration was not enough to get the balck hole so by increasing the nuber of iteration once can go furthur in time and see if the black holes forms. Second errors grow and become dominant so the code failed to predict the behavoiur of field. For solving this problem one may want to increase the grid size, in this run grid size of, $n = ''' + str(Gravity_object.Grid_size) + r''' $, is used. There is another possibilities to improve the numerical solution, change the solver to something more accurate, in this run solver ''' + Gravity_object.Solver_type_name + r''' is used. '''

    S = r'''
\section{Results}
\subsection{Final Plots}

Graphs \ref{fig:R-Pi}, \ref{fig:R-phi}, and \ref{fig:R-Phi} show results of $\Pi$, $\phi$, and $\Phi$ vs. r, respectively, at finalt time, t =  ''' + str(Gravity_object.field.time) + r'''.

\begin{figure}[hbt]
 \centering
 \includegraphics[width=12cm]{./Report/PivrR.pdf}
 \caption{Plot of $\Pi$ vs. r at final time.}
 \label{fig:R-Pi}
\end{figure}

\begin{figure}
 \centering
 \includegraphics[width=12cm]{./Report/phivrR.pdf}
 \caption{Plot of $\phi$ vs. r at final time.}
 \label{fig:R-phi}
\end{figure}

\begin{figure}
 \centering
 \includegraphics[width=12cm]{./Report/PhivrR.pdf}
 \caption{Plot of $\Phi$ vs. r at final time.}
 \label{fig:R-Phi} 
\end{figure}

\subsection{Black hole formation}

One of the aim of \grv\ is to study the black hole fomration of different fields in \AdS\ geometry. Once the black hole forms the field stops its evolution. It is suggested that all fields forms a black hole at sometimes during their evolution, and it is the universal feature of all fields in \AdS\ . The time of fomation of black hole depends on the amplititude and shape of initial wave, the geometry of space, potential, and the field choice. Because it is not possible to run the code for ever an end condition implimented in the code to stop the evolution of field after some number of iteration. In this run the number of iteration is defined, $i_{\max}  = ''' + str(Gravity_object.Max_interation) + r'''$. \\
For black hole formation the code checks the value of $A$ at each point, at each time. Theoretically once $A = 0$ it means that the black hole fomed so the condition $A_{\min}$ is defined to check whether the black hole is formed or not. One should choose something close to zero, but independently, by changing the $A_{\min}$ need to make sure that the condition do not affect the result. In this run $A_{\min} = ''' + str(Gravity_object.A_min) + r'''$ . \\

'''  + S1
 
    if Gravity_object.output.Power_Spectrum_status :
       (t, r, x) = loadtxt("./Output/Power_Spectrum_data/"+Gravity_object.output.Power_Spectrum_file_name, unpack=True, comments = '#')
       S += r'''\subsection{Power Spectrum}
    Assuming the evolution of each point in space following the power low in Fourier space, one can compute the power of power spectrum for large frequencies with finding the best fit line in log-log plot. Here it is assumed assume,

    \begin{equation}
       r(k) \propto k^n
    \end{equation}

    In this run the power, $n$ , is computed for ''' + str(Gravity_object.output.Power_Spectrum_points) + r''' points.

    \begin{center}
    \begin{tabular}{ | l | l | l | p{5cm} |}
    \hline
    r      & n\\ \hline '''
       for i in range(Gravity_object.output.Power_Spectrum_points):
           S += str(r[i]) +  r'''&''' + str(Gravity_object.field.Power_Spec_n[i])  + r'''\\ \hline 
'''
       S += r'''
    \end{tabular}
    \end{center}
'''
    return S

