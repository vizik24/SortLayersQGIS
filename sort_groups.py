from qgis.core import QgsProject, QgsLayerTree, QgsLayerTreeGroup, QgsLayerTreeLayer

def sort_groups():
    ''' This function gets the children of the root node in the layer treePosition
        and extracts the group names, then sorts them alphabetically and inserts groups
        according to their sorted position, before deleting the originals'''
    root = QgsProject.instance().layerTreeRoot()

    # Extract group names and sort them
    groups = []
    for child in root.children():
        if isinstance(child, QgsLayerTreeGroup):
            groups.append(child)
    sorted_groups = sorted(groups, key=lambda x: x.name().replace('_', '').lower())

    # Reorder groups in the layer tree
    for index, group in enumerate(sorted_groups):
        group.parent().insertChildNode(index, group.clone())

    # Remove original groups
    for group in groups:
        group.parent().removeChildNode(group)

sort_groups()
