from importlib import reload
import goo
from goo.division import *
from goo.handler import *

reload(goo)

goo.reset_modules()
goo.reset_scene()

celltype = goo.create_celltype("cellA", physics_on=True)
celltype.homo_adhesion_strength = 2000

cell = celltype.create_cell("cell", (1, 1, 0), scale=(1, 1, 1))

sim = goo.Simulator(celltypes=[celltype])
sim.toggle_gravity(False)

division_handler = TimeDivisionPhysicsHandler(BisectDivisionLogic, mu=51)
sim.add_handler(division_handler)
sim.add_handler(ForceUpdateHandler())
sim.add_handler(RemeshHandler(freq=5))

sim.run_simulation(start=1, end=250)