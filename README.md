# blender-unity-scripts
Collection of scripts for my Blender to Unity3d workflow

## Rotate a Blender Object for Unity Export

By default Blender objects are exported to Unity with a x rotation of -90 deg, which is annoying most of the time. This script fixes it.

It rotates a Blender Object 90 degrees on X and it's mesh back -90 deg, so when you export it into Unity it will be upright with a rotation of 0,0,0.

### Usage

* Open script in Blenders Text editor and press 'Run Script'
* Select an object
* Press space and find the command 'Rotate Object for Unity3d' (just type unity and hit enter)
* See that you object is now rotated by +90 deg on X
