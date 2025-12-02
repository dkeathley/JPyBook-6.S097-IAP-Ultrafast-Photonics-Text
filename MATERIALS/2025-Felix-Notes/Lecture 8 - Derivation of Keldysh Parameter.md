date:: 2025-01-30
tags:: #Lecture #Theory 


Here we derive the Kledysh parameter $\gamma$ which is a unitless number quantifying the transition from multiphoton emission to tunneling emission. This is very important in the field of strong-field physics and attosecond science. This parameter and the accompanying Keldysh theory for electron emission rates has been developed in the 60ties in Sowjet Russia. The idea of using strong optical fields was sparked by the invention of the laser, as incoherent light would never be able to reach the necessary field strength.

We consider the case of an electron in an atomic potential with ionisation energy $\Phi$ . The electric field distorts the potential landscape by bending the barrier towards one side. If the barrier thickness becomes finite we have a chance that electrons tunnels out through the barrier. However, under lower field conditions the chance of the electron absorbing multiple photons at once and escaping dominates the chance for tunneling and is a likelier pathway.


![[Pasted image 20250130103021.png]]


Citation: Zheltikov, A. M., Keldysh parameter, photoionization adiabaticity, and the tunneling time, Phys. Rev. A 94,4 2016.




The following derivation is a bit heuristic and there are more rigorous derivation coming to the same result.

We start by saying that the ionisation energy $\Phi$ can be expressed as an escape velocity/ kinetic energy $v_{t}$ , now called tunneling velocity.
$$
\Phi = \frac{1}{2} m_{e} v_{t}^2 
$$
We can define now also the width of the barrier $x_{t}$.
We know that the potential decreases by $\Delta V(x) = -qE_{0}x$, where $q$ is the charge of the electron and $E_{0}$ the peak electric field strength. Under the condition that,
$$
-\Phi = -qE_{0}x,
$$
we can find our barrier width,

$$
x_{t} = \frac{\Phi}{ q E_{0}}.
$$
Now with a velocity and a distance we can define a time!

The "tunneling time" $T$ is written as,
$$
T= \frac{x_{t}}{v_{t}} = \sqrt{ \frac{m\Phi}{2q^2E_{0}^2} }.
$$

Now we know that there is dynamical process going on with the electric field as it is not static in time but oscillating rapidly. So the question that we need to ask is, if the electron actually has enough time to tunnel out during one half oscillation of the electric field? 
Stating the explicit condition,
$$
T \ll \frac{T_{\lambda}}{2} \approx \frac{1}{2\omega}.
$$

Now writing out the inequality,
$$
\frac{1}{2\omega} \gg \sqrt{ \frac{m\Phi}{2q^2 E_{0}^2} },
$$
and rewriting i we find,
$$
1 \gg \omega \frac{\sqrt{ 2m\Phi}}{q^2 E_{0}^2}.
$$


Based on Keldysh theory one can also calculate the emission rates transitioning from multiphoton to tunneling, as shown below.



![[Keldysh.pdf]]