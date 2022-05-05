# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Main entry for the viewer"""

from sys import exit


from dearpygui import dearpygui as dpg


def setup_events() -> None:
    with dpg.handler_registry():
        dpg.add_key_down_handler(
            dpg.mvKey_Q,
            callback=lambda: exit(0)
            if dpg.is_key_down(dpg.mvKey_Control)
            else None,
        )
        dpg.add_key_down_handler(dpg.mvKey_N, callback=selection_window)


def about_window() -> None:
    with dpg.window(
        label="About Social Media Catalog Viewer",
        no_resize=True,
        min_size=(500, 300),
        pos=(200, 100),
    ):
        dpg.add_text("Social Media Catalog 1.0.0")
        dpg.add_separator()
        dpg.add_text("By Samuel Wu and all Social Media Catalog contributes.")
        dpg.add_text(
            "Both Social Media Catalog and viewer is licensed under the BSD 3 "
            "Clause License, see LICENSE for more infomation.",
            wrap=650,
        )
        dpg.add_separator()
        dpg.add_text(
            "Social Media Catalog uses third party libraries that "
            "are under different licenses, see ThirdPartyLibraries.txt for "
            "more infomation.",
            wrap=650,
        )


def selection_window():
    #TODO: Add a create new window
    with dpg.window(label="New", pos=(450, 300)):
        dpg.add_button()
        dpg.add_button()
        dpg.add_button()


def welcome_window() -> None:
    def close_welcome():
        dpg.delete_item("intro")
        selection_window()

    def page_one():
        dpg.set_value(
            "welcome dialog",
            "Welcome, this is a application that helps you view a list of"
            "videos, tweets or posts from a social media website.",
        )
        dpg.hide_item("back btn")
        dpg.set_item_callback("next btn", page_two)

    def page_two():
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
        dpg.set_value(
            "welcome dialog",
            "This application requires an internet connection to download an "
            "catalog. Otherwise you can open files that contains the catalog.",
        )
        dpg.set_item_callback("back btn", page_two)
        dpg.set_item_callback("next btn", page_four)

    def page_four():
        dpg.set_value(
            "welcome dialog",
            "On the next page, an window will open and you can choose a "
            "social media site to download a list of entries or open a file.",
        )
        dpg.set_item_callback("back btn", page_three)
        dpg.set_item_callback("next btn", close_welcome)

    with dpg.window(
        label="Introduction",
        tag="intro",
        no_resize=True,
        no_move=True,
        width=365,
        height=110,
        pos=(450, 300),
        on_close=close_welcome,
    ):
        dpg.add_text(tag="welcome dialog", wrap=350)
        dpg.add_separator()
        dpg.add_button(label="Back", tag="back btn", pos=(15, 80))
        dpg.add_button(label="Next", tag="next btn", pos=(315, 80))
        page_one()


def create_main_window() -> None:
    #TODO: Add a Table for its main functionality
    with dpg.window(tag="Main Window"):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Save", shortcut="Ctrl+S")
                dpg.add_menu_item(
                    label="Quit", shortcut="Ctrl+Q", callback=lambda: exit(0)
                )

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="About", callback=about_window)


def main() -> None:
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
