My chapter in a nested directory in m01
=======================================

This file is ``m01_introduction/material/mychapter.rst``.

.. _refnestedm01:

Some subsection
---------------

Some text here.

.. questionnaire:: 1
  :title: The English questionnaire

  Some image:

  .. _refnestedimg:

  .. image:: /images/apluslogo.png
    :alt: aplus logo

  **TESTING LINKS**: 

  * chapter in the same module :doc:`../06_languages`, :ref:`section in multilang <multilangref>`
    * exercise: :ref:`multilang quiz <refmultilangquiz>`
  * chapter in the same module and nested directory: :doc:`/m01_introduction/material/mychapter`, :ref:`refnestedm01`
    * exercise: :ref:`quiz in m01 nested chapter <refnestedimg>`
  * chapter in another module: :doc:`/m02_programming_exercises/02_hello_world`, :ref:`chapter hello world <refhelloworld>`
    * exercise: :ref:`exercise hello python <refhellopython>`
  * chapter in another module and nested directory: :doc:`/m02_programming_exercises/material/somechapter`, :ref:`refnestedm02`
    * exercise: :ref:`quiz in m02 nested chapter <refnestedimgm02>`

  .. pick-one:: 1

    What is 1+1?

    a. 1
    *b. 2
    c. 3

    !b § Try again.

