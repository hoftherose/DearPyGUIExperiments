class Attributes:
    def __init__(self):
        pass

    def GetName(self) -> str:
        pass

    def GetParams(self) -> dict[str, any]:
        pass

class Nodes:
    def __init__(self, name: str, attributes: [Attributes]):
        pass

    def GetName(self) -> str:
        pass

    def GetAttributes(self) -> list[Attributes]:
        pass

    def GetParams(self) -> list[Attributes]:
        pass
