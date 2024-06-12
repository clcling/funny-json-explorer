from build import FunnyJsonExplorerBuilder


class FunnyJsonExplorer:
    def __init__(self, data, factory):
        self.data = data
        self.factory = factory
        self.root = None

    def _load(self):
        builder = FunnyJsonExplorerBuilder(self.factory)
        self.root = builder.build(self.data)

    def show(self):
        self._load()
        if self.root:
            i = 0
            for child in self.root.children:
                if i < len(self.root.children) - 1:
                    child.draw(False, 0, "├─ ")
                else:
                    child.draw(True, 0, "├─ ")
                i += 1


