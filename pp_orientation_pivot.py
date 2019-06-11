import bpy
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

class ORPIV_MT_draw_presets(Menu):
    bl_label = "Orientation and Pivot Presets"
    preset_subdir = "view_preset/orientation_and_pivot"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetOrpiv(AddPresetBase, Operator):
    bl_idname = "screen.orpiv_preset_add"
    bl_label = "Add Orientation and Pivot Preset"
    preset_menu = "ORPIV_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "scene = bpy.context.scene",
        ]

    # properties to store in the preset
    preset_values = [
        "scene.transform_orientation_slots[0].type",
        "scene.tool_settings.transform_pivot_point",
        "scene.tool_settings.use_transform_pivot_point_align",
        ]

    # where to store the preset
    preset_subdir = "view_preset/orientation_and_pivot"

def orpiv_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons['PresetterProfessional'].preferences
    layout = self.layout

    if prefs.orpiv == True:
        row = layout.row(align=True)
        row.menu(ORPIV_MT_draw_presets.__name__, text=ORPIV_MT_draw_presets.bl_label)
        row.operator(AddPresetOrpiv.bl_idname, text="", icon='ADD')
        row.operator(AddPresetOrpiv.bl_idname, text="", icon='REMOVE').remove_active = True