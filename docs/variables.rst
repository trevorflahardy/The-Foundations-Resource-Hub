.. _variables:

Variables
=========

In programming, a variable is like a storage container used to hold
data. Think of it as a labeled box where you can store a value—whether
it's a number, a piece of text, or a ``true`` / ``false`` statement. Variables
allow programs to process and manipulate information dynamically.

Variables are similar to how they're used in math, where you might have
an equation like ``x = 5``. In programming, you can assign values to
variables and use them to perform calculations, make decisions, or
control hardware components. But how are variables defined in Arduino?

Defining a Variable
-------------------

Let's say you're writing a program to control the speed of a motor (can
be any example, not necessarily a motor). You might use a variable to
store the speed value, which can then be adjusted during the program's
execution.

.. code-block:: cpp

   int motorSpeed = 100; // Variable to store the motor speed

The above line of code creates a variable named ``motorSpeed`` and
assigns it a value of ``100``.

--------------

To define a variable in Arduino, you use the following syntax:

.. code-block:: cpp

   <variable type> <variable name> = <value>;

In our motor speed example, ``int`` (the variable type) before the
variable name indicates that it's an integer, or a whole number without
a decimal point. We'll discover more of these `Data Types`_ as
we go along.

Variable Mutability
-------------------

Sometimes you want to change the value of a variable as your program.
This is called **mutability**, and it describes the process of mutating (changing)
the value of a variable.

To change the value of a variable, you assign a new value to it. For example,
you could change the value of ``motorSpeed`` later in the program, allowing you to
control the motor's speed dynamically:

.. code-block:: cpp

   // This variable's value can change.
   int speed = 100;

   // We can change it simply by assigning a new value.
   speed = 200;

Conversely, a variable that cannot change its value is known as **immutable**, or a
**constant**. We'll cover this in the `Variable Qualifiers`_ section.

.. _data_types:

Data Types
----------

Every variable in Arduino has a **type**, which defines the kind of data
it can store. The type determines the size of the variable in memory and
the operations you can perform on it. Types vary from simple numbers to
complex structures, each with its own rules and limitations.

Here are some of the most commonly used data types:

#. ``int`` (**Integer**): Stores whole numbers, such as ``1``, ``42``,
   or ``-7``.

   .. code:: cpp

      int myNumber = 10; // Stores the number 10

   Trying to store a decimal number in an ``int`` variable will **truncate**
   (a word for remove) the decimal portion. For example, ``int pi = 3.14;`` will
   store ``3`` in ``pi``. “Whole integers” (aka whole numbers) are
   numbers **without** a decimal point.

   This also goes for arithmetic operations. If you divide two integers,
   the result will be an integer. For example, ``5 / 2`` will result in
   ``2``, not ``2.5``.

   .. code:: cpp

      int result = 5 / 2; // Stores 2, not 2.5

#. ``long``: An ``int`` can only store numbers up to a certain size. If
   you need to store larger numbers, you can use a ``long``. A ``long``
   can store larger numbers than an ``int``.

   .. code:: cpp

      long bigNumber = 1000000L; // Stores a large number

   Notice the ``L`` at the end of the number. This tells the compiler
   that the number is a ``long``. If you don't include the ``L``, the
   number will be treated as an ``int``.

   A ``long`` is useful when you need to store numbers that are too large
   for an ``int``. It can store numbers up to ``2,147,483,647``. ``long``\s can
   only store whole numbers, not decimals.

   .. note::

      The ``long`` type is not used as often as ``int`` in this course.
      However, it is important to know that it exists as some :ref:`libraries <libraries>`
      may require it. More on this later, though.

#. ``float`` (**Floating-Point Number**): Stores numbers **with**
   decimals, such as ``3.14``, ``0.5``, or ``-2.718``.

   .. code:: cpp

      float pi = 3.14; // Stores the value of pi with decimals

   Floating-point numbers can represent a wide range of values,
   including fractions and very large or very small numbers. They are
   useful for calculations that require precision. They can also hold
   whole numbers, but they may use more memory than ``int`` variables.

