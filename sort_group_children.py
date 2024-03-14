from qgis.core import QgsProject, QgsLayerTree, QgsLayerTreeGroup, QgsLayerTreeLayer

def reorder_groups(group):
    # Extract subgroups and sort them
    subgroups = []
    for child in group.children():
        if isinstance(child, QgsLayerTreeGroup):
            subgroups.append(child)
    sorted_subgroups = sorted(subgroups, key=lambda x: x.name().replace('_', '').lower())

    # Reorder subgroups in the group
    for index, subgroup in enumerate(sorted_subgroups):
        group.insertChildNode(index, subgroup.clone())

    # Remove original subgroups
    for subgroup in subgroups:
        group.removeChildNode(subgroup)

    # Recursively reorder subgroups
    for subgroup in sorted_subgroups:
        reorder_groups(subgroup)

# Usage:
root = QgsProject.instance().layerTreeRoot()

# Recursively reorder groups
for child in root.children():
    if isinstance(child, QgsLayerTreeGroup):
        reorder_groups(child)

# Print the sorted group names (optional)
def print_group_names(group):
    for child in group.children():
        if isinstance(child, QgsLayerTreeGroup):
            print_group_names(child)
        elif isinstance(child, QgsLayerTreeLayer):
            print(child.name())


    
    
    
    
    
    
    

