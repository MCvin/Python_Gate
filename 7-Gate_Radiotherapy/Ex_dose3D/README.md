# This example is intended to show the use of a patient CT and a 3D dose actor

The application is a simple GPS beam firing gammas at a patient defined with a voxelised image from a CT scan.

A 3D dose actor records and save the absorbed dose per voxel of the geometry.

The different outputs can be read and analysed using the Python notebook gate_radiotherapy.ipynb

To run it:

`Gate mac/main.mac`

or with visualisation:

`Gate --qt mac/main.mac`

The outputs produced are saved in the folder output/
