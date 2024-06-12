from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, container_icon, leaf_icon):
        self.container_icon = container_icon
        self.leaf_icon = leaf_icon
        self.style = None

    @abstractmethod
    def draw(self, flag, level, prefix=""):
        pass


class Leaf(Component):
    def __init__(self, name, value=None, style=None, leaf_icon=None):
        self.leaf_icon = leaf_icon
        self.name = name
        self.value = value
        self.style = style

    def draw(self, flag, level, prefix=""):
        icon = self.leaf_icon
        if self.style == 'tree':
            if self.value:
                print(f"{prefix}{icon}{self.name}: {self.value}")
            else:
                print(f"{prefix}{icon}{self.name}")
        elif self.style == 'rectangle':
            if self.value:
                print(
                    f"{prefix}{icon}{self.name}: {self.value} {'─' * (44 - len(self.name) - len(str(self.value)) - len(prefix) - 2)}┤")
            else:
                if prefix[0] == "└":
                    print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┘")
                else:
                    print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┤")


class Container(Component):
    def __init__(self, name, level=0, style=None, container_icon=None):

        self.container_icon = container_icon
        self.name = name
        self.level = level
        self.style = style
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def draw(self, flag, level=0, prefix=""):
        icon = self.container_icon
        if self.style == 'tree':
            if flag:
                prefix = "└─ "

            print(f"{prefix}{icon}{self.name}")

            if self.children:
                last_child = self.children[-1]

                for child in self.children[:-1]:
                    if flag == False:
                        prefix_next = "| " + "  " * (level) + "   ├─ "
                    else:
                        prefix_next = "  " * (level) + "   ├─ "
                    child.draw(flag, level + 1, prefix_next)

                if flag == True:
                    prefix_next = "  " * level + "   └─ "
                else:
                    prefix_next = "| " + "  " * (level) + "   └─ "
                last_child.draw(flag, level + 1, prefix_next)
        elif self.style == 'rectangle':
            if level == 0 and flag == False:
                print(f"┌─ {icon}{self.name} {'─' * (41 - len(self.name))}┐")
            else:
                print(f"{prefix}{icon}{self.name} {'─' * (44 - len(self.name) - len(prefix))}┤")

            if self.children:
                last_child = self.children[-1]

                for child in self.children[:-1]:
                    prefix_next = "|   " + "|" * (level) + " ├─ "
                    child.draw(False, level + 1, prefix_next)

                if flag == True:
                    prefix_next = "└─" + "─" * level + "───┴─ "
                else:
                    prefix_next = "|   " + "| " * (level) + "├─ "
                last_child.draw(False, level + 1, prefix_next)

