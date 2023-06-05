class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        
        # Inverte os nós da subárvore esquerda
        left = self.invertTree(root.left)
        # Inverte os nós da subárvore direita
        right = self.invertTree(root.right)
        
        # Inverte os ponteiros dos nós da árvore
        root.left = right
        root.right = left
        
        return root