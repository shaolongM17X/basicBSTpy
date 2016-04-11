import unittest

from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

  def setUp(self):
    self._Binary_Search_Tree = Binary_Search_Tree()
    
  #testing empty tree
  
  def test_empty_binary_search_trees(self):
    self.assertEqual('[ ]' ,str(self._Binary_Search_Tree))
    
  def test_height_empty_tree(self):   
    self.assertEqual(0, self._Binary_Search_Tree.get_height())
    
  def test_inorder_empty_tree(self):
    self.assertEqual('[ ]' ,str(self._Binary_Search_Tree.pre_order()))
    
  def test_preorder_empty_tree(self):
    self.assertEqual('[ ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_postorder_empty_tree(self):
    self.assertEqual('[ ]' ,str(self._Binary_Search_Tree.post_order()))
  
  #testing one node

  def test_add_root_to_empty_tree(self):
    self._Binary_Search_Tree.insert_element('Data')
    #self.assertEqual('[ Data ]', str(self._Binary_Search_Tree))
    self.assertEqual(1, self._Binary_Search_Tree.get_height())
    
  def test_height_with_root(self):   
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual(1, self._Binary_Search_Tree.get_height())  
    
  def test_inorder_with_root(self):
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data ]' ,str(self._Binary_Search_Tree.in_order())) 
    
  def test_preorder_with_root(self):
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data ]' ,str(self._Binary_Search_Tree.pre_order()))  
    
  def test_postorder_with_root(self):
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data ]' ,str(self._Binary_Search_Tree.post_order())) 
  
  #testing insertion after one node
    
  def test_add_left_node_to_root(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')
    #self.assertEqual('[ Structures, Data ]', str(self._Binary_Search_Tree)) #how is this suppose to print out ??? Does it print in alpha order? 
    self.assertEqual(2, self._Binary_Search_Tree.get_height())
    
  def test_inoder_with_root_and_left_node(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')  
    self.assertEqual('[ Data, Structures ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_preoder_with_root_and_left_node(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')  
    self.assertEqual('[ Structures, Data ]' ,str(self._Binary_Search_Tree.pre_order()))
  
  def test_postoder_with_root_and_left_node(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')  
    self.assertEqual('[ Data, Structures ]' ,str(self._Binary_Search_Tree.post_order()))  

  def test_add_right_node_to_root(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Structures')
    #self.assertEqual('[ Data, Structures ]', str(self._Binary_Search_Tree))
    self.assertEqual(2, self._Binary_Search_Tree.get_height())
  
  def test_inorder_with_root_and_right_node(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Structures')  
    self.assertEqual('[ Data, Structures ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_preorder_with_root_and_right_node(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Structures')  
    self.assertEqual('[ Data, Structures ]' ,str(self._Binary_Search_Tree.pre_order()))
    
  def test_postorder_with_root_and_right_node(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Structures')  
    self.assertEqual('[ Structures, Data ]' ,str(self._Binary_Search_Tree.post_order()))  
    
  def test_add_right_node_to_right_child(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Structures')
    #self.assertEqual('[  ]', str(self._Binary_Search_Tree))  
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_inorder_with_right_node_to_right_child(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Structures')
    self.assertEqual('[ Data, Rocks, Structures ]' ,str(self._Binary_Search_Tree.in_order()))
  
  def test_preorder_with_right_node_to_right_child(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Structures')
    self.assertEqual('[ Data, Rocks, Structures ]' ,str(self._Binary_Search_Tree.pre_order()))
    
  def test_postorder_with_right_node_to_right_child(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Structures')
    self.assertEqual('[ Structures, Rocks, Data ]' ,str(self._Binary_Search_Tree.post_order()))

  def test_add_left_node_to_left_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Data')
    #self.assertEqual('[ ]', str(self._Binary_Search_Tree))
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_inorder_with_left_node_to_left_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data, Rocks, Structures ]' ,str(self._Binary_Search_Tree.in_order()))

  def test_preorder_with_left_node_to_left_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Structures, Rocks, Data ]' ,str(self._Binary_Search_Tree.pre_order()))
    
  def test_postorder_with_left_node_to_left_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data, Rocks, Structures ]' ,str(self._Binary_Search_Tree.post_order()))
    
  def test_add_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree') 
    # print bst tree test needed 
    self.assertEqual(2, self._Binary_Search_Tree.get_height())
    
  def test_inorder_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')   
    self.assertEqual('[ Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_preorder_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')  
    self.assertEqual('[ Structures, Rocks, Tree ]' ,str(self._Binary_Search_Tree.pre_order()))  
    
  def test_postorder_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')  
    self.assertEqual('[ Rocks, Tree, Structures ]' ,str(self._Binary_Search_Tree.post_order())) 
  
  def test_add_left_node_to_left_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data')
      #self.assertEqual('[ ]', str(self._Binary_Search_Tree))
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_inorder_with_left_node_to_left_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data, Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_preorder_with_left_node_to_left_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Structures, Rocks, Data, Tree ]' ,str(self._Binary_Search_Tree.pre_order()))
    
  def test_postorder_with_left_node_to_left_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data')
    self.assertEqual('[ Data, Rocks, Tree, Structures ]' ,str(self._Binary_Search_Tree.post_order()))
    
    
  def test_add_right_node_to_left_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Sign')
    #self.assertEqual('[ ]', str(self._Binary_Search_Tree))
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_add_left_and_right_node_to_left_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Sign')  
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_add_left_node_to_right_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Three')
    #self.assertEqual('[ ]', str(self._Binary_Search_Tree))  
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_add_right_node_to_right_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Unique')
    #self.assertEqual('[ ]', str(self._Binary_Search_Tree)) 
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
  
  def test_add_left_and_right_node_to_right_of_second_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
  
  def test_add_third_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign') 
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    
  def test_inorder_third_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign') 
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')    
    self.assertEqual('[ Data, Rocks, Sign, Structures, Three, Tree, Unique ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_preorder_third_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign') 
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')    
    self.assertEqual('[ Structures, Rocks, Data, Sign, Tree, Three, Unique ]' ,str(self._Binary_Search_Tree.pre_order()))
    
  def test_postorder_third_level(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign') 
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')    
    self.assertEqual('[ Data, Sign, Rocks, Three, Unique, Tree, Structures ]' ,str(self._Binary_Search_Tree.post_order()))
    
    
  #following tests for removal 

  def test_removing_leaving_empty(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.remove_element('Data')
    self.assertEqual('[ ]', str(self._Binary_Search_Tree))
    self.assertEqual(0, self._Binary_Search_Tree.get_height())

  def test_removing_left_node_of_root_leaving_root(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.remove_element('Data')
    self.assertEqual('[ Structures ]', str(self._Binary_Search_Tree))
    self.assertEqual(1, self._Binary_Search_Tree.get_height())
    
  def test_removing_right_node_of_root_leaving_root(self):
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.remove_element('Structures')
    self.assertEqual('[ Data ]', str(self._Binary_Search_Tree))
    self.assertEqual(1, self._Binary_Search_Tree.get_height())
    
  def test_removing_left_node_of_root_leaving_height_two(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Trees')
    self._Binary_Search_Tree.remove_element('Data')
    self.assertEqual('[ Structures, Trees ]', str(self._Binary_Search_Tree))
    self.assertEqual(2, self._Binary_Search_Tree.get_height())
    
  def test_removing_right_node_of_root_leaving_height_two(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Trees')
    self._Binary_Search_Tree.remove_element('Trees') 
    self.assertEqual(2, self._Binary_Search_Tree.get_height())  
    self.assertEqual('[ Data, Structures ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_left_child_second_level_leaving_height_three(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.remove_element('Rocks')
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    self.assertEqual('[ Data, Sign, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))  
  
  def test_removing_left_child_of_left_of_second_level_leaving_height_three(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.remove_element('Data')
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    self.assertEqual('[ Rocks, Sign, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_left_child_of_left_of_second_level_leaving_height_two(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.remove_element('Data')
    self.assertEqual(2, self._Binary_Search_Tree.get_height())  
    self.assertEqual('[ Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_right_child_of_left_of_second_level_leaving_height_three(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data')
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.remove_element('Sign')
    self.assertEqual(3, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Data, Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
  
  def test_removing_right_child_of_left_of_second_level_leaving_height_two(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.remove_element('Sign')
    self.assertEqual(2, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_left_child_of_second_level_leaving_height_three(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Tree')
    self.assertEqual(3, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Rocks, Structures, Three, Unique ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_left_child_of_right_of_second_level_leaving_height_three(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Three')
    self.assertEqual(3, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Rocks, Structures, Tree, Unique ]' ,str(self._Binary_Search_Tree.in_order()))    
    
  def test_removing_left_child_of_right_of_second_level_leaving_height_two(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.remove_element('Three')
    self.assertEqual(2, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_right_child_of_right_of_second_level_leaving_height_three(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Unique')
    self.assertEqual(3, self._Binary_Search_Tree.get_height())  
    self.assertEqual('[ Rocks, Structures, Three, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_right_child_of_right_of_second_level_leaving_height_two(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Unique')
    self.assertEqual(2, self._Binary_Search_Tree.get_height())  
    self.assertEqual('[ Rocks, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    
  def test_removing_root_with_one_right_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.remove_element('Structures')
    self.assertEqual(3, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Data, Rocks, Sign, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    self.assertEqual('[ Tree, Rocks, Data, Sign ]' ,str(self._Binary_Search_Tree.pre_order()))
    self.assertEqual('[ Data, Sign, Rocks, Tree ]' ,str(self._Binary_Search_Tree.post_order()))
    
  def test_removing_root_multiple_right_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree') 
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Structures')
    self.assertEqual(3, self._Binary_Search_Tree.get_height()) 
    self.assertEqual('[ Rocks, Sign, Three, Tree, Unique ]' ,str(self._Binary_Search_Tree.in_order()))
    self.assertEqual('[ Three, Rocks, Sign, Tree, Unique ]' ,str(self._Binary_Search_Tree.pre_order()))
    self.assertEqual('[ Sign, Rocks, Unique, Tree, Three ]' ,str(self._Binary_Search_Tree.post_order())) 
    
  def test_removing_left_node_with_multiple_children(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Sign')
    self._Binary_Search_Tree.insert_element('Beta')
    self._Binary_Search_Tree.insert_element('All')
    self._Binary_Search_Tree.remove_element('Rocks')
    self.assertEqual(5, self._Binary_Search_Tree.get_height())
    self.assertEqual('[ All, Beta, Data, Sign, Structures, Tree ]' ,str(self._Binary_Search_Tree.in_order()))
    self.assertEqual('[ Structures, Sign, Data, Beta, All, Tree ]' ,str(self._Binary_Search_Tree.pre_order()))
    self.assertEqual('[ All, Beta, Data, Sign, Tree, Structures ]' ,str(self._Binary_Search_Tree.post_order()))
  
  
  def test_removing_left_node_with_one_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Rocks')
    self.assertEqual(3, self._Binary_Search_Tree.get_height())
    self.assertEqual('[ Data, Structures, Tree, Unique ]' ,str(self._Binary_Search_Tree.in_order()))
    self.assertEqual('[ Structures, Data, Tree, Unique ]' ,str(self._Binary_Search_Tree.pre_order()))
    self.assertEqual('[ Data, Unique, Tree, Structures ]' ,str(self._Binary_Search_Tree.post_order()))
    
  def test_removing_right_node_with_multiple_children(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Water')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Test')
    self._Binary_Search_Tree.insert_element('Vapor')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Tree')
    self.assertEqual(4, self._Binary_Search_Tree.get_height())
    self.assertEqual('[ Data, Rocks, Structures, Test, Three, Unique, Vapor, Water ]' ,str(self._Binary_Search_Tree.in_order()))
    self.assertEqual('[ Structures, Rocks, Data, Unique, Three, Test, Water, Vapor ]' ,str(self._Binary_Search_Tree.pre_order()))
    self.assertEqual('[ Data, Rocks, Test, Three, Vapor, Water, Unique, Structures ]' ,str(self._Binary_Search_Tree.post_order()))
    
  def test_removing_right_node_with_one_child(self):
    self._Binary_Search_Tree.insert_element('Structures')
    self._Binary_Search_Tree.insert_element('Rocks')
    self._Binary_Search_Tree.insert_element('Tree')
    self._Binary_Search_Tree.insert_element('Data') 
    self._Binary_Search_Tree.insert_element('Water')
    self._Binary_Search_Tree.insert_element('Three')
    self._Binary_Search_Tree.insert_element('Test')
    self._Binary_Search_Tree.insert_element('Unique')
    self._Binary_Search_Tree.remove_element('Tree')  
    self.assertEqual(4, self._Binary_Search_Tree.get_height())
    self.assertEqual('[ Data, Rocks, Structures, Test, Three, Unique, Water ]' ,str(self._Binary_Search_Tree.in_order()))
    self.assertEqual('[ Structures, Rocks, Data, Unique, Three, Test, Water ]' ,str(self._Binary_Search_Tree.pre_order()))
    self.assertEqual('[ Data, Rocks, Test, Three, Water, Unique, Structures ]' ,str(self._Binary_Search_Tree.post_order()))  

if __name__ == '__main__':
  unittest.main()