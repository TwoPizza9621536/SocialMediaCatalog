import dearpygui.dearpygui as dpg


def new_catalog_window(playlist):
    dpg.delete_item("new")

    with dpg.tab(label=playlist.playlist_name, parent="main_viewer"):
        with dpg.table():
            dpg.add_table_column(label="Video Title")
            dpg.add_table_column(label="Video Id")

            # TODO: Add videos to the table
            for k, v in playlist.videos:
                with dpg.table_row():
                    for _j in range(2):
                        dpg.add_text(f"")
