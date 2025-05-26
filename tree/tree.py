# A simple tree structure to represent a product hierarchy

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child (self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Acer"))
    laptop.add_child(TreeNode("Asus"))

    cellphone = TreeNode("Cell phone")
    cellphone.add_child(TreeNode("Apple"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("MI"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    # print(root.children)
    