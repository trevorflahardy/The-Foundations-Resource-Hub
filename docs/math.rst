.. _math_operations:

Math Operations
===============

Math is such a common thing in programming that it has its own set of
operations. These operations are used to perform calculations,
manipulate data, and solve problems in your programs.

Arithmetic operators are used to perform basic mathematical operations
like addition, subtraction, multiplication, and division. Here are the
main arithmetic operators in Arduino:

- ``+`` (**Addition**): Adds two values together.
- ``-`` (**Subtraction**): Subtracts the right value from the left
  value.
- ``*`` (**Multiplication**): Multiplies two values.
- ``/`` (**Division**): Divides the left value by the right value.
- ``%`` (**Modulus**): Returns the remainder of the division of the left
  value by the right value (example below to help understand this).

But how do we use these operators? You have seen some examples given to
you already in this book, but they were never formally discussed. You
use these operators the same as you do in conventional math. For
example:

.. code-block:: cpp

  int sum = 5 + 3; // 5 + 3 = 8
  int difference = 5 - 3; // 5 - 3 = 2
  int mul = 5 * 3; // 5 * 3 = 15
  int div = 6 / 2; // 6 / 2 = 3

  // The modulus operator (%) returns the remainder when one
  // number is divided by another. Consider the following,
  int mod = 5 % 3; // 5 divided by 3 is 1 with a remainder of 2
  Serial.println(mod);
  >>> 2


.. seealso::
  **Additional Explanation on Modulus Operator**:

  .. code:: cpp

    Serial.println(10 % 3); // 10 divided by 3 is 3 with a remainder of 1
    >>> 1

    Serial.println(15 % 4); // 15 divided by 4 is 3 with a remainder of 3
    >>> 3

    Serial.println(20 % 7); // 20 divided by 7 is 2 with a remainder of 6
    >>> 6


Math Operations with Different Data Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Arduino, not every operation is supported by every :ref:`data
type <data_types>`. For example, you cannot multiply two
``String``\ s together, or divide two ``bool``\ s. However, you can add
two ``int``\ s together, or subtract two ``float``\ s.

So what can you add/multiply/divide/etc. together, and what can't you?
Here's a quick reference:

.. list-table:: Supported Math Operations by Data Type
   :header-rows: 1

   * - Data Type
     - Supported Operations
   * - ``int``
     - Addition, Subtraction, Multiplication, Division, Modulus
   * - ``float``
     - Addition, Subtraction, Multiplication, Division
   * - ``bool``
     - Logical Operators (e.g., ``&&``, ``||``). See :ref:`bool-operations`.
   * - ``char``
     - Addition, Subtraction. See :ref:`char_operations`.
   * - ``String``
     - Concatenation. See :ref:`string_operations`.

.. _bool-operations:

``bool`` Logical Operators
^^^^^^^^^^^^^^^^^^^^^^^^^^
Two ``bool``\s can be compared using logical operators (e.g., ``&&``, ``||``), but cannot be added, subtracted, multiplied, or divided. This is covered in :ref:`logical operators <logical_operators>`.

.. _char_operations:

``char`` Operations
^^^^^^^^^^^^^^^^^^^

A ``char`` can be added to or subtracted from another ``char`` or an ``int``, but not multiplied, divided, or have the modulus operator applied.

.. code-block:: cpp

    char letter = 'A';
    char nextLetter = letter + 1; // 'A' + 1 = 'B'

.. note::

  This is because ``char``\ s are represented as numbers in programming. The ASCII value of ``'A'`` is ``65``, ``'B'`` is ``66``, and so on. When you add ``1`` to ``'A'``, you get ``'B'``. You **will not need to know this** for this course, but it's good to know!

.. _string_operations:

``String`` Operations
^^^^^^^^^^^^^^^^^^^^^

Two ``String``\s can be **concatenated** (a word for combined) using the ``+``
operator with other ``String``\s and certain :ref:`data types <data_types>`:

Supported Concatenations:
''''''''''''''''''''''''''

You can concatenate a ``String`` with:

#. **Constant integers** (e.g., ``123``).
#. **Constant long integers** (e.g., ``123456789``).
#. **Single characters** (e.g., ``'A'``).
#. **Constant character arrays** (C-strings) (e.g., ``"abc"``).
#. **Other** ``String`` objects.

Examples of String Concatenation:
''''''''''''''''''''''''''''''''''

.. code-block:: cpp

  String stringOne = "Hello";
  String stringTwo = "World";
  String stringThree;

  // Adding a constant integer:
  stringThree = stringOne + 123;  // Result: "Hello123"

  // Adding a constant long integer:
  stringThree = stringOne + 123456789;  // Result: "Hello123456789"

  // Adding a single character:
  stringThree = stringOne + 'A';  // Result: "HelloA"

  // Adding a constant character array:
  stringThree = stringOne + " there!";  // Result: "Hello there!"

  // Adding another String:
  stringThree = stringOne + " " + stringTwo;  // Result: "Hello World"


Adding Function Results
''''''''''''''''''''''''

You can also add the results of functions to strings. For example, if you have a function that returns an integer, you can add the result to a string:

.. code-block:: cpp

  stringThree = stringOne + millis();  // E.g., "Hello12345" (if millis() = 12345)
  stringThree = stringOne + analogRead(A0);  // E.g., "Hello402" (if analogRead(A0) = 402)

.. seealso::

  You can see the `Arduino Documentation for String Addition <https://docs.arduino.cc/built-in-examples/strings/StringAdditionOperator/>`__ for more information.

Math Shorthands
~~~~~~~~~~~~~~~

Some math operations are so common that shorthands have been created for
them. These shorthands allow you to perform an operation and assign the
result to a variable in a single step.

Here are some common shorthand operators:

- ``++``: Increments the value of a variable by 1.

  .. code:: cpp

    int count = 0;
    count++; // Equivalent to count = count + 1

  This is the same as ``count = count + 1``, but shorter and more readable. It is also **very important** for :ref:`loops <loops>`.

- ``--``: Decrements the value of a variable by 1.

  .. code:: cpp

    int score = 100;
    score--; // Equivalent to score = score - 1

  This is the same as ``score = score - 1``, but shorter and more readable. It is also **very important** for :ref:`loops <loops>`.

- ``+=``: Adds the right value to the left value and assigns the
  result to the left value.

  .. code:: cpp

    int x = 5;
    x += 3; // Equivalent to x = x + 3

- ``-=``: Subtracts the right value from the left value and assigns
  the result to the left value.

  .. code:: cpp

    int y = 10;
    y -= 2; // Equivalent to y = y - 2

- ``*=``: Multiplies the left value by the right value and assigns
  the result to the left value.

  .. code:: cpp

    int z = 3;
    z *= 4; // Equivalent to z = z * 4

- ``/=``: Divides the left value by the right value and assigns the
  result to the left value.

  .. code:: cpp

    int a = 20;
    a /= 5; // Equivalent to a = a / 5

- ``%=``: Applies the modulus operation to the left value and
  assigns the result to the left value.

  .. code:: cpp

    int b = 10;
    b %= 3; // Equivalent to b = b % 3

These shorthand operators are useful for updating variables in a single
step, reducing the amount of code you need to write. You should use
these operators when you want to increment, decrement, or modify a
variable's value quickly and efficiently.

Quiz
----

.. quizdown:: quizzes/math_quiz.md
