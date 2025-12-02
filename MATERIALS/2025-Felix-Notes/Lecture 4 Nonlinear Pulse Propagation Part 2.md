date:: {2025-01-15}
tags:: #Lecture #Simulation #Nonlinear #Optics


We stopped in the last lecture at the Nonlinear Schroedinger Equation NLSE 

$$
\frac{\partial A(t,z)}{\partial z} = \frac{jk_{2}}{2}  \frac{\partial^2 A(t,z)}{\partial t^2} - j\gamma \vert A(t,z)\vert^2 A(t,z).
$$
or equivalently while also substituting $D_{2}= \frac{k_{2}}{2}$,
$$
j\frac{\partial A(t,z)}{\partial z} =-D_{2}  \frac{\partial^2 A(t,z)}{\partial t^2} + \gamma \vert A(t,z)\vert^2 A(t,z).
$$

We due this substitution as $D_{2}$ is a common parameter called the dispersion parameter.
To look some more at the properties of the NLSE  we can look what the intensity dependent phase creates in the pulse.


```tikz


\begin{document}

\begin{tikzpicture}[domain=-3:3, scale=3]
    % Gaussian Function
    \begin{scope}[shift={(0,6)}]
        \draw[very thin,color=gray] (-3.2,-0.2) grid (3.2,1.2);
        \draw[->] (-3.5,0) -- (3.5,0) node[right] {$t$};
        \draw[->] (0,-0.2) -- (0,1.5) node[above] {$I(t)$};
        \draw[color=blue,thick] plot[samples=200] (\x,{exp(-\x*\x)}) 
            node[below right] {Intensity};
    \end{scope}

% Neg Gaussian Function
    \begin{scope}[shift={(0,3)}]
        \draw[very thin,color=gray] (-3.2,-1.2) grid (3.2,1.2);
        \draw[->] (-3.5,0) -- (3.5,0) node[right] {$t$};
        \draw[->] (0,-1.5) -- (0,1.5) node[above] {$\phi(t)$};
        \draw[color=blue,thick] plot[samples=200] (\x,{-exp(-\x*\x)}) 
            node[below right] {Phase};
    \end{scope}


    % First Derivative
    \begin{scope}[shift={(0,0)}]
        \draw[very thin,color=gray] (-3.2,-0.8) grid (3.2,0.8);
        \draw[->] (-3.5,0) -- (3.5,0) node[right] {$t$};
        \draw[->] (0,-0.8) -- (0,0.8) node[above] {$f(t)$};
        \draw[color=red,thick] plot[samples=200] (\x,{2*\x*exp(-\x*\x)}) 
            node[below right] {Frequency Change };
    \end{scope}

\end{tikzpicture}

\end{document}
```


  We discussed in the last lecture that there are stationary solution to the NLSE and that these are called solitons. The condition of an unchanging wavepacket requires that $\frac{\partial A(t,z)}{\partial z} = -j\beta A(t,z)$, where $\beta$ is just an accumulated  phase shift but the overall envelope is unchanging.
  
  This means such a condition in the NLSE,
$$
j \frac{\partial A(t,z)}{\partial z}=-D_{2}  \frac{\partial^2 A(t,z)}{\partial t^2} + \gamma \vert A(t,z)\vert^2 A(t,z),
$$
is our stationary soliton! What this effectively means is that the chirp and the nonlinear phase are perfectly balanced.
A solution to this equation is the sech pulse,
$$
A_{s}(t,z) = A_{0}\cdot \text{sech}\left( \frac{t}{\tau}\right) e^{-j\beta z},
$$
with the nonlinear phase shift $\beta z$ of the soliton,
$$
\beta z = \frac{\gamma}{2} A_{0}^2 z.
$$

Now can start solving the equation above by using the ansatz $A(t,z) = A_{0}~ \text{sech}\left( \frac{t}{\tau} \right) e^{-j\beta z}$ and inserting it into the NLSE.
We start by looking at the individual terms

$$
\frac{\partial^2 A_{s}(t,z)}{\partial t^2} = A_{0} \frac{\text{sech}\left( \frac{t}{\tau} \right)e^{-j\beta z} }{\tau^2} \left( - \text{sech}\left( \frac{t}{\tau} \right)^2 + \tanh^2\left( \frac{t}{\tau} \right) \right) = A_{0}\frac{\text{sech}\left( \frac{t}{\tau} \right)e^{-j\beta z} }{\tau^2} \left( 1 - 2\tanh^2\left( \frac{t}{\tau} \right) \right) 
$$

$$
\gamma \vert A(t,z)\vert^2 A(t,z) = \gamma ~ A_{0}^2 \text{sech}\left( \frac{t}{\tau} \right)^2 A_{0}\text{sech}\left( \frac{t}{\tau} \right) e^{-j\beta z} = \gamma ~ A_{0}^2\left( 1-\tanh^2\left( \frac{t}{\tau} \right) \right) A_{0}\text{sech}\left( \frac{t}{\tau} \right) e^{-j\beta z} 
$$


