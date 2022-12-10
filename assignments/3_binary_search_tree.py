class Node:
    def __init__(self, key, value):
        """
        initializes the node
       key: root key

       """
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value):
        """
       key: append key
       :return: None
       """
        if key == self.key:
            return
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Node(key, value)
        else:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Node(key, value)
  

    def get(self, val):
        """
       val: value to search in tree 
       :return: the data asociated to that value
       """
        if val == self.key:
            #modify the return
            print(f" Get key: {self.key} , value: {self.value}")
            return self.value
        if val < self.key:
            if self.left:
                return self.left.get(val)
            else:
                return False
        else:
            if self.right:
                return self.right.get(val)
            else:
                return False  

    def print_keys(self):
        """
        print all key and values in order
       :return: None
       """
        if self.left:
            self.left.print_keys()
            print(self.right)
        print(f"key: {self.key}, value: {self.value}")
        if self.right:
            self.right.print_keys()
        return False

    def height(self, h=0):
        leftHeight = self.left.height(h + 1) if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftHeight, rightHeight)

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_' + (' ' * spacing)
        spacing = spacing - len(str(n)) + 1
        return str(n) + (' ' * spacing)


    
    def print(self):
        space=" "
        #print(f"{50*space} + {self.key}")
        height=tree.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        offset = int((width - 1) / 2)

        for depth in range(0, height + 1):
            if depth > 0:
                # print directional lines
                print(' ' * (offset + 1) + (' ' * (spacing + 2)).join(['/' + (' ' * (spacing - 2)) + '\\'] * (2 ** (depth - 1))))
            
            row = self.getNodesAtDepth(depth, [])
            print((' ' * offset) + ''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1

        print('/')

    
    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.key)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))

        if self.right:
            self.right.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))
        return nodes


#add first node
tree=Node("Vahe", 40)
#use insert to add more nodes
tree.insert("Thomas",41)
tree.insert("Anna",32)
tree.insert("Andrew",25)
tree.insert("William",20)
tree.insert("Daniel",20)
tree.insert("Serena",20)

#using the get function
#print("Search: ",tree.get("Vahe"))
print(tree.get("Vahe"))

tree.print()
#tree.print_keys()

#print(tree.height())
#tree.print()
#print(tree.getNodesAtDepth(0))
#print(tree.getNodesAtDepth(1))
#print(tree.getNodesAtDepth(2))
#print(tree.getNodesAtDepth(3))


