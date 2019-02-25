import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 30), ylim=(-0.7, 0.7))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially to generate the animation
def animate(i):
    
    ### Once PIB_Func and PIB_En are defined, the following
    ### code can be used to plot the time-evolution of an energy eigenfunction

    ### Define x-grid - this will be for a particle in a box of length L=30 atomic units (Bohr radii)
    ### We will represent the function with 1000 grid points (dx = 30/1000)
    x = np.linspace(0, 30, 1000)

    ### Imaginary unit i
    ci = 0.+1j

    ### Creates an array of values of energy eigenstate 3 evaluated at 1000 x-values between 0 and L=30 atomic units
    psi_1 = PIB_Func(x, 3, 30.)
    ### Get energy of that state
    E1  = PIB_En(3, 30.)
    ### Evaluate time-dependent part of current state at current time
    ft1  = PIB_Time(3, 30, i)
    ### Create an empty array of 1000 complex numbers that can be filled with the time-dependent wavefunction values
    psi_t = np.zeros(1000,dtype=complex)


    psi_t = ft1*psi_1
    psi_t_star = np.conj(psi_t)

    #psi_t = psi_t + np.sqrt(1./3)*psi_2*np.exp(-ci*E3*i)
    y = np.real(psi_t)
    z = np.imag(psi_t)
    p = np.real(psi_t_star * psi_t)
    #y = np.sin(2*np.pi*x/2)*np.cos(i/4.)
    line.set_data(x, y)
    return line,

#### give a list of x-values between 0 and L, the length L, and the quantum numbner n
#### return a list of psi_n values between 0 and L
def PIB_Func(x, n, L):
    psi_n = np.sqrt(2./L)*np.sin(n*np.pi*x/L)
    ### Write code here... need to define argument to Sin 
    ### Normalization constant
    ### and need to define function and return it
    return psi_n


### Give a quantum number n and a length L, return the energy 
### of an electron in a box of length L in state n
def PIB_En(n, L):
    En = (n*n * np.pi*np.pi)/(2*L*L)
    return En

### Give the quantum number and the current time, evaluate the time-dependent part of the wavefunction at current time
### and return its value
def PIB_Time(n, L, t):
    E = PIB_En(n, L)
    ci = 0.+1j
    phi_n_t = np.exp(-1*ci*E*t)
    ### Write code here to define phi_n_t
    return phi_n_t
# call the animator.  blit=True means only re-draw the parts that have changed.

anim = animation.FuncAnimation(fig, animate, init_func=init,
	                               frames=10000, interval=20, blit=True)
#anim.save('PIB_EE3.mp4', fps=15, extra_args=['-vcodec', 'libx264'])
          
plt.show()
