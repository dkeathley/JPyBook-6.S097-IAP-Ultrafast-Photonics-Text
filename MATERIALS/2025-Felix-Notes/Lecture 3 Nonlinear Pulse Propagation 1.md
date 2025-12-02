date:: {2025-01-12}
tags:: #Lecture #Theory #Fundamentals #Nonlinear


# General Introduction



![[NonlinearOptics.pdf]]



Nonlinearity in optics or rather the conversion of one photon into photons with different energies plays important roles across all optical sciences, from microscopy, quantum optics, telecommunication, spectroscopy or ultrafast optics.

We will give a brief introduction on this topic so you can have chance on understanding the basic phenomena and get a good starting position for your research. If you want to dive deeper in this topic of Nonlinear Optics we recommend the text book Nonlinear Optics from Robert Boyd.

So what do we mean by nonlinearity in the case of optics? In  the past we have discussed the role of dispersion, which is the linear response of a medium to the excitation of an optical wave. So whenever an optical wave propagates inside a medium we create a microscopic charge displacement of the electron away from it's ion.

{Draw picture of ion and electron with a spring connecting the two}

This displacement we call polarization $P(t)$. From Maxwells equations we can actually derive the inhomogeneous wave equation that describes this phenomenon.

$$
\nabla^2 E - \frac{1}{ c^2} \frac{\partial^2E}{\partial t^2} = \frac{1}{\epsilon_{0}c^2}  \frac{\partial^2P(t)}{\partial t^2} 
$$
If  we simply set $P(t)=0$ we get the case of vacuum under reasonable circumstances (At very large (not yet attained) intensities also the vacuum will show a polarizability).

Microscopically we can think about this case as the classical damped harmonic oscillator (also known as Lorentz oscillator) or a mass attached to a spring with friction. Whenever we drive the system away from the resonance with a certain frequency $\omega_{Driving}$ we get a response of the system that has a specific amplitude and phase different from the exciting wave. So effectively we get our LTI system again.
Writing the Polarization as $P(t) = \epsilon_{0}  \chi^{(1)}E(t)$ we get a linear Polarization response to the driving field $E(t)$. 
So plugging this into the above equation we get,
$$
\nabla^2 E - \frac{1}{ c^2} \frac{\partial^2E}{\partial t^2} = \frac{1}{\epsilon_{0}c^2}  \frac{\partial^2\epsilon_{0}  \chi^{(1)}E(t)}{\partial t^2}$$
$$
\nabla^2 E - \frac{1}{ c^2}\frac{\partial^2E}{\partial t^2} - \frac{1}{ c^2}\chi^{(1)} \frac{\partial^2E}{\partial t^2} = 0 \\

$$

$$
\nabla^2 E - \frac{1}{ c^2}(1+ \chi^{(1)} )\frac{\partial^2E}{\partial t^2} = 0 \\

$$
With expressing $(1+\chi^{(1)}) = n$, we finally arrive at the homogeneous case again,
$$
\nabla^2 E - \frac{n^2}{ c^2}\frac{\partial^2E}{\partial t^2} = 0 \\

$$
In the frequency domain this equation becomes even easier to handle,

$$
(\nabla^2  + \frac{n^2 \omega^2}{ c^2})\tilde{E}(\omega) = 0 \\
$$
--- 
Leave out:

 With the solution to this diff. equation being a forward or a backward traveling wave,
 $$
 \left( \nabla - \frac{jn\omega}{c} \right)\left( \nabla + \frac{jn\omega}{c} \right)\tilde{E}(\omega) = 0
 $$
---


 So we get our solution $E(\omega) = \tilde{A}(\omega)e^{\pm jn\omega z/c   }$ and also we can remember that $\frac{n\omega}{c} = k$.
Ending up ultimately with,

$$
E(t,z)=A(t) e^{j(\omega t \pm kz) }.
$$
Before we have a look at nonlinearity we need to look at an important property of the dispersion effects. For any propagation we have of course a moving wave/pulse, but when considering dispersion we mostly care about relative changes. How does the envelope change, while neglecting the general change of its position in space.

{Draw picture of pulse short than one that is dispersed and displaced}

However, we can resolve that problem easily by looking at the spectral phase and its Taylor expansion properties ,
$$
\phi (\omega) = \phi_{0} + \phi_{1}\omega + \frac{1}{2} \phi_{2}\omega^2 +\frac{1}{6} \phi_{3}\omega^3 + \dots,
$$
with the zeroth order term being the carrier phase shift, the first order the group delay, the second the chirp and the third order the third order dispersion.
No solve our problem of having a moving pulse we can simply neglect the zeroth and the first order term and we are left with only relative changes as specifically the chirp.

