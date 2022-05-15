# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
"""Info about the application."""
from dearpygui import dearpygui as dpg


def about_window():
    """Show infomation about the view and credits."""
    with dpg.window(
        label="About Social Media Catalog Viewer",
        no_resize=True,
        min_size=(500, 300),
        pos=(200, 100),
    ):
        dpg.add_text("Social Media Catalog 1.0.0")
        dpg.add_separator()
        dpg.add_text("By Social Media Catalog contributors.")
        dpg.add_text(
            "Both Social Media Catalog and viewer is licensed under the BSD 3 "
            "Clause License, see LICENSE for more infomation.",
            wrap=650,
        )
        dpg.add_separator()
        dpg.add_text(
            "Social Media Catalog uses third party libraries and assets that "
            "are under different licenses, see ThirdPartyLibraries.txt for "
            "more infomation.",
            wrap=650,
        )
