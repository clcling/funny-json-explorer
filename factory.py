from abc import ABC, abstractmethod
from components import Leaf, Container


class StyleFactory(ABC):
    def __init__(self, container_icon, leaf_icon):
        self.container_icon = container_icon
        self.leaf_icon = leaf_icon
        self.style = None

    @abstractmethod
    def create_container(self, name, level=0):
        pass

    @abstractmethod
    def create_leaf(self, name, value=None):
        pass


class TreeStyleFactory(StyleFactory):
    def create_container(self, name, level=0):
        self.style = 'tree'
        return Container(name, level, self.style, self.container_icon)

    def create_leaf(self, name, value=None):
        self.style = 'tree'
        return Leaf(name, value, self.style, self.leaf_icon)


class RectangleStyleFactory(StyleFactory):
    def create_container(self, name, level=0):
        self.style = 'rectangle'
        return Container(name, level, self.style, self.container_icon)

    def create_leaf(self, name, value=None):
        self.style = 'rectangle'
        return Leaf(name, value, self.style, self.leaf_icon)

