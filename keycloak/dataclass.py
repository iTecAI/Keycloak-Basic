import json

class Dataclass:
    EXCLUDE = ["content"]
    def __init__(self, content: dict) -> None:
        self.content = content
    
    def to_dict(self):
        propnames = [i for i in dir(self) if not i in self.EXCLUDE and not i.startswith("__") and not i == "EXCLUDE"]
        return {p: getattr(self, p) for p in propnames if not hasattr(getattr(self, p), "__call__")}
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
