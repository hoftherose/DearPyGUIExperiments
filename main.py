import dearpygui.dearpygui as dpg
from src.interfaces.nodes import Nodes, Attributes

dpg.create_context()

def link_callback(sender, app_data):
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)

def delink_callback(sender, app_data):
    dpg.delete_item(app_data)

def main():
    nodes = [Nodes("Node 1", [
                Attributes(attribute_type=dpg.mvNode_Attr_Output, label="F2", width=150),
            ]),
            Nodes("Node 2", [
                Attributes(attribute_type=dpg.mvNode_Attr_Output, label="F4", width=200),
            ])]
    with dpg.window(label="Tutorial", width=400, height=400):

        with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
            for node in nodes:
                node.GenerateNode(dpg)

    dpg.create_viewport(title='Custom Title', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()
