.. _arrays:

Arrays
======

An array is a collection of variables of the same type, stored under one
name. Arrays are useful when you need to store multiple values, such as
sensor readings or a list of LED states, and access them using a single
variable name.

For example, instead of creating separate variables for multiple sensor
readings:

.. code:: cpp

   int sensor1 = 100;
   int sensor2 = 200;
   int sensor3 = 300;

You can use an array to store all the readings in a single variable:

.. code:: cpp

   int sensorReadings[3] = {100, 200, 300};

Why do we use arrays? They help organize related data, simplify code,
and make it easier to work with multiple values. They also allow you to
easily perform operations on *groups* of data at once, such as
calculating averages or finding the maximum value.

Let's say that we had 100 sensor readings:

.. code:: cpp

   int sensor1 = 100;
   int sensor2 = 200;
   int sensor3 = 300;
   // ...
   int sensor100 = 1000;

How would you add all these sensor readings together? You would have to
write 100 lines of code to add them all together! Instead, you can use
an array to store all the sensor readings and add them together in a
loop. How do we do this, though?

How Arrays Work
---------------

Arrays consist of the following components:

#. **Data Type**: Specifies the type of data the array will hold (e.g., ``int``, ``float``, ``char``).
#. **Array Name**: The unique identifier for the array, used to access its elements.
#. **Size**: The number of elements the array can hold. This is determined when the array is created, or you can let the compiler determine it automatically.
#. **Elements**: Individual values stored in the array, accessed by their index. Indices start at ``0`` and go up one value for each element.

To hold all our sensor readings in an array, we can define an array like so:

.. code:: cpp

   int sensorReadings[5] = {100, 200, 300, 400, 500}; // Array of 5 sensor readings

Or, our super long example with 100 sensor readings:

.. code:: cpp

   int sensorReadings[100] = {100, 200, 300, 400, 500, ...}; // Array of 100 sensor readings

--------------

Thus, to define an array in Arduino, you use the following **syntax**:

.. code:: cpp

   <variable type> <array name>[<size>?] = {<value1>, <value2>, ...};

For instance:

.. code:: cpp

   int ledStates[5] = {1, 0, 1, 1, 0}; // Array of LED states

The question mark (``?``) after “size” in the syntax means that if you
initialize the array with values, the size can be determined
automatically:

.. code:: cpp

   int sensorReadings[] = {100, 200, 300, 400}; // Automatically sized. Can only hold 4 items.

   int NUM_SENSORS = 5;
   int sensorReadings[NUM_SENSORS] = {100, 200, 300, 400, 500}; // Sized to 5. Can use a variable to size the array too.

Accessing and Modifying Arrays
------------------------------

Sometimes, you may need to change the values stored in an array or
retrieve specific elements. To access or modify elements in an array,
use their index:

.. code:: cpp

   int firstReading = sensorReadings[0]; // Accesses the first element (100)
   sensorReadings[2] = 400; // Changes the third element to 400

..

   You can also declare an array without initializing it. In this case,
   the array elements will contain **garbage values** (random data).
   Always initialize your arrays to avoid unexpected behavior.

   You can define a ``const`` array, too! This is useful when you want
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

..

   **Advanced Note: Parallel Arrays [OPTIONAL]:** If you need to
   associate data of different types (e.g., sensor IDs and readings),
   consider using **parallel arrays**. Parallel arrays are separate
   arrays that share a relationship through their indices:

   .. code:: cpp

      int sensorIDs[] = {1, 2, 3};
      int sensorReadings[] = {100, 200, 300};

      // Access the ID and corresponding reading:
      int id = sensorIDs[1];         // Sensor ID: 2
      int reading = sensorReadings[1]; // Sensor Reading: 200

   While effective, this approach requires careful indexing to ensure
   consistency. Alternatives like structures (``struct``) can provide a
   more robust solution for complex data relationships, but they are out
   of the scope of this course.

Arrays are a critical part of programming in Arduino, enabling efficient
and organized management of related data.