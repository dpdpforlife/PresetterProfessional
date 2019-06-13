import bpy, os
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)
addon_name = os.path.basename(os.path.normpath(directory))

class CURSOR_MT_draw_presets(Menu):
    bl_label = "3d Cursor Presets"
    preset_subdir = "view_preset/cursor"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetCursor(AddPresetBase, Operator):
    bl_idname = "screen.cursor_preset_add"
    bl_label = "Add 3d Cursor Preset"
    preset_menu = "CURSOR_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "c = bpy.context.scene.cursor",
        ]

    # properties to store in the preset
    preset_values = [
        "c.location",
        "c.rotation_euler",
        "c.rotation_quaternion",
        "c.rotation_axis_angle",
        "c.rotation_mode",
        ]

    # where to store the preset
    preset_subdir = "view_preset/cursor"

def cursor_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons[addon_name].preferences
    layout = self.layout

    if prefs.cursor == True:
        layout.label(text="3d Cursor Presets")
        row = layout.row(align=True)
        row.menu(CURSOR_MT_draw_presets.__name__, text=CURSOR_MT_draw_presets.bl_label)
        row.operator(AddPresetCursor.bl_idname, text="", icon='ADD')
        row.operator(AddPresetCursor.bl_idname, text="", icon='REMOVE').remove_active = True

def curpiv_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons[addon_name].preferences
    layout = self.layout

    if prefs.cursor == True:
        layout.label(text="3d Cursor Presets")
        row = layout.row(align=True)
        row.menu(CURSOR_MT_draw_presets.__name__, text=CURSOR_MT_draw_presets.bl_label)
        row.operator(AddPresetCursor.bl_idname, text="", icon='ADD')
        row.operator(AddPresetCursor.bl_idname, text="", icon='REMOVE').remove_active = True