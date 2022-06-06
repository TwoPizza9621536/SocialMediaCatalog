# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Help the user to open or download a catalog"""
from dearpygui import dearpygui as dpg


from file_handler import file_dialog


def new_dialog_window():
    """Creates a new dialog window to create a new catalog to open a file."""
    if dpg.does_item_exist("welcome"):
        dpg.focus_item("welcome")
        return

    if dpg.does_item_exist("new"):
        dpg.focus_item("new")
        return

    with dpg.child_window(
        label="New",
        tag="new",
        parent="main_window",
        width=640,
        height=480,
        pos=(225, 150),
    ):
        dpg.add_text("")
        with dpg.group(horizontal=True):
            dpg.add_button(label="New Catalog")
            dpg.add_button(
                label="Open Catalog", callback=file_dialog, user_data="open"
            )

        dpg.add_button(
            label="Close",
            callback=lambda: dpg.delete_item("new"),
            pos=(585, 450),
        )
