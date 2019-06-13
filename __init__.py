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
    "version" : (0, 0, 2),
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
from . pp_view import VIEW3D_MT_view_presets, VIEW3D_PT_view_presets, AddPresetView, draw_master
from . pp_shading import SHADE_MT_draw_presets, AddPresetShade, shade_func
from . pp_cursor import CURSOR_MT_draw_presets, AddPresetCursor, cursor_func, curpiv_func

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

    shade: BoolProperty(
        name="Shading",
        default=True,
    )

    view: BoolProperty(
        name="Shading and Overlays",
        default=True,
    )

    cursor: BoolProperty(
        name="3D Cursor in 3D Cursor Panel",
        default=True,
    )

    curpiv: BoolProperty(
        name="3D Cursor in Pivot Point Popover",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Enable or Disable Preset Types")
        box=layout.box()
        row=box.row()
        row.prop(self, "vis")
        row.prop(self, "giz")
        row=box.row()
        row.prop(self, "ol")
        row.prop(self, "shade")
        row=box.row()
        row.prop(self, "orpiv")
        row.prop(self, "snap")
        row=box.row()
        row.prop(self, "cursor")
        row.prop(self, "curpiv")
        row=layout.row()
        layout.label(text="The Shading and Overlays Panel Appears in the 3d View Header")
        box=layout.box()
        box.label(text="Use this presetter to recall Overlay and Shading settings in one place.")
        box.prop(self, "view")

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
    AddPresetSnap,
    VIEW3D_MT_view_presets,
    AddPresetView,
    VIEW3D_PT_view_presets,
    SHADE_MT_draw_presets,
    AddPresetShade,
    CURSOR_MT_draw_presets,
    AddPresetCursor,
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
    bpy.types.VIEW3D_HT_header.append(draw_master)
    bpy.types.VIEW3D_PT_shading.prepend(shade_func)
    bpy.types.VIEW3D_PT_view3d_cursor.append(cursor_func)
    bpy.types.VIEW3D_PT_pivot_point.prepend(curpiv_func)


def unregister():
    bpy.utils.unregister_class(PPAddonPreferences)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_PT_overlay.remove(overlay_func)
    bpy.types.VIEW3D_PT_gizmo_display.remove(gizmo_func)
    bpy.types.VIEW3D_PT_object_type_visibility.remove(visibility_func)
    bpy.types.VIEW3D_PT_transform_orientations.remove(orpiv_func)
    bpy.types.VIEW3D_PT_snapping.remove(snap_func)
    bpy.types.VIEW3D_HT_header.remove(draw_master)
    bpy.types.VIEW3D_PT_shading.remove(shade_func)
    bpy.types.VIEW3D_PT_view3d_cursor.remove(cursor_func)
    bpy.types.VIEW3D_PT_pivot_point.remove(curpiv_func)


if __name__ == "__main__":
    register()
