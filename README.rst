drawtree
========

.. image:: https://img.shields.io/pypi/v/drawtree.svg?style=flat-square&label=latest%20version
    :target: https://pypi.python.org/pypi/drawtree
    :alt: Latest PyPI version


Draw binary tree in plain text

Usage
-----
Draw tree from level order traversal, '#' signifies a path terminator where no node exists below.

.. code-block:: python

    from drawtree import draw_level_order
    draw_level_order('{3,9,20,#,#,15,7}')

::

      3
     / \
    9  20
       / \
      15  7

Draw random binary search tree

.. code-block:: python

    from drawtree import draw_random_bst
    draw_random_bst(10)

::

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

Draw binary search tree from integer array

.. code-block:: python

    from drawtree import draw_bst
    nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    draw_bst(nums)

::

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


Command line
------------

$ bst takes 


Flags:
 -p, --preorder    interpet sequence as preorder    
 -b, --balanced    auto balance bst
 -l, --level-order interpet sequence as level-order

Print a bst:

.. code-block:: bash

    $ bst 10 5 8 4 6 
    $ bst nodes.txt
    $ echo "colin eric dave" | bst
    $ cat nodes.txt | sort | uniq | bst

Print a balanced bst:

.. code-block:: bash

    $ bst -b 10 5 6 9 3
    $ bst -b nodes.txt
    $ bst -b < nodes.txt

Print a bst from a preorder expression:

.. code-block:: bash

    $ bst -p dave colin dan
    $ echo "1 2 3 4 5" | bst -p
    $ bst -p nodes.txt  

Print a binary tree from a level order expression:

.. code-block:: bash

    $ bst -l [4,#,7,5,9,#]   (leetcode format)
    $ bst -l {4 # 7 5} 

Print a random bst:

.. code-block:: bash

    $ bst           (random bst of 10 nodes)
    $ bst 5         (random bst of 5 nodes)
    $ bst -b 7      (random balanaced bst of 7 nodes)


Installation
------------
To install drawtree, simply:

.. code-block:: bash

    $ pip install drawtree


Licence
-------
MIT

Reference
---------
`Draw tree <http://web.archive.org/web/20071224095835/http://www.openasthra.com/wp-content/uploads/2007/12/binary_trees1.c>`_

Authors
-------

`drawtree` was written by `Madhusudan Banik <msbanik@gmail.com>`_.
