Painting Meshes

Activate Texture Packer Plugin in Blender

https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/UV/TextureAtlas

* all objects into 1 blend file
* Create Geometry
* Unwrap in UVSlot 1
* Paint each object , every object has 1 material

Texture Atlas Bakeing

Goto render settings
Create Texture Atlas and add all objects for that atlas, Auto unwrap to UV channel 2

Select each object and adjust the UVSettings
￼
Bake: Select TextureAtlas in UV editor, as active texture, select all objects, press “Bake” buttons (Bake Mode: Texture)

Save Image

Unity
Swap UVs in Unity Import settings (to use TextureAtlas Channel as Diffuse)
Activate Generate Lightmap UV (Lightmap Uvs get generated in the Channel 1)

