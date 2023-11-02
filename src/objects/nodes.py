class Attributes:
    def __init__(self, attribute_type=0, **kwargs):
        self.attribute_type = attribute_type
        self.params = kwargs

    def GetAttributeType(self) -> str:
        return self.attribute_type

    def GetParams(self) -> dict[str, any]:
        return self.params
    
    def GenerateAttribute(self, dpg):
        with dpg.node_attribute(attribute_type=self.GetAttributeType()):
            dpg.add_input_text(**self.GetParams())

class Nodes:
    def __init__(self, name: str, attributes: list[Attributes], **kwargs):
        self.name = name
        self.attributes = attributes
        self.params = kwargs

    def GetName(self) -> str:
        return self.name

    def GetAttributes(self) -> list[Attributes]:
        return self.attributes

    def GetParams(self) -> dict[str, any]:
        return self.params

    def GenerateNode(self, dpg):
        with dpg.node(label=self.GetName()):
            for attr in self.GetAttributes():
                attr.GenerateAttribute(dpg)

            
