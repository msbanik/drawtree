# -*- coding: utf-8 -*-
import sys


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_min(node):
    """Find min value node"""
    while node and node.left:
        node = node.left
    return node


def find_max(node):
    """Find max value node"""
    while node and node.right:
        node = node.right
    return node


def find(value, node):
    """Find node with val equal to value"""
    while node:
        if value < node.val:
            node = node.left
        elif value > node.val:
            node = node.right
        else:
            return node


def insert(value, node):
    """Insert value into node by following BST properties"""
    if node is None:
        return TreeNode(value)

    if value < node.val:
        node.left = insert(value, node.left)

    elif value > node.val:
        node.right = insert(value, node.right)
    else:
        # duplicate, ignore it
        return node
    return node


def delete(value, node):
    """Deletes node from the tree
    Return a pointer to the resulting tree
    """
    if node is None:
        return None

    if value < node.val:
        node.left = delete(value, node.left)
    elif value > node.val:
        node.right = delete(value, node.right)
    elif node.left and node.right:
        tmp_cell = find_min(node.right)
        node.val = tmp_cell.val
        node.right = delete(node.val, node.right)
    else:
        if node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
    return node


class AsciiNode(object):
    left = None
    right = None

    # length of the edge from this node to its children
    edge_length = 0
    height = 0
    lablen = 0

    # -1 = left, 0 = root, 1 = right
    parent_dir = 0

    # max supported unit32 in dec, 10 digits max
    label = ''


MAX_HEIGHT = 1000
lprofile = [0] * MAX_HEIGHT
rprofile = [0] * MAX_HEIGHT
INFINITY = (1 << 20)

# adjust gap between left and right nodes
gap = 3


def build_ascii_tree_recursive(t):
    """
    :type t: TreeNode
    """
    if t is None:
        return None

    node = AsciiNode()
    node.left = build_ascii_tree_recursive(t.left)
    node.right = build_ascii_tree_recursive(t.right)

    if node.left:
        node.left.parent_dir = -1

    if node.right:
        node.right.parent_dir = 1

    node.label = '{}'.format(t.val)
    node.lablen = len(node.label)
    return node


# Copy the tree into the ascii node structure
def build_ascii_tree(t):
    if t is None:
        return None
    node = build_ascii_tree_recursive(t)
    node.parent_dir = 0
    return node


# The following function fills in the lprofile array for the given tree.
# It assumes that the center of the label of the root of this tree
# is located at a position (x,y).  It assumes that the edge_length
# fields have been computed for this tree.
def compute_lprofile(node, x, y):
    if node is None:
        return

    isleft = (node.parent_dir == -1)
    lprofile[y] = min(lprofile[y], x - ((node.lablen - isleft) / 2))
    if node.left:
        i = 1
        while (i <= node.edge_length and y + i < MAX_HEIGHT):
            lprofile[y + i] = min(lprofile[y + i], x - i)
            i += 1

    compute_lprofile(node.left, x - node.edge_length - 1, y + node.edge_length + 1)
    compute_lprofile(node.right, x + node.edge_length + 1, y + node.edge_length + 1)


def compute_rprofile(node, x, y):
    if node is None:
        return

    notleft = (node.parent_dir != -1)
    rprofile[y] = max(rprofile[y], x + ((node.lablen - notleft) / 2))
    if node.right is not None:
        i = 1
        while i <= node.edge_length and y + i < MAX_HEIGHT:
            rprofile[y + i] = max(rprofile[y + i], x + i)
            i += 1

    compute_rprofile(node.left, x - node.edge_length - 1, y + node.edge_length + 1)
    compute_rprofile(node.right, x + node.edge_length + 1, y + node.edge_length + 1)


