# This example is intended to show a simple targeted radiopherapy application

In this example, the geometry of the patient is defined from a CT and the source is defined as a radioactive ion source and using a SPECT image for the activity distribution.

A 3D dose actor records and save the absorbed dose per voxel of the geometry.

The different outputs can be read and analysed using the Python notebook gate_radiotherapy.ipynb

To run it:

`Gate mac/main.mac`

or with visualisation:

`Gate --qt mac/main.mac`

The outputs produced are saved in the folder output/
