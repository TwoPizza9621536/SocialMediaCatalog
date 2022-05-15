# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Greets the user when they open the viewer."""
from dearpygui import dearpygui as dpg


from new_dialog_window import new_dialog_window


def close_welcome():
    """Close the welcome dialog."""
    dpg.delete_item("welcome")
    new_dialog_window()


def page_one():
    """Display the first page of the help dialog."""
    dpg.set_value(
        "welcome dialog",
        "Welcome, this is a application that helps you view a list of "
        "videos, tweets or posts from a social media website.",
    )
    dpg.hide_item("back btn")
    dpg.set_item_callback("next btn", page_two)


def page_two():
    """Display the second page of the welcome dialog."""
    dpg.set_value(
        "welcome dialog",
        "This application uses third party libraries provided by social "
        "media sites and you are subjected to their ToS and Privacy "
        "Policy.",
    )
    dpg.show_item("back btn")
    dpg.set_item_callback("back btn", page_one)
    dpg.set_item_callback("next btn", page_three)


def page_three():
    """Display the third page of the welcome dialog."""
    dpg.set_value(
        "welcome dialog",
        "An Internet connection is require to download an catalog. Otherwise "
        "you can open files that contain catalog information.",
    )
    dpg.set_item_callback("back btn", page_two)
    dpg.set_item_callback("next btn", page_four)


def page_four():
    """Display the fourth page of the welcome dialog."""
    dpg.set_value(
        "welcome dialog",
        "On the next page, an window will open and you can choose a "
        "social media site to download a list of entries or open a file.",
    )
    dpg.set_item_callback("back btn", page_three)
    dpg.set_item_callback("next btn", close_welcome)


def welcome_window():
    """Create the welcome dialog."""
    with dpg.child_window(
        label="Welcome",
        tag="welcome",
        width=365,
        height=130,
        pos=(360, 300),
        menubar=True,
    ):
        dpg.add_text(tag="welcome dialog", wrap=360)
        with dpg.group(horizontal=True, pos=(0, 90)):
            dpg.add_separator()
            dpg.add_button(label="Back", tag="back btn", pos=(15, 100))
            dpg.add_button(label="Next", tag="next btn", pos=(315, 100))

        page_one()