# This function fills in the edge_length and
# height fields of the specified tree
def compute_edge_lengths(node):
    if node is None:
        return
    compute_edge_lengths(node.left)
    compute_edge_lengths(node.right)

    # first fill in the edge_length of node
    if (node.right is None and node.left is None):
        node.edge_length = 0
    else:
        if node.left:
            i = 0
            while (i < node.left.height and i < MAX_HEIGHT):
                rprofile[i] = -INFINITY
                i += 1
            compute_rprofile(node.left, 0, 0)
            hmin = node.left.height
        else:
            hmin = 0

        if node.right is not None:
            i = 0
            while (i < node.right.height and i < MAX_HEIGHT):
                lprofile[i] = INFINITY
                i += 1
            compute_lprofile(node.right, 0, 0)
            hmin = min(node.right.height, hmin)
        else:
            hmin = 0

        delta = 4
        i = 0
        while (i < hmin):
            delta = max(delta, gap + 1 + rprofile[i] - lprofile[i])
            i += 1

        # If the node has two children of height 1, then we allow the
        # two leaves to be within 1, instead of 2
        if (((node.left is not None and node.left.height == 1) or (
                        node.right is not None and node.right.height == 1)) and delta > 4):
            delta -= 1
        node.edge_length = ((delta + 1) / 2) - 1


    # now fill in the height of node
    h = 1
    if node.left:
        h = max(node.left.height + node.edge_length + 1, h)
    if node.right:
        h = max(node.right.height + node.edge_length + 1, h)
    node.height = h


# used for printing next node in the same level,
# this is the x coordinate of the next char printed
print_next = 0


# This function prints the given level of the given tree, assuming
# that the node has the given x coordinate.
def print_level(node, x, level):
    global print_next
    if node is None:
        return
    isleft = (node.parent_dir == -1)
    if level == 0:
        spaces = (x - print_next - ((node.lablen - isleft) / 2))
        sys.stdout.write(' ' * spaces)

        print_next += spaces
        sys.stdout.write(node.label)
        print_next += node.lablen
    elif node.edge_length >= level:
        if node.left:
            spaces = (x - print_next - level)
            sys.stdout.write(' ' * spaces)
            print_next += spaces
            sys.stdout.write('/')
            print_next += 1

        if node.right:
            spaces = (x - print_next + level)
            sys.stdout.write(' ' * spaces)
            print_next += spaces
            sys.stdout.write('\\')
            print_next += 1
    else:

        print_level(node.left,
                    x - node.edge_length - 1,
                    level - node.edge_length - 1)
        print_level(node.right,
                    x + node.edge_length + 1,
                    level - node.edge_length - 1)


# prints ascii tree for given Tree structure
def drawtree(t):
    if t is None:
        return
    proot = build_ascii_tree(t)
    compute_edge_lengths(proot)
    i = 0
    while (i < proot.height and i < MAX_HEIGHT):
        lprofile[i] = INFINITY
        i += 1

    compute_lprofile(proot, 0, 0)
    xmin = 0
    i = 0
    while (i < proot.height and i < MAX_HEIGHT):
        xmin = min(xmin, lprofile[i])
        i += 1

    i = 0
    global print_next
    while (i < proot.height):
        print_next = 0
        print_level(proot, -xmin, i)
        print
        i += 1

    if proot.height >= MAX_HEIGHT:
        print "This tree is taller than %d, and may be drawn incorrectly.".format(MAX_HEIGHT)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == '#' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def draw_bst(nums):
    """ Draw binary search tree from number in nums
    :type nums: list[int]
    """
    if not nums:
        return
    root = TreeNode(nums[0])
    for num in nums[1:]:
        root = insert(num, root)
    drawtree(root)


def draw_random_bst(n):
    """ Draw random binary search tree of n nodes
    """
    from random import randint
    nums = set()
    max_num = 10 * n
    if 0 < n < MAX_HEIGHT:
        while len(nums) != n:
            nums.add(randint(1, max_num))
    draw_bst(list(nums))


def draw_level_order(string):
    """ The serialization of a binary tree follows a level order traversal,
    where '#' signifies a path terminator where no node exists below.

    e.g. '{3,9,20,#,#,15,7}'

          3
         / \
        9  20
           / \
          15 7
    """
    drawtree(deserialize(string))


if __name__ == '__main__':
    # nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    # draw_bst(nums)

    # draw_random_bst(10)

    # drawtree(deserialize('{3,9,20,#,#,15,7}'))
    pass
