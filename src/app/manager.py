import dearpygui.dearpygui as dpg
from ..objects.nodes import Nodes, Attributes

nodes = [Nodes("Node 1", [
            Attributes(attribute_type=dpg.mvNode_Attr_Output, label="F1", width=150),
        ]),
        Nodes("Node 2", [
            Attributes(attribute_type=dpg.mvNode_Attr_Output, label="F2", width=200),
        ])]

def create_node():
    nodes.append(Nodes("Node 3", [Attributes(attribute_type=dpg.mvNode_Attr_Output, label="F2", width=150),]))

class AppManager:
    def __init__(self):
        pass
    
    def SetupMenu(self):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Create Node", callback=create_node)
