# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Creates the main window."""
import sys


import dearpygui.dearpygui as dpg


from about_window import about_window
from new_dialog_window import new_dialog_window
from file_handler import file_dialog
from welcome_window import welcome_window


def main_window():
    """The meat of the viewer."""
    with dpg.window(tag="main_window", width=1080, height=720, pos=(90, 20)):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(
                    label="New", shortcut="Ctrl+N", callback=new_dialog_window
                )
                dpg.add_menu_item(
                    label="Open",
                    shortcut="Ctrl+O",
                    callback=file_dialog,
                    user_data="open",
                )
                dpg.add_menu_item(
                    label="Save",
                    shortcut="Ctrl+S",
                    show=False,
                    user_data="save",
                )
                dpg.add_menu_item(
                    label="Quit",
                    shortcut="Ctrl+Q",
                    callback=lambda: sys.exit(0),
                )

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="About", callback=about_window)

        welcome_window()

        dpg.add_input_text(default_value="Search")

        with dpg.tab_bar(tag="main_viewer"):
            dpg.add_tab_button(label="X", trailing=True)
