# __init__.py

from .sort_groups import sort_groups  # Importing the sort_groups function from sort_groups.py
from .sort_group_children import reorder_groups
from .sort_layers import reorder_recursive
from qgis.core import QgsProject, QgsLayerTreeGroup

def classFactory(iface):
    return MyPlugin(iface)

class MyPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        # sort groups
        sort_groups()

        # sort group children
        root = QgsProject.instance().layerTreeRoot()
        # Recursively reorder groups
        for child in root.children():
            if isinstance(child, QgsLayerTreeGroup):
                reorder_groups(child)
        
        # Sort Layers
        reorder_recursive(root)
        

    def unload(self):
        pass
