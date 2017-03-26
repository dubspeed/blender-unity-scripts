import math
import bmesh
import bpy
import mathutils

def main(context):
    o =  bpy.context.object
    bm = bmesh.new()   # create an empty BMesh
    bm.from_mesh(o.data)   # fill it in from a Mesh

    cent = (0, 0, 0)
    rot = mathutils.Matrix.Rotation(math.radians(-90.0), 4, 'X')

    o.rotation_euler=(math.radians(90.0), 0.0, 0.0)
    bmesh.ops.rotate(		
        bm,                      # BMESH object
        cent   = cent,      # Rotation pivot point 
        matrix = rot,            # Rotation value
        verts  = bm.verts,   # What verts to rotate
        space  = o.matrix_world  # Rotate in object world space
    )

    bm.to_mesh(o.data)
    bm.free() 


class RotateUnity3d(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rotate_unity3d"
    bl_label = "Rotate Object for Unity3d"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(RotateUnity3d)


def unregister():
    bpy.utils.unregister_class(RotateUnity3d)


if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.object.rotate_unity3d()