#. ``String`` (**Text**): Stores a **sequence of characters**, such as
   ``"Hello"``, ``"Arduino"``, or ``"123"``.

   .. code:: cpp

      String message = "Hello, Arduino!"; // Stores a text message

   A ``String`` is how you store messages, words, or sentences in code.
   When creating a string, it **must** be enclosed in double quotes
   (``"``). In Arduino, you can manipulate strings, such as combining
   them or extracting parts of them (covered in :ref:`math_operations` later).
   Strings are useful for displaying messages, reading input, or storing
   text-based data. We'll cover these in more detail later.

#. ``char`` (**Character**): Stores **a single character**, such as
   ``'A'``, ``'b'``, or ``'7'``.

   .. code:: cpp

      char grade = 'A'; // Stores the letter A

   Characters are enclosed in single quotes (``'``) to distinguish them
   from ``String``\ s. Characters **only** represent individual letters,
   digits, or symbols. A ``char`` **cannot** hold multiple characters,
   it can only store a single character. These are not often used in the
   course, however, they may be important in some specific cases.

#. ``bool`` (**Boolean**): Stores ``true`` or ``false`` values.

   .. code:: cpp

      bool isLightOn = true; // Indicates whether a light is on

   Internally, ``true`` is represented as ``1`` and ``false`` as ``0``.
   Booleans are used for logical operations, comparisons, and
   decision-making in your code. You may see a ``bool`` display as a
   ``1`` or ``0`` because of this.

.. caution::

   Note the distinction between a ``char`` and a ``String``.

   A ``char`` stores a single character and uses ``''`` (single quotes), while a
   ``String`` stores multiple characters and uses ``""`` (double
   quotes). ``char``\ s can **only hold a single character**, while
   ``String``\ s can hold **multiple characters**. Thus,

   .. code:: cpp

      char letter = 'A'; // Correct
      String word = "Hello"; // Correct

      char word = "Hello"; // Incorrect! "" is a String

   Defining a variable with the wrong type will result in a compilation.
   error. Make sure to use the correct type for your data.

Variable Qualifiers
-------------------

Variable **qualifiers** are additional keywords that modify the behavior
of variables. They provide information about how the variable
should be treated or used in the program. One common qualifier is
``const``, which we'll cover here.

``const``
~~~~~~~~~

The ``const`` keyword is used to define a **constant variable**, which
is a variable whose value cannot be changed once it's set. This is also
known as an **immutable variable**. Constants are
useful for storing values that should not be modified during the
program's execution, such as mathematical constants or pin numbers.

Defining a ``const`` Variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To define a constant variable, you use the following syntax:

.. code-block:: cpp

   const <variable type> <variable name> = <value>;

For example, let's say you wanted to define a pin number for an LED that is connected
to pin 13 on your Arduino board. This pin does not change during the execution
of your code so it's a good candidate for a constant.

.. code-block:: cpp

   const int LED_PIN = 13; // Defines a constant for the LED pin

As a general rule of thumb, you want to declare any variable you **know
will not change** as a ``const``. This is because it is good practice to
make sure that you do not accidentally change the value of a variable
that should not be changed.

.. code-block:: cpp

   const int LED_PIN = 13; // Defines a constant for the LED pin
   LED_PIN = 10; // Error! You cannot change the value of a constant.

Sometimes you want an error to be thrown if you accidentally change the
value of a variable. This is where ``const`` comes in handy.

.. note::

   **Advanced Note: Constants vs Preprocessor Directives [OPTIONAL]:**
   When defining pins to variables, it is recommended to use
   preprocessor directives instead of constants. This is because
   preprocessor directives are more efficient and cleaner. However, for
   the purposes of this course, we will be using constants. You can read
   more about this in the :ref:`Macros and Preprocessor
   Directives <macros-and-preprocessor-directives>` section.

.. seealso::

   There are **many other modifiers** in the Arduino Language, however, you
   do not need to know them for this course. You can find them on the
   `Arduino Language
   Reference <https://docs.arduino.cc/language-reference/#variables>`__ if
   you are interested, but you do not need to.

Variable Initialization vs Definition
-------------------------------------

So far, we've discussed how to define variables and assign them values.
Common examples have shown a variable being defined and a value being
assigned to it at the same time. However, this is not the only way to
create a variable. You can either,

#. Define a variable and assign it a value **at the same time** (`Initialization`_). This is the most common way to create variables and what you have seen so far.
#. Define a variable **without** assigning it a value (`Definition`_).

How do these two differ, and when should you use one over the other?

Initialization
~~~~~~~~~~~~~~

Initialization is the process of assigning an initial value to a
variable when it is declared. This often happens at the time the
variable is created in the program. For example, if you declare a
variable ``int x = 5;``, you are **both** declaring the variable ``x``
*and* initializing it with the value ``5``. Initialization ensures that
a variable has a valid value before it is used, preventing undefined
behavior.

For example,

.. code-block:: cpp

   int x = 5; // Variable 'x' is defined and initialized to 5

   int y;     // Variable 'y' is defined but not initialized

   // Trying to use 'y' without a value is going to crash
   // your program!
   Serial.println(y); // Error: 'y' is not initialized

.. tip::

   ``Serial.println()`` tries to use the ``y`` variable in
   the code above. This will cause an error because ``y`` has not been
   initialized with a value. Do not worry about what ``Serial.println()``
   is yet, this is covered in :ref:`Functions`.

   All you need to know is that the program crashes.

Definition
~~~~~~~~~~

Definition refers to the process of declaring a variable's type and name
**without necessarily assigning it an initial value**. For example,
``int x;`` defines the variable ``x`` but does not initialize it,
leaving its value indeterminate until it is explicitly assigned later in
the code. Using an uninitialized variable can lead to unpredictable
behavior or errors in your program.

.. code-block:: cpp

   int y; // Variable 'y' is defined but not initialized

   y = 10; // 'y' is assigned a value after definition

Key Difference Between Initialization and Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The key difference between initialization and definition is whether a
variable is given a value at the time it is declared. Sometimes
in programming you want to define a variable without giving it a value,
and then assign it a value later in the program. However, **You should
initialize variables whenever possible** to ensure they have a valid
value before being used.

.. code-block:: cpp

   // Initialization:
   int a = 10;  // Variable 'a' is defined and initialized to 10

.. code-block:: cpp

   // Definition:
   // Variable 'b' is defined but not initialized.
   // if you try and use 'b' without giving it a value,
   // your program will crash!
   int a;

   // Usage
   a = 10;      // 'b' is assigned a value after definition

These two code blocks are functionally equivalent, but the first is
considered better practice because it ensures the variable has a valid
value from the start.

To sum this, **initialization** combines the steps of definition and
value assignment, while **definition** by itself only reserves memory
and specifies the type without assigning a value.

.. tip::

   In this course, you will mostly see variables being initialized when
   they are defined. This is because it is good practice to ensure that
   variables have a valid value before they are used. When you start to use
   :ref:`libraries` and more complex code, you will see variables being
   defined without being initialized.

   We will cover those cases when they come up.

Built-in Variables and Constants
--------------------------------

Arduino provides a set of predefined constants (variables that cannot
change) to simplify working with hardware components. These constants
are used to control pins, set input/output modes, and interact with
external devices.

.. seealso::

   You can view all the builtin constants `on the Arduino
   documentation <https://docs.arduino.cc/language-reference/#variables>`__,
   however, we will only be covering exactly what you need to know in this
   course.

``HIGH`` and ``LOW``
~~~~~~~~~~~~~~~~~~~~

Two of the most commonly used constants are ``HIGH`` and
``LOW``. These are used in conjunction with digital pins to
represent the states of those pins.

- ``HIGH``: Represents a digital signal of ``1`` or a voltage of
  approximately ``5V`` (on most boards). It's often used to turn on an
  LED, power a device, or indicate an active state.
- ``LOW``: Represents a digital signal of ``0`` or a voltage of
  ``0V``. It's typically used to turn off an LED, cut power, or indicate
  an inactive state.

When working with Arduino pins, these constants allow you to control
devices like LEDs, relays, or other components in an easy-to-read
manner:

.. code-block:: cpp

   digitalWrite(13, HIGH); // Turns on an LED connected to pin 13
   digitalWrite(13, LOW);  // Turns off the LED

In practical terms, ``HIGH`` and ``LOW`` correspond to the electrical
state of a given pin.

``INPUT`` and ``OUTPUT``
~~~~~~~~~~~~~~~~~~~~~~~~

In addition to ``HIGH`` and ``LOW``, Arduino provides two more
constants: ``INPUT`` and ``OUTPUT``. These constants are used to
set the mode of a pin, indicating whether it should be used for reading
input or writing output.

- ``INPUT``: Sets a pin as an **input**, allowing your code to read
  external signals or sensor data.
- ``OUTPUT``: Sets a pin as an **output**, enabling your code to send
  signals to external devices like LEDs, motors, or relays.

.. code-block:: cpp

   pinMode(2, INPUT);  // Sets pin 2 as an input
   pinMode(13, OUTPUT); // Sets pin 13 as an output


``LED_BUILTIN``
~~~~~~~~~~~~~~~

``LED_BUILTIN`` is a constant that represents the built-in LED on most
Arduino boards, including your Arduino Uno. This constant is useful when
you want to control the built-in LED without specifying a pin number.

.. code-block:: cpp

   digitalWrite(LED_BUILTIN, HIGH); // Turns on the built-in LED
   digitalWrite(LED_BUILTIN, LOW);  // Turns off the built-in LED

----

.. tip::

   ``HIGH`` / ``LOW`` and ``INPUT`` / ``OUTPUT`` will be covered in more detail when
   discussing controlling pins and
   interacting with external components in the :ref:`Your First
   Arduino Program <first_arduino_program>` section.

   These variables will be used extensively in your Arduino projects. Don't
   worry about memorizing them now; you'll become familiar with them over time.

.. _variable_scope:

Variable Scope
--------------

In programming, there are rules that determine where a variable can be
used in your code. This is known as **variable scope**. Understanding
variable scope is crucial, as it affects how you structure your programs
and how you manage data.

In Arduino, variables can have **global** scope or **local** scope, and the
distinction impacts how you structure your programs.

Global Scope
~~~~~~~~~~~~

Variables with global scope are declared outside of any function. They
can be accessed and modified by any part of the program, including all
functions.

**Example: Global Variable:**

.. whole-code-block:: cpp

   int counter = 0;  // Global variable

   void setup() {
      Serial.begin(9600);
   }

   void loop() {
      counter++;  // Increment the global counter
      Serial.println(counter);  // Accessible in loop()
      delay(1000);
   }

In this example, ``counter`` is accessible throughout the entire
program. However, overusing global variables can make debugging
difficult, as changes in one part of the code may unintentionally affect
another.

.. note::

   Typically global variables are defined using ``UPPER_SNAKE_CASE`` to
   distinguish them from local variables. This is a common convention in
   programming.

   .. code:: cpp

      int GLOBAL_VARIABLE = 0;

Local Scope
~~~~~~~~~~~

Variables with local scope are declared inside a function or block of
code (e.g., inside ``{}``). They are only accessible within that
specific function or block.

Example: Local Variable
^^^^^^^^^^^^^^^^^^^^^^^

.. whole-code-block:: cpp

   void setup() {
      Serial.begin(9600);
   }

   void loop() {
      int localCounter = 0;  // Local variable
      localCounter++;  // Increment local variable
      Serial.println(localCounter);  // Always prints 1
      delay(1000);
   }

Here, ``localCounter`` is recreated each time ``loop()`` runs, so its
value doesn't persist between iterations. This ensures that changes to
the variable do not affect other parts of the program.

Nested Functions and Variable Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Arduino, while you cannot define functions directly inside other
functions, you can create a structure where functions call other
functions. This allows for modular code while maintaining the scope of
variables within individual functions.

Example: Nested Function Calls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. whole-code-block:: cpp

   int calculateSum(int a, int b) {  // Function used within another function
      return a + b;
   }

   void printResult(int num1, int num2) {
      int sum = calculateSum(num1, num2);  // Call a helper function
      Serial.print("The sum of ");
      Serial.print(num1);
      Serial.print(" and ");
      Serial.print(num2);
      Serial.print(" is ");
      Serial.println(sum);
   }

   void setup() {
      Serial.begin(9600);
      printResult(5, 7);  // Prints: The sum of 5 and 7 is 12
   }

   void loop() {
      // No code needed here
   }

In this example:

- ``calculateSum`` is a helper function used by printResult.
- The variable ``sum`` is local to ``printResult`` and cannot be
  accessed outside of it, ensuring modularity and minimizing potential
  bugs.

Why Scope Matters
~~~~~~~~~~~~~~~~~

- **Avoiding Conflicts**: Keeping variables local where possible reduces
  the chances of accidental changes elsewhere in the program.
- **Improved Readability**: Local variables make it clear where and how
  a variable is used.
- **Memory Efficiency**: Local variables are created and destroyed as
  needed, reducing memory usage compared to global variables.

--------------

By carefully managing variable scope, you can write cleaner, more
efficient, and less error-prone programs. Aim to use global variables
sparingly and rely on local variables whenever possible for modular,
maintainable code.

Quiz
----

.. quizdown:: quizzes/variables_quiz.md