Coming back to our wave function the term $k(\omega)z = \phi(\omega)$, with $k(\omega)$ being explicitly frequency dependent. So when looking at $k(\omega)$ we can also look at its taylor expansion,
$$
\phi (\omega) = \left( k_{0}+k_{1}\omega +\frac{1}{2} k_{2}\omega^2  + \dots \right)z,
$$
simply use $k_{2}$ to just describe the effects of chirp and not the movement of the pulse or higher order dispersion. I want to note that we can recover the movement by considering the group velocity at the carrier wave and move the envelope artificially.

$t$ will be the in the following in the moving frame.

This gives us the propagation equation,

$$
 \frac{\partial E(t,z)}{\partial z} = -\frac{jk_{2}}{2}  \frac{\partial^2 E(t,z)}{\partial t^2}
$$
At this point it is also useful to only consider the envelope and remove the carrier frequency.


Now we can play another trick with the Fourier transform to get rid of the envelope and remove the carrier frequency which is a linear phase in time and corresponds to a shift in frequency!

$$
E(t) = A(t) e^{j\omega_{0} t} \rightarrow A(t)
$$
$$
\tilde{E}(\omega) = A(\omega-\omega_{0}) \rightarrow A(\omega)
$$

To determine the rate of change of the envelope with propagation in z, we can look at the derivative of the envelope,
$$
\frac{\partial A(t,z)}{\partial z} = -\frac{jk_{2}}{2}  \frac{\partial^2 A(t,z)}{\partial t^2}.
$$
Of course we in principle this equation we have solved before already and the solution to the wave equation also fulfills this one by definition. But it will become more important in the following considering nonlinear propagation.

### Nonlinear Propagation

However, any real system only behaves linear for a certain range of driving strength. When driven sufficiently strong the force of the ion pulling on the electron changes.

Under the assumption that this still only perturbative we can write $P(t)$ as its Taylor expansion, 
$$
P(t) =\epsilon_{0}(\chi^{(1)} E(t) + \chi^{(2)} E(t)^2 +\chi^{(3)} E(t)^3 + \dots + \chi^{(n)} E(t)^n).
$$
These nonlinear terms are the source terms in our wave equation creating new frequency components!
$$
\nabla^2 E - \frac{n^2}{ c^2}\frac{\partial^2E}{\partial t^2} = \frac{1}{\epsilon_{0}c^2}  \frac{\partial^2P_{NL}(t)}{\partial t^2} \\

$$



The second order polarization term is causing effects like second harmonic generation, difference frequency generation or spontaneous parametric down conversion. 

The third order term is causing effects like third harmonic generation, Kerr lensing, Raman scattering, or self phase modulation.


For nonlinear propagation we will ignore the second order term and focus on what is called self phase modulation. Self phase modulation originates from the third order nonlinarity which brings an intensity dependent  phase.

We can express,
$$
P^{(3)}(t) = \epsilon_{0} \chi^{(3)}E(t)^3 =  \epsilon_{0} \chi^{(3)}A(t)^3 \cos(\omega t)^3 =   \epsilon_{0} \chi^{(3)}A(t)^3 (\frac{1}{4}\cos(3\omega t) + \frac{3}{4} \cos(\omega t)),
$$
excluding the $\cos(3\omega t)$ term which THG, we are left with the intensity dependent phase,
$$
P^{(3)}(t) =  \epsilon_{0} \chi^{(3)}A(t)^3  \frac{3}{4} \cos(\omega t) =  \frac{3\epsilon_{0}}{4} \chi^{(3)}\|E(t)\|^2  E(t).
$$

Plugging this into our nonlinear wave equation we get,
$$
\nabla^2 E - \frac{n^2}{ c^2}\frac{\partial^2E}{\partial t^2} = \frac{3}{4c^2} \chi^{(3)} \frac{\partial^2(\|E(t)\|^2  E(t))}{\partial t^2}, 
$$


We are omitting the derivation steps here to yield the nonlinear Schroedinger equation, but encourage looking into the  reference ( Thibault Voumard, Desy Thesis 2024).

To come back to our propagation equation we simply take the heuristic approach and assume that the SPM is can be described by a nonlinear phase,
$$
\frac{\partial A(t,z)}{\partial z} = - j\gamma \vert A(t,z)\vert^2 A(t,z).
$$

Here we can easily guess the solution for a propagation starting from $z=0$ and write,

$$
A(t,z) = e^{-j\gamma\vert A(t,0)\vert^2 z}A(t,0).
$$

Now, we can put together everything including dispersion and SPM, and we end up with the following differential equation called NLSE,

$$
\frac{\partial A(t,z)}{\partial z} =\frac{jk_{2}}{2}  \frac{\partial^2 A(t,z)}{\partial t^2} - j\gamma \vert A(t,z)\vert^2 A(t,z).
$$


