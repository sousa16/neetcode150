class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clones = [None] * 101

        def clone(original):
            if clones[original.val] is not None: # visited
                return clones[original.val]

            copy = Node(original.val)
            clones[original.val] = copy  # Mark visited before following edges

            for neighbor in original.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node)