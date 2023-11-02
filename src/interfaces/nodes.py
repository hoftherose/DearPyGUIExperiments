class Attributes:
    def __init__(self, name, attribute_type=None, **kwargs):
        self.name = name
        self.attribute_type = attribute_type
        self.params = kwargs

    def GetName(self) -> str:
        return self.name

    def GetAttributeType(self) -> str:
        return self.attribute_type

    def GetParams(self) -> dict[str, any]:
        return self.params

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
