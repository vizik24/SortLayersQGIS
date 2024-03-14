def reorder_layers_within_groups(node):
    # Extract layers and sort them
    layers = []
    for child in node.children():
        if isinstance(child, QgsLayerTreeLayer):
            layers.append(child)
    sorted_layers = sorted(layers, key=lambda x: x.name().replace('_', '').lower())

    # Reorder layers in the group
    for index, layer in enumerate(sorted_layers):
        node.insertChildNode(index, layer.clone())

    # Remove original layers
    for layer in layers:
        node.removeChildNode(layer)

# Usage:
root = QgsProject.instance().layerTreeRoot()

# Recursively reorder layers within groups
def reorder_recursive(node):
    for child in node.children():
        if isinstance(child, QgsLayerTreeGroup):
            reorder_recursive(child)
            reorder_layers_within_groups(child)

# Start reordering from the root
reorder_recursive(root)

# Print the sorted layer and group names (optional)
def print_layers_and_groups(node, indent=0):
    for child in node.children():
        if isinstance(child, QgsLayerTreeLayer):
            print('  ' * indent + '- Layer:', child.name())
        elif isinstance(child, QgsLayerTreeGroup):
            print('  ' * indent + '- Group:', child.name())
            print_layers_and_groups(child, indent + 1)

# Print the sorted layer and group names
print_layers_and_groups(root)
