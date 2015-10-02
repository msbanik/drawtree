drawtree
========

.. image:: https://pypip.in/v/drawtree/badge.png
    :target: https://pypi.python.org/pypi/drawtree
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

Draw binary tree in plain text

Usage
-----
.. code-block:: python
    from drawtree import draw_level_order
    draw_level_order('{3,9,20,#,#,15,7}')
    ...

::
  3
 / \
9  20
   / \
  15  7


.. code-block:: python
    from drawtree import draw_random_bst
    draw_random_bst(10)
    ...

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


.. code-block:: python
    from drawtree import draw_bst
    nums = [55, 30, 10, 5, 2, 20, 15, 25, 40, 35, 70, 60, 80, 75, 95]
    draw_bst(nums)
    ...

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


Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`drawtree` was written by `Madhusudan Banik <msbanik@gmail.com>`_.
