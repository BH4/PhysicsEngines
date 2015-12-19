#test simulation
from simulation import simulation


sim=simulation()

sim.setTmax(10)

sim.addParticle()

sim.includeForce('EarthG')
sim.includeOutput('PosYvsTime','VelYvsTime')

sim.run()
