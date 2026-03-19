from data import industry_tech_data
class TreeNode:
    def __inint__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)
