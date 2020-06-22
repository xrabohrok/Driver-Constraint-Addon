'''
Copyright (C) 2016 Andreas Esau
andreasesau@gmail.com

Created by Andreas Esau

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Driver to Bone Constraint",
    "description": "This Operator lets you create a shape driver constraint to a bone with one single dialog operator. Quick and easy.",
    "author": "Andreas Esau",
    "version": (2, 0, 1,"Alpha"),
    "blender": (2, 80, 0),
    "location": "Operator Search -> Driver Constraint",
    "warning": "This addon is still in development.",
    "wiki_url": "https://github.com/ndee85/Driver-Constraint-Addon",
    "category": "Rigging" }


import bpy
from . import constraint_operator

# load and reload submodules
##################################



# register
##################################

import traceback

classes = (
    constraint_operator.DRIVER_CONSTRAINT_OT_create,
)

def add_to_specials(self,context):
    if len(bpy.context.selected_objects) > 0:
        self.layout.operator_context = "INVOKE_DEFAULT"
        self.layout.separator()
        op = self.layout.operator("object.create_driver_constraint",text="Driver Constraint",icon="DRIVER")
        op.mode = "DRIVER"
        if context.active_object.type == "ARMATURE" and len(context.selected_pose_bones) > 1:
            op = self.layout.operator("object.create_driver_constraint",text="Action Constraint",icon="ACTION")
            op.mode = "ACTION"
        
def add_pose_tools(self,context):
    if len(bpy.context.selected_objects) > 0:
        self.layout.operator_context = "INVOKE_DEFAULT"
        self.layout.separator()
        self.layout.label("Driver Tools:")
        op = self.layout.operator("object.create_driver_constraint",text="Driver Constraint",icon="DRIVER")
        op.mode = "DRIVER"
        if context.active_object != None and context.active_object.type == "ARMATURE" and len(context.selected_pose_bones) > 1:
            op = self.layout.operator("object.create_driver_constraint",text="Action Constraint",icon="ACTION")
            op.mode = "ACTION"

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_pose.append(add_to_specials)
    bpy.types.VIEW3D_MT_object.append(add_to_specials)
    bpy.types.VIEW3D_PT_context_properties.append(add_pose_tools)
    # bpy.types.VIEW3D_PT_tools_object.append(add_pose_tools)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_pose.remove(add_to_specials)
    bpy.types.VIEW3D_MT_object.remove(add_to_specials)
    bpy.types.VIEW3D_PT_context_properties.remove(add_pose_tools)
    # bpy.types.VIEW3D_PT_tools_object.remove(add_pose_tools)

