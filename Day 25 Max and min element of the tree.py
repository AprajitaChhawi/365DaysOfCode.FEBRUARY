#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def findMax(root):
    if root==None:
        return
    stack=[]
    node=root
    stack.append(node)
    maxelement=0
    while len(stack)!=0:
        node=stack.pop()
        if maxelement<node.data:
            maxelement=node.data
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return maxelement
    '''
    :param root: root of the given tree.
    :return: max 
    
    '''
    #code here
    
def findMin(root):
    if root==None:
        return
    stack=[]
    node=root
    stack.append(node)
    minelement=999990
    while len(stack)!=0:
        node=stack.pop()
        if minelement>node.data:
            minelement=node.data
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return minelement
    '''
    :param root: root of the given tree.
    :return: min 
    
    '''
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)
    def Insert(self,parent, child,dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list

        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        
        
        print(findMax(tree.root),findMin(tree.root))

# } Driver Code Ends
