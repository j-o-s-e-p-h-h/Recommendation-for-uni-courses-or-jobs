from data import industry_tech_data
class TreeNode:
    def __inint__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

Tech_Tree = TreeNode(None)
medicine = TreeNode(industry_tech_data["Medicine"])
agriculture = TreeNode(industry_tech_data["Agriculture"])
business = TreeNode(industry_tech_data["Business"])


Tech_Tree.add_child(medicine)
Tech_Tree.add_child(agriculture)
Tech_Tree.add_child(business)

