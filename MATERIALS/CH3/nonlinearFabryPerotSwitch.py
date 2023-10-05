import numpy as np
import meep as mp

# --- Simulation Settings ---

#Save tag
save_prefix = 'Ey-slab-w-chi3-75.0-lambda-0.0-HR'

#Source settings
fcen=1/1.55
df = 0.2
source_height = 1.4
amp=2.0

chi3 = 75.0
eps = 12

#Rate to sample at monitors in time
# -- Specified as how many samples per period to use
# -- Based off of highest frequency in source
time_sample_rate = 10


#Width of the slab
length_lambda = 0.0
slab_width = (1/fcen)*length_lambda/np.sqrt(eps)
slab_height = mp.inf

#Spatial resolution
resolution = 100

#Size of the cell in x and y
sx=slab_width + 1.0
sy=1.4

#Thickness of PML (perfectly matched layers)
# -- Avoids reflections from boundaries
dpml=0.5

 
#wg_width = mp.inf

# --- Simulation Setup ---
sX = sx + 2.0*dpml
sY = sy + 2.0*dpml

#Create the simulation cell
cell = mp.Vector3(sX,sY,0)

#Add in the waveguide.
# -- Specify epsilon and chi3 for the medium
geometry = [mp.Block(mp.Vector3(slab_width,slab_height, mp.inf),
                     center=mp.Vector3(),
                     material=mp.Medium(epsilon=eps, chi3=chi3))]

# Add in a gaussian source with polarization in z
sources = [mp.Source(mp.GaussianSource(frequency=fcen, fwidth=df),
                     component=mp.Ey,
                     center=mp.Vector3(-sx/2.0, 0),
                     size=mp.Vector3(0, source_height),
                     amplitude=amp)]

#Add in the pml layers
pml_layers = [mp.PML(dpml)]

#Create the simulation object:
sim = mp.Simulation(cell_size=cell,
                    boundary_layers=pml_layers,
                    geometry=geometry,
                    sources=sources,
                    resolution=resolution)

#Add in a monitor for the fields
monitor =  mp.Volume(center=mp.Vector3(0.0,0.0),
                     size=mp.Vector3(sx, sy))

#Run the simulation and save fields at the monitor at the time_sample_rate
sim.run(mp.in_volume(monitor,
                     mp.to_appended(save_prefix,
                                    mp.at_every(1.0/(fcen + 0.5*df)/time_sample_rate,
                                                mp.output_efield_y))),
        until=mp.stop_when_fields_decayed(dt=10, c=mp.Ey, pt=mp.Vector3(sx*0.5,0), decay_by=1e-3))

#until=1.2*sx*np.sqrt(eps)
