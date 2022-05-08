#!/usr/bin/env python
# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Main entry for the viewer"""
import sys


from dearpygui import dearpygui as dpg


from about_window import about_window
from new_dialog_window import new_dialog_window
from welcome_window import welcome_window


def setup_events():
    """Setup handlers for keyboard requests."""
    with dpg.handler_registry():
        dpg.add_key_down_handler(
            dpg.mvKey_N,
            callback=lambda: new_dialog_window()
            if dpg.is_key_down(dpg.mvKey_Control)
            else None
        )
        dpg.add_key_down_handler(
            dpg.mvKey_Q,
            callback=lambda: sys.exit(0)
            if dpg.is_key_down(dpg.mvKey_Control)
            else None
        )


def create_main_window():
    """Create main viewer window."""
    # TODO: Add a Table for its main functionality
    with dpg.window(tag="Main Window", width=1080, height=720, pos=(90, 20)):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(
                    label="New", shortcut="Ctrl+N", callback=new_dialog_window
                )
                dpg.add_menu_item(label="Save", shortcut="Ctrl+S")
                # TODO: Implement a save dialog
                dpg.add_menu_item(
                    label="Quit",
                    shortcut="Ctrl+Q",
                    callback=lambda: sys.exit(0)
                )

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="About", callback=about_window)

        welcome_window()


def main():
    """Entry point to setup DearPyGui."""
    dpg.create_context()
    dpg.create_viewport(title="Social Media Catalog Viewer")

    setup_events()
    create_main_window()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
