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
