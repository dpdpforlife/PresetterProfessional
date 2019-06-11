import bpy
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

class GIZMO_MT_draw_presets(Menu):
    bl_label = "Gizmo Presets"
    preset_subdir = "view_preset/gizmo"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetGizmo(AddPresetBase, Operator):
    bl_idname = "screen.gizmo_preset_add"
    bl_label = "Add Gizmo Preset"
    preset_menu = "GIZMO_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "screen = bpy.context.space_data",
        "scene = bpy.context.scene",
        ]

    # properties to store in the preset
    preset_values = [
        "screen.show_gizmo_navigate",
        "screen.show_gizmo_tool",
        "screen.show_gizmo_context",
        "scene.transform_orientation_slots[1].type",
        "screen.show_gizmo_object_translate",
        "screen.show_gizmo_object_rotate",
        "screen.show_gizmo_object_scale",
        "screen.show_gizmo_empty_image",
        "screen.show_gizmo_empty_force_field",
        "screen.show_gizmo_light_size",
        "screen.show_gizmo_light_look_at",
        "screen.show_gizmo_camera_lens",
        "screen.show_gizmo_camera_dof_distance",
        ]

    # where to store the preset
    preset_subdir = "view_preset/gizmo"

def gizmo_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons['PresetterProfessional'].preferences
    layout = self.layout

    if prefs.giz == True:
        row = layout.row(align=True)
        row.menu(GIZMO_MT_draw_presets.__name__, text=GIZMO_MT_draw_presets.bl_label)
        row.operator(AddPresetGizmo.bl_idname, text="", icon='ADD')
        row.operator(AddPresetGizmo.bl_idname, text="", icon='REMOVE').remove_active = True