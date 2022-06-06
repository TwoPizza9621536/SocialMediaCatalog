# SPDX-FileCopyrightText: 2022 The Social Media Catalog Contributors

# SPDX-License-Identifier: BSD-3-Clause
import json
import yaml


import dearpygui.dearpygui as dpg
from social_media_catalog.youtube import Playlist


from catalog_viewer import new_catalog_window


def save_file():
    # TODO: Implement a save dialog
    raise NotImplemented


def open_file(sender, app_data):
    with open(app_data["file_path_name"], mode="r", encoding="utf-8") as f:
        if app_data["file_name"].endswith(".json"):
            playlist_data = json.loads(f.read())
        elif app_data["file_name"].endswith((".yml", ".yaml")):
            playlist_data = yaml.load(f.read())
        else:
            # TODO: Handle error when file does not ends with json or yaml.
            raise NotImplemented

    new_catalog_window(Playlist.from_json(playlist_data))


def file_dialog(sender, app_data, user_data):
    if user_data == "open":
        callback = open_file
    elif user_data == "save":
        callback == save_file

    with dpg.file_dialog(directory_selector=False, callback=callback):
        dpg.add_file_extension(
            "JSON File (*.json){.json}",
            color=(245, 222, 25, 0),
            custom_text="[JSON]",
        )
        dpg.add_file_extension(
            "YAML Ain't Markup Language (*.yml *.yaml){.yml,.yaml}",
            color=(255, 232, 133, 0),
            custom_text="[YAML]",
        )
