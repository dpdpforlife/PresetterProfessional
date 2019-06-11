# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "PresetterProfessional",
    "author" : "Dan Pool (dpdp)",
    "description" : "Quick View, Transform, and Snap Presets",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Viewport View, Transform and Snap Popups",
    "warning" : "Never smoke cigarettes around explosives!",
    "category" : "Generic"
}

import bpy
from . pp_visibility import VIS_MT_draw_presets, AddPresetVisibility, visibility_func
from . pp_gizmos import GIZMO_MT_draw_presets, AddPresetGizmo, gizmo_func
from . pp_overlays import OVERLAY_MT_draw_presets, AddPresetOverlay, overlay_func
from . pp_orientation_pivot import ORPIV_MT_draw_presets, AddPresetOrpiv, orpiv_func
from . pp_snapping import SNAP_MT_draw_presets, AddPresetSnap, snap_func

from bpy.types import Operator, AddonPreferences
from bpy.props import BoolProperty


class PPAddonPreferences(AddonPreferences):
    bl_idname = __name__

    vis: BoolProperty(
        name="Object Types Visibility",
        default=True,
    )

    giz: BoolProperty(
        name="Viewport Gizmos",
        default=True,
    )

    ol: BoolProperty(
        name="Viewport Overlays",
        default=True,
    ) 

    orpiv: BoolProperty(
        name="Orientation and Pivot Point",
        default=True,
    )

    snap: BoolProperty(
        name="Snapping",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Enable or Disable Preset Types")
        layout.prop(self, "vis")
        layout.prop(self, "giz")
        layout.prop(self, "ol")
        layout.prop(self, "orpiv")
        layout.prop(self, "snap")
        # layout.operator('object.qwer_prefs_update', text="Update")

classes = (
    OVERLAY_MT_draw_presets,
    AddPresetOverlay,
    GIZMO_MT_draw_presets,
    AddPresetGizmo,
    VIS_MT_draw_presets,
    AddPresetVisibility,
    ORPIV_MT_draw_presets,
    AddPresetOrpiv,
    SNAP_MT_draw_presets,
    AddPresetSnap
    )

def register():
    bpy.utils.register_class(PPAddonPreferences)
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_PT_overlay.prepend(overlay_func)
    bpy.types.VIEW3D_PT_gizmo_display.prepend(gizmo_func)
    bpy.types.VIEW3D_PT_object_type_visibility.prepend(visibility_func)
    bpy.types.VIEW3D_PT_transform_orientations.prepend(orpiv_func)
    bpy.types.VIEW3D_PT_snapping.prepend(snap_func)


def unregister():
    bpy.utils.unregister_class(PPAddonPreferences)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_PT_overlay.remove(overlay_func)
    bpy.types.VIEW3D_PT_gizmo_display.remove(gizmo_func)
    bpy.types.VIEW3D_PT_object_type_visibility.remove(visibility_func)
    bpy.types.VIEW3D_PT_transform_orientations.remove(orpiv_func)
    bpy.types.VIEW3D_PT_snapping.remove(snap_func)


if __name__ == "__main__":
    register()
