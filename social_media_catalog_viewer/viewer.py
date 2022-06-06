#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Main entry for the viewer"""
import os
import sys
from inspect import getsourcefile


import dearpygui.dearpygui as dpg


from file_handler import file_dialog
from main_window import main_window
from new_dialog_window import new_dialog_window


def setup_assets():
    """Setup any assets like images and fonts for the viewer to use."""
    appdir = os.path.dirname(getsourcefile(lambda: 0))
    with dpg.font_registry():
        dpg.bind_font(dpg.add_font(f"{appdir}/assets/Cantarell-VF.otf", 16))

    # with dpg.texture_registry():
    #     dpg.add_static_texture()


def setup_events():
    """Setup handlers for keyboard requests."""
    with dpg.handler_registry():
        if dpg.is_key_down(dpg.mvKey_Control):
            dpg.add_key_press_handler(dpg.mvKey_N, callback=new_dialog_window)
            dpg.add_key_press_handler(
                dpg.mvKey_O, callback=file_dialog, user_data="open"
            )
            dpg.add_key_press_handler(
                dpg.mvKey_Q, callback=lambda: sys.exit(0)
            )


def main():
    """Entry point to setup DearPyGui."""
    dpg.create_context()
    dpg.create_viewport(title="Social Media Catalog Viewer")

    setup_assets()
    setup_events()
    main_window()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
