class BinTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_trav(subtree):
    if subtree is not None:
        print(subtree.data)
        pre_order_trav(subtree.left)
        pre_order_trav(subtree.right)

def in_order_trav(subtree):
    if subtree is not None:
        in_order_trav(subtree.left)
        print(subtree.data)
        in_order_trav(subtree.right)

def post_order_trav(subtree):
    if subtree is not None:
        post_order_trav(subtree.left)
        post_order_trav(subtree.right)
        print(subtree.data)


if __name__  ==  "__main__":
    tree = BinTreeNode(1)
    tree1 = BinTreeNode(2)
    tree2 = BinTreeNode(3)
    tree3 = BinTreeNode(4)
    tree4 = BinTreeNode(5)
    tree5 = BinTreeNode(6)
    tree6 = BinTreeNode(7)
    
    tree.left = tree1
    tree.right = tree2
    tree1.left = tree3
    tree1.right = tree5
    tree2.left = tree6
    tree2.right = tree4
   

    print('inorder: ')
    in_order_trav(tree)
    print('preorder :')
    pre_order_trav(tree)
    print('postorder: ')
    post_order_trav(tree)

