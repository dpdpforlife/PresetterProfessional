import bpy
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase


class OVERLAY_MT_draw_presets(Menu):
    bl_label = "Overlay Presets"
    preset_subdir = "view_preset/overlay"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetOverlay(AddPresetBase, Operator):
    bl_idname = "screen.overlay_preset_add"
    bl_label = "Add Overlay Preset"
    preset_menu = "OVERLAY_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "screen = bpy.context.space_data"
        ]

    # properties to store in the preset
    preset_values = [
        "screen.overlay.show_floor",
        "screen.overlay.show_ortho_grid",
        "screen.overlay.show_axis_x",
        "screen.overlay.show_axis_y",
        "screen.overlay.show_axis_z",
        "screen.overlay.grid_scale",
        "screen.overlay.grid_subdivisions",
        "screen.overlay.show_text",
        "screen.overlay.show_cursor",
        "screen.overlay.show_annotation",
        "screen.overlay.show_extras",
        "screen.overlay.show_bones",
        "screen.overlay.show_relationship_lines",
        "screen.overlay.show_motion_paths",
        "screen.overlay.show_outline_selected",
        "screen.overlay.show_object_origins",
        "screen.overlay.show_object_origins_all",
        "screen.overlay.show_wireframes",
        "screen.overlay.wireframe_threshold",
        "screen.overlay.show_face_orientation",
        ]

    # where to store the preset
    preset_subdir = "view_preset/overlay"

# Draw into an existing panel
def overlay_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons['PresetterProfessional'].preferences
    layout = self.layout

    if prefs.ol == True:
        row = layout.row(align=True)
        row.menu(OVERLAY_MT_draw_presets.__name__, text=OVERLAY_MT_draw_presets.bl_label)
        row.operator(AddPresetOverlay.bl_idname, text="", icon='ADD')
        row.operator(AddPresetOverlay.bl_idname, text="", icon='REMOVE').remove_active = True