from drawtree import draw_level_order
draw_level_order('{3,9,20,#,#,15,7}')

"""
  3
 / \
9  20
   / \
  15  7

"""

# from drawtree import draw_random_bst
# draw_random_bst(10)
"""
    64
    / \
   /   \
  4    66
   \     \
   37    70
   / \
  8  51
 / \
6  12
     \
     21

"""

# from drawtree import draw_bst
# nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
# draw_bst(nums)
"""
             55
             / \
            /   \
           /     \
          /       \
         30       70
        / \       / \
       /   \     /   \
      /     \   60   80
     10     40       / \
    / \     /       /   \
   /   \   35      75   95
  5    20
 /     / \
2     /   \
     15   25

"""