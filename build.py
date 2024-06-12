

class FunnyJsonExplorerBuilder:
    def __init__(self, factory):
        self.factory = factory

    def build(self, data, level=0):
        if isinstance(data, dict):
            container = self.factory.create_container("", level)
            for key, value in data.items():
                container.add_child(self.build_node(key, value, level + 1))
            return container
        elif isinstance(data, list):
            container = self.factory.create_container("", level)
            for index, item in enumerate(data):
                container.add_child(self.build_node(f"[{index}]", item, level + 1))
            return container

    def build_node(self, name, value, level=0):
        if isinstance(value, dict) or isinstance(value, list):
            container = self.factory.create_container(name, level)
            if isinstance(value, dict):
                for key, val in value.items():
                    container.add_child(self.build_node(key, val, level + 1))
            else:
                for index, item in enumerate(value):
                    container.add_child(self.build_node(f"[{index}]", item, level + 1))
            return container
        else:
            return self.factory.create_leaf(name, value)
