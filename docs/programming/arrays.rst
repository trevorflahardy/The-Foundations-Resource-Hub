.. _arrays:

Arrays
======

An array is a special variable type that allows you to store multiple
values under a single variable name. Arrays are useful when you need to
store a collection of related data, such as sensor readings or LED
states. They help organize data, simplify code, and make it easier to
work with multiple values.

For example, instead of creating separate variables for multiple sensor
readings:

.. code-block:: cpp

   int sensor1 = 100;
   int sensor2 = 200;
   int sensor3 = 300;

You can use an array to store all the readings in a single variable:

.. code-block:: cpp

   int sensorReadings[3] = {100, 200, 300};

Why do we use arrays? They help organize related data, simplify code,
and make it easier to work with multiple values. They also allow you to
easily perform operations on *groups* of data at once, such as
calculating averages or finding the maximum value.

Let's say that we had 100 sensor readings:

.. code-block:: cpp

   int sensor1 = 100;
   int sensor2 = 200;
   int sensor3 = 300;
   // ...
   int sensor100 = 1000;

How would you add all these sensor readings together? You would have to
write 100 lines of code to add them all together! Instead, you can use
an array to store all the sensor readings and add them together in a
:ref:`loop <loops>`.

Anatomy of an Array
-------------------

An array consists of the following components:

#. **Data Type**: Specifies the :ref:`type of data <data_types>` the array will hold (e.g., ``int``, ``float``, ``char``).
#. **Array Name**: The unique identifier for the array, used to access its elements. An array is a special variable, so it follows the same naming rules.
#. **Size**: The number of elements the array can hold. This is determined when the array is created, or you can let the compiler determine it automatically.
#. **Elements**: Individual values stored in the array, accessed by their index. Indices start at ``0`` and go up one value for each element.

Array Syntax
^^^^^^^^^^^^

To define an array, you need to specify the data type, array name, and
(sometimes) size. To do this, you use the following **syntax** in your code:

.. code-block:: cpp

   <variable type> <array name>[<size>?] = {<value1>, <value2>, ...};

For instance:

.. code-block:: cpp

   int ledStates[5] = {1, 0, 1, 1, 0}; // Array of LED states

The question mark (``?``) after “size” in the syntax means that if you
initialize the array with values, the size can be determined
automatically:

.. code-block:: cpp

   int sensorReadings[] = {100, 200, 300, 400}; // Automatically sized. Can only hold 4 items.

   int NUM_SENSORS = 5;
   int sensorReadings[NUM_SENSORS] = {100, 200, 300, 400, 500}; // Sized to 5 elements max.

.. tip::

   See how we used a constant variable ``NUM_SENSORS`` to define the size of the array? This is a good practice to make your code more readable and maintainable, if you choose to specify the size of the array yourself.

Array Initialization
^^^^^^^^^^^^^^^^^^^^

When you define an array, you can initialize it with values. The values
are enclosed in curly braces (``{}``) and separated by commas. The
number of values must match the array's size. For example:

.. code-block:: cpp

   int sensorReadings[5] = {100, 200, 300, 400, 500}; // Array of 5 sensor readings

Or, our super long example with 100 sensor readings:

.. code-block:: cpp

   int sensorReadings[100] = {100, 200, 300, 400, 500, ...}; // Array of 100 sensor readings

Array Definition
^^^^^^^^^^^^^^^^

You can also define an array without initializing it. In this case, the
array elements will contain **garbage values**.

.. code-block:: cpp

   int sensorReadings[5]; // Array of 5 sensor readings with garbage values

   sensorReadings[0] = 100; // Assign a value to the first element
   sensorReadings[1] = 200; // Assign a value to the second element
   sensorReadings[2] = 300; // Assign a value to the third element
   sensorReadings[3] = 400; // Assign a value to the fourth element
   sensorReadings[4] = 500; // Assign a value to the fifth element
   >>> {100, 200, 300, 400, 500}

.. seealso::

   A :ref:`practical example <for_loop_fibonacci_example>` of this will be demonstrated later in the
   :ref:`loops` section.

Accessing and Modifying Arrays
------------------------------

Sometimes, you may need to change the values stored in an array or
retrieve specific elements. To access or modify an array element in
programming, you do it by using the array name followed by the **index**
of the item you want to access or modify

An **index** is a number that represents the position of an element in
the array. The first element in an array has an index of ``0``, the
second element has an index of ``1``, and so on. For example, in an array
``sensorReadings[5]``, the first element is at index ``0``, and the last
element is at index ``4``.

So for example, in the array ``sensorReadings[5]``:

.. code-block:: cpp

   int firstReading = sensorReadings[0]; // Accesses the first element (100)
   sensorReadings[2] = 400; // Changes the third element to 400

.. note::

   You can define a ``const`` array, too. This is useful when you want
   to store a set of values that should not change during the program's
   execution.

   .. code:: cpp

      const int LED_PINS[] = {2, 3, 4, 5}; // Array of LED pins that cannot change

Key Rules and Limitations
-------------------------

- Arrays must consist of variables of the same type. You cannot mix
  types in a single array. For example, this is not allowed:

  .. code:: cpp

     int invalidArray[2] = {100, "text"}; // Error: type mismatch

- Attempting to access an element outside the array's defined size will
  throw an error! For example:

  .. code:: cpp

     int numbers[3] = {1, 2, 3};
    int invalidAccess = numbers[5]; // Not good! This array only has 3 elements.

.. quizdown:: ../quizzes/arrays_quiz.md

.. note::

   **Advanced: Parallel Arrays [OPTIONAL]:** If you need to
   associate data of different types (e.g., sensor IDs and readings),
   consider using **parallel arrays**. Parallel arrays are separate
   arrays that share a relationship through their indices:

   .. code:: cpp

      int sensorIDs[] = {1, 2, 3};
      float sensorReadings[] = {100.63, 200.21, 300.86};

      // Access the ID and corresponding reading:
      int id = sensorIDs[1];         // Sensor ID: 2
      float reading = sensorReadings[1]; // Sensor Reading: 200.21

   While effective, this approach requires careful indexing to ensure
   consistency. Alternatives like structures (``struct``) can provide a
   more robust solution for complex data relationships, but they are out
   of the scope of this course.

Arrays are a critical part of programming in Arduino, enabling efficient
and organized management of related data.