$$
\frac{\partial A(t,z)}{\partial z} = -j\beta ~A_{0}\text{sech}\left( \frac{t}{\tau} \right) e^{-j \beta z} 
$$
With all the individual terms we can spell out the final equation,

$$
-j^2 \beta A_{s}(t,z) = - D_{2}\frac{A_{s}(t,z) }{\tau^2} \left( 1 - 2\tanh^2\left( \frac{t}{\tau} \right) \right) + \gamma A_{0}^2~ \left( 1-\tanh^2\left( \frac{t}{\tau} \right) \right) A_{s}(t,z).
$$


$$
\beta = - D_{2}\frac{1 }{\tau^2} \left( 1 - 2\tanh^2\left( \frac{t}{\tau} \right) \right) + \gamma A_{0}^2~ \left( 1-\tanh^2\left( \frac{t}{\tau} \right) \right) 
$$

Now we assume that $\frac{D_{2}}{\tau^2}$ is two times smaller than $\gamma A_{0}^2$  and substitute it with $\alpha$ and $\frac{\alpha}{2}$,
$$
\beta = - \frac{\alpha}{2} \left( 1 - 2\tanh^2\left( \frac{t}{\tau} \right) \right) + \alpha ~ \left( 1-\tanh^2\left( \frac{t}{\tau} \right) \right) 
$$

$$
\beta = \alpha \left( -\frac{1}{2} + 1\tanh^2\left( \frac{t}{\tau} \right) + 1 - \tanh^2\left( \frac{t}{\tau} \right) \right) 
$$

$$
\beta = \frac{\alpha}{2} = \frac{\gamma A_{0}}{2}
$$

Now we have our two conditions for the soliton to be stationary. 
Which are $2\frac{D_{2}}{\tau^2} = \gamma A_{0}^2$ and $\beta = \frac{\gamma A_{0}}{2}$

With this we can also define the characteristic dispersion length $L_{D}$ in the linear case and the $L_{NL}$ for the nonlinear dispersion,
$$
\begin{align} \\
L_{D} = \frac{\tau^2}{2D_{2}} \\
L_{NL} = \frac{1}{\gamma A_{0}^2} 
\end{align} \\
$$
For the soliton case these are equal $L_{D} = L_{NL}$.



*Showing here the soliton solutions including also the higher order solutions.*




### Simulating the Nonlinear Schroedinger Equation

To numerically solve the NLSE we employ what is called the Split-Step Method which uses the fact that the linear and nonlinear terms can be solved separately and more efficiently in the Fourier domain for the dispersion and the time domain for the nonlinear term.

So to start deriving our split-step approach we can express our NLSE with operators, as we are for exampled used to in quantum mechanics,

$$
j \frac{\partial A(t,z)}{\partial z}=-D_{2}  \frac{\partial^2 A(t,z)}{\partial t^2} + \gamma \vert A(t,z)\vert^2 A(t,z) = (\hat{D} + \hat{N})A(t,z).
$$
The general solution to this case is to express equation as a multiplication with an exponential with the operators in its exponent,

$$
A(t,z+\Delta z) = e^{-j(\hat{D}+\hat{N})\Delta z} A(t,z).
$$
This exponential we can be split up under the cost of a small error, scaling with $\Delta z$. This can be found using the Baker-Campbell-Hausdorff formula and is due to the operators $\hat{D}$ and $\hat{N}$ not commuting,
$$
A(t,z+\Delta z) \approx e^{-j\hat{D}\Delta z}e^{-j\hat{N}\Delta z} e^{-j[\hat{D}, \hat{N}]\Delta z^2/2} A(t,z).
$$
From this we simply neglect the correction term under the cost of the error and write our solution by solving first in time and then in the Fourier domain and finally inverse transforming back to time,

$$
A(t,z+\Delta z) \approx \mathcal{F}^{-1}\left( e^{-jD_{2}\omega^2\Delta z} \mathcal{F}\left( e^{-j\gamma\vert A(t,z)\vert^2\Delta z} A(t,z)\right)\right).
$$
However a quadratic error can be very costly requiring very fine steps for our numerical simulation.
The computationally costly step of this equation is the Fourier transform as the simple multiplication is cheap. To exploit this fact we can employ the Strang splitting, which performs half steps in the time domain, similar to for example the Leap-Frog algorithm. This can also be derived from the Baker-Campbell-Hausdorff formula and results in error that scales with $\Delta z^3$.
The resulting procedure is written as the following,

$$
A(t,z+\Delta z) \approx e^{-j \gamma\vert A(t,z)\vert^2\Delta z/2}~\mathcal{F}^{-1}\left( e^{-jD_{2}\omega^2\Delta z}~ \mathcal{F}\left( e^{-j \gamma\vert A(t,z)\vert^2\Delta z/2} A(t,z)\right)\right).
$$
Splitting in this way we perform the same amounts of Fourier transforms and one more multiplication but gaining precision of an error only scaling with $\Delta z^3$.

