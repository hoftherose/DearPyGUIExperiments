class Attributes:
    def __init__(self, name, **kwargs):
        self.name = name
        self.params = kwargs

    def GetName(self) -> str:
        return self.name

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
