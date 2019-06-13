import bpy, os
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)
addon_name = os.path.basename(os.path.normpath(directory))

class SHADE_MT_draw_presets(Menu):
    bl_label = "Shading Presets"
    preset_subdir = "view_preset/Shading"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetShade(AddPresetBase, Operator):
    bl_idname = "screen.shade_preset_add"
    bl_label = "Add Shading Preset"
    preset_menu = "SHADE_MT_draw_presets"

    # variable used for all preset values
    preset_defines = [
        "s = bpy.context.space_data.shading",
        ]

    # properties to store in the preset
    preset_values = [
        "s.type",
        "s.use_scene_lights",
        "s.use_scene_world",
        "s.studio_light",
        "s.studiolight_rotate_z",
        "s.studiolight_background_alpha",
        "s.light",
        "s.use_world_space_lighting",
        "s.color_type",
        "s.background_type",
        "s.background_color",
        "s.show_backface_culling",
        "s.show_xray",
        "s.xray_alpha",
        "s.show_shadows",
        "s.shadow_intensity",
        "s.show_cavity",
        "s.use_dof",
        "s.show_object_outline",
        "s.object_outline_color",
        "s.show_specular_highlight",
        "s.wireframe_color_type",
        "s.show_xray_wireframe",
        "s.xray_alpha_wireframe",
        ]

    # where to store the preset
    preset_subdir = "view_preset/shading"

# Draw into an existing panel
def shade_func(self, context):
    layout = self.layout

    prefs = bpy.context.preferences.addons[addon_name].preferences
    layout = self.layout

    if prefs.shade == True:
        row = layout.row(align=True)
        row.menu(SHADE_MT_draw_presets.__name__, text=SHADE_MT_draw_presets.bl_label)
        row.operator(AddPresetShade.bl_idname, text="", icon='ADD')
        row.operator(AddPresetShade.bl_idname, text="", icon='REMOVE').remove_active = True