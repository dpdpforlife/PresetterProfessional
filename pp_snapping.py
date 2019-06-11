import bpy
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

import os

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)

class SNAP_MT_draw_presets(Menu):
    bl_label = "Snapping Presets"
    preset_subdir = "view_preset/snapping"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetSnap(AddPresetBase, Operator):
    bl_idname = "screen.snap_preset_add"
    bl_label = "Add Snapping Preset"
    preset_menu = "SNAP_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "ts = bpy.context.scene.tool_settings",
        ]

    # properties to store in the preset
    preset_values = [
        "ts.snap_elements",
        "ts.use_snap_grid_absolute",
        "ts.snap_target",
        "ts.use_snap_align_rotation",
        "ts.use_snap_project",
        "ts.use_snap_peel_object",
        "ts.use_snap_translate",
        "ts.use_snap_rotate",
        "ts.use_snap_scale",
        ]

    # where to store the preset
    preset_subdir = "view_preset/snapping"

def snap_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons['PresetterProfessional'].preferences
    layout = self.layout

    if prefs.snap == True:
        row = layout.row(align=True)
        row.menu(SNAP_MT_draw_presets.__name__, text=SNAP_MT_draw_presets.bl_label)
        row.operator(AddPresetSnap.bl_idname, text="", icon='ADD')
        row.operator(AddPresetSnap.bl_idname, text="", icon='REMOVE').remove_active = True