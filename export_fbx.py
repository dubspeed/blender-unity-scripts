import bpy
import os

def write_some_data(context, filepath, apply_unit_scale):
    path = os.path.dirname(filepath)
    
    bpy.ops.object.select_all(action='DESELECT')
            
    count = 0
    for object in bpy.data.objects:
        print ("processing " + object.name)
        object.select = True
        bpy.ops.export_scene.fbx (
            filepath = os.path.join(path, object.name + ".fbx"), 
            check_existing=False, 
            use_selection=True, 
            apply_unit_scale=apply_unit_scale
        );
        count += 1
        object.select = False

    print ('FBX-QUICK: Exported ' + str(count) + 'objects')
    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportSceneFBX(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_scene.fbx_quick" 
    bl_label = "Export Scene As FBX (quick)"

    # ExportHelper mixin class uses this
    filename_ext = ""

    filter_glob = StringProperty(
            default="",
            options={'HIDDEN'},
            maxlen=255,  # Max internal buffer length, longer would be clamped.
            )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    apply_unit_scale = BoolProperty(
            name="Apply unit scale",
            description="Apply unit scale",
            default=False,
            )
            
    def execute(self, context):
        return write_some_data(context, self.filepath, self.apply_unit_scale)

def menu_func_export(self, context):
    self.layout.operator(ExportSceneFBX.bl_idname, text="Export Scene as FBX")

def register():
    bpy.utils.register_class(ExportSceneFBX)
    bpy.types.INFO_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportSceneFBX)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()

    # test call
    #bpy.ops.export_scene.fbx_quick('INVOKE_DEFAULT')
