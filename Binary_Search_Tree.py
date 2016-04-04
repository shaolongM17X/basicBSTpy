class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      # TODO complete Node initialization

  def __init__(self):
    self._root = None
    # TODO complete initialization

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    pass # TODO replace pass with your implementation

  def remove_element(self, value):
    # Remove the value specified from the tree. Select the minimum
    # value to the from the right as this element's replacement.
    # Take note of when to move a node reference and when to replace
    # the value in a node instead. It is not necessary to return the 
    # value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    pass # TODO replace pass with your implementation

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    pass # TODO replace pass with your implementation

  def pre_order(self):
    # Construct an return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    pass # TODO replace pass with your implementation

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    pass # TODO replace pass with your implementation

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    pass # TODO replace pass with your implementation

  def __str__(self):
    return self.in_order()

