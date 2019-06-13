import bpy, os
from bpy.types import Operator, Menu
from bl_operators.presets import AddPresetBase

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)
addon_name = os.path.basename(os.path.normpath(directory))

class VIEW3D_MT_view_presets(Menu):
    bl_label = "View Presets"
    preset_subdir = "view_preset/view"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset


class AddPresetView(AddPresetBase, Operator):
    bl_idname = "screen.view_preset_add"
    bl_label = "Add View Preset"
    preset_menu = "VIEW3D_MT_view_presets"

    # variable used for all preset values
    preset_defines = [
        "screen = bpy.context.space_data",
        "s = bpy.context.space_data.shading",
        "scene = bpy.context.scene",
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
    preset_subdir = "view_preset/view"

def draw_master(self,context):
    prefs = bpy.context.preferences.addons[addon_name].preferences
    layout = self.layout

    if prefs.view == True:
        layout.popover(
            panel="VIEW3D_PT_view_presets",
            icon='PRESET',
            text="",
            #icon_value=view.icon_from_show_object_viewport
        )

class VIEW3D_PT_view_presets(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_label = "View Object Types"
    bl_ui_units_x = 12

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        view = context.space_data

        layout.label(text="Shading and Visibility Presets")
        row = layout.row(align=True)
        row.menu(VIEW3D_MT_view_presets.__name__, text=VIEW3D_MT_view_presets.bl_label)
        row.operator(AddPresetView.bl_idname, text="", icon='ADD')
        row.operator(AddPresetView.bl_idname, text="", icon='REMOVE').remove_active = True