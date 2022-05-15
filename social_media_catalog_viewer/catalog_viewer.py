import dearpygui.dearpygui as dpg


def new_catalog_window(playlist):
    dpg.delete_item("new")

    with dpg.tab(label=playlist.playlist_name, parent="main_viewer"):
        with dpg.table():
            dpg.add_table_column(label="Video Title")
            dpg.add_table_column(label="Video Id")

            for i in range(3):
                with dpg.table_row():
                    for j in range(2):
                        dpg.add_text(f"Row{i} Column{j}")
