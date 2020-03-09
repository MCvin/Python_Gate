# This example is intended to show the use of Phase Space files

The application is a complete linac from https://gitlab.in2p3.fr/davidsarrut/gate-exercices/-/tree/master/linac

The first macro mac/main.mac is a complete simulation with the source from the primary source with a GPS beam.

The second one mac/main-write-PhS.mac is the same complete simulation but stores the particles in a phase space file before the jaws.

The third one mac/main-read-PhS.mac uses the phase space file produced by the second one as source. This speed up considerably the simulation.

The different outputs can be read and analysed using the Python notebook gate_radiotherapy.ipynb

To run it:

`Gate mac/main.mac`

or with visualisation:

`Gate --qt mac/main.mac`

The outputs produced are saved in the folder output/
