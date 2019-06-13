import bpy, os
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)
addon_name = os.path.basename(os.path.normpath(directory))

class VIS_MT_draw_presets(Menu):
    bl_label = "Visibility Presets"
    preset_subdir = "view_preset/visibility"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetVisibility(AddPresetBase, Operator):
    bl_idname = "screen.visibility_preset_add"
    bl_label = "Add Visibility Preset"
    preset_menu = "VIS_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "screen = bpy.context.space_data"
        ]

    # properties to store in the preset
    preset_values = [
        "screen.show_object_viewport_mesh",
        "screen.show_object_select_mesh",
        "screen.show_object_viewport_curve",
        "screen.show_object_select_curve",
        "screen.show_object_viewport_surf",
        "screen.show_object_select_surf",
        "screen.show_object_viewport_meta",
        "screen.show_object_select_meta",
        "screen.show_object_viewport_font",
        "screen.show_object_select_font",
        "screen.show_object_viewport_grease_pencil",
        "screen.show_object_select_grease_pencil",        
        "screen.show_object_viewport_armature",
        "screen.show_object_select_armature",
        "screen.show_object_viewport_lattice",
        "screen.show_object_select_lattice",
        "screen.show_object_viewport_empty",
        "screen.show_object_select_empty",
        "screen.show_object_viewport_light",
        "screen.show_object_select_light",
        "screen.show_object_viewport_light_probe",
        "screen.show_object_select_light_probe", 
        "screen.show_object_viewport_camera",
        "screen.show_object_select_camera",
        "screen.show_object_viewport_speaker",
        "screen.show_object_select_speaker",
        ]

    # where to store the preset
    preset_subdir = "view_preset/visibility"

# Draw into an existing panel
def visibility_func(self, context):
    prefs = bpy.context.preferences.addons[addon_name].preferences
    layout = self.layout

    if prefs.vis == True:
        row = layout.row(align=True)
        row.menu(VIS_MT_draw_presets.__name__, text=VIS_MT_draw_presets.bl_label)
        row.operator(AddPresetVisibility.bl_idname, text="", icon='ADD')
        row.operator(AddPresetVisibility.bl_idname, text="", icon='REMOVE').remove_active = True