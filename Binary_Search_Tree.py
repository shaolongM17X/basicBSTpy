class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None
      self._height = 0

  def __init__(self):
    self._root = None

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self._root = self._insert_rec(self._root, value)


  def _insert_rec(self, node, value):
    if node is None:
      newNode = self._BST_Node(value)
      newNode._height = 1
      return newNode
    value_at_node = node._value
    if value < value_at_node:
      node._left = self._insert_rec(node._left, value)
    elif value > value_at_node:
      node._right = self._insert_rec(node._right, value)


    node._height = self._getCorrectedHeight(node)
    return node

  def _getCorrectedHeight(self, node):
    if node._left is not None:
      height_left = node._left._height
    else:
      height_left = 0
    if node._right is not None:
      height_right = node._right._height
    else:
      height_right = 0
    return 1 + max(height_left, height_right)

  def remove_element(self, value):
    # Remove the value specified from the tree. Select the minimum
    # value to the from the right as this element's replacement.
    # Take note of when to move a node reference and when to replace
    # the value in a node instead. It is not necessary to return the 
    # value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self._root = self._remove_rec(self._root, value)

  def _remove_rec(self, node, value):
    if node is None:
      return node
    value_at_node = node._value
    if value < value_at_node:
      node._left = self._remove_rec(node._left, value)
    elif value > value_at_node:
      node._right = self._remove_rec(node._right, value)
    else:
      # if this node has two children
      if node._left is not None and node._right is not None:
        node._value = self._find_min(node._right)
        node._right = self._remove_rec(node._right, node._value)
      elif node._left is not None:
        # this node has only left child
        return node._left
      else:
        # this node has only right child or no child
        return node._right
    node._height = self._getCorrectedHeight(node)
    return node

  # Helper method used in remove_rec to find the minimum value in the right subtree of a node having two children
  def _find_min(self, node):
    while node._left is not None:
      node = node._left
    return node._value

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    str = "[ "
    str += self._in_order_rec(self._root)
    if self._root is not None:
      str = str[:-2]
    else:
      return "[ ]"
    str += " ]"
    return str

  def _in_order_rec(self, node):
    if node is None:
      return ""
    result = ""
    value_left = self._in_order_rec(node._left)
    if value_left != "":
      result += value_left
    result += str(node._value) + ", "
    value_right = self._in_order_rec(node._right)
    if value_right != "":
      result += value_right
    return result

  def pre_order(self):
    # Construct an return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self._root is None:
      return "[ ]"
    else:
      str = "[ "
      str += self._pre_order_rec(self._root)
      str = str[:-2]
      str += " ]"
      return str

  def _pre_order_rec(self, node):
    if node is None:
      return ""
    result = ""
    result += str(node._value) + ", "
    value_left = self._pre_order_rec(node._left)
    if value_left != "":
      result += value_left
    value_right = self._pre_order_rec(node._right)
    if value_right != "":
      result += value_right
    return result


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self._root is None:
      return "[ ]"
    else:
      str = "[ "
      str += self._post_order_rec(self._root)
      str = str[:-2]
      str += " ]"
      return str
  def _post_order_rec(self, node):
    if node is None:
      return ""
    result = ""
    value_left = self._post_order_rec(node._left)
    if value_left != "":
      result += value_left
    value_right = self._post_order_rec(node._right)
    if value_right != "":
      result += value_right
    result += str(node._value) + ", "
    return result

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    return 0 if self._root is None else self._root._height


  def __str__(self):
    return self.in_order()
