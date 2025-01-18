.. _control_structures:

Control Structures
==================

Often in our programs we need to make decisions, repeat actions, or
manage the flow of execution. This is where **control structures** come
in. Control structures allow your program to adapt dynamically, making
decisions based on specific conditions or events.

What are Control Structures?
----------------------------

**Control structures** are fundamental tools that allow your program to
make decisions, repeat actions, and manage the flow of execution. In
essence, they define the logic that determines how your code behaves
based on different conditions or events. Think of them as road signs
guiding your program through various paths depending on specific inputs
or states.

Control structures can be categorized into:

- **Conditional statements**: Allow decision-making based on whether a condition is ``true`` or ``false``.
- **Loops**: Enable repeating actions until a certain condition is met or for a specified number of iterations.
- **Jump statements**: Manage the flow of control by breaking out of or skipping parts of the code.

These tools empower your program to adapt dynamically, ensuring it can
respond intelligently to varying inputs or environments.

Conditional Statements
----------------------

Conditional statements allow your code to make decisions based on
certain conditions, enabling more dynamic behavior. The three main
components are ``if``, ``else if``, and ``else`` blocks.

**``if`` Statements**
~~~~~~~~~~~~~~~~~~~~~

The ``if`` statement checks a boolean condition and executes the code
inside its block only if the condition evaluates to ``true``. For
example,

.. code:: cpp

    int temperature = 90; // Temperature value

    if (temperature > 70) {
        Serial.println("Turn on the fan!");
    }

    >>> Turn on the fan!

In this example, if the ``temperature`` is greater than 70, the message
“Turn on the fan!” is printed to the Serial Monitor.

The syntax for an ``if`` statement is:

.. code:: cpp

    if (condition) {
        // Code to run if the condition is true
    }

where ``condition`` is a boolean expression that evaluates to ``true``
or ``false``. If the condition is ``true``, the code inside the block is
executed. If the condition is ``false``, the code is skipped. The block
is enclosed in curly braces ``{}`` to define the scope of the ``if``
statement.

If statements can only check ``true`` or ``false`` conditions.

**``else`` Statements**
~~~~~~~~~~~~~~~~~~~~~~~

What if the condition is ``false``, what if I want to do something else?
This is where the ``else`` statement comes in. The ``else`` statement
runs a block of code if the ``if`` condition is ``false``. For example,

.. code:: cpp

    int temperature = 20; // Temperature value

    if (temperature > 90) {
        Serial.println("Turn on the fan!");
    } else {
        Serial.println("Temperature is just right!");
    }

    >>> Temperature is just right!

In this example, if the temperature is neither above 90 nor below 10,
the message “Temperature is just right!” is printed.

The syntax for an ``else`` statement is:

.. code:: cpp

    if (condition) {
        // Code to run if the condition is true
    } else {
        // Code to run if the condition is false
    }

The ``else`` block is executed only if the ``if`` condition is
``false``. This allows you to define an alternative action when the
initial condition is not met.

**``else if`` Statements**
~~~~~~~~~~~~~~~~~~~~~~~~~~

How can I check multiple conditions? This is where the ``else if``
statement comes in. The ``else if`` statement allows you to check
additional conditions after the initial ``if`` statement. For example,

.. code:: cpp

    int temperature = 5; // Temperature value

    if (temperature > 90) {
        Serial.println("Turn on the fan!");
    } else if (temperature < 10) {
        Serial.println("Turn on the heater!");
    } else {
        Serial.println("Temperature is just right!");
    }

    >>> Turn on the heater!

In this example, if the temperature is below 10, the message “Turn on
the heater!” is printed. The ``else if`` block is only executed if the
initial ``if`` condition is false.

The syntax for an ``else if`` statement is:

.. code:: cpp

    if (condition1) {
        // Code to run if condition1 is true
    } else if (condition2) {
        // Code to run if condition1 is false and condition2 is true
    } else {
        // Code to run if all conditions are false
    }

The ``else if`` block is evaluated only if the preceding ``if`` or
``else if`` conditions are false. This allows you to check multiple
conditions in sequence and execute different code based on the results.

You can have as many ``else if`` blocks as you need to handle different
scenarios. The ``else`` block is optional and runs only if all preceding
conditions are false.

.. code:: cpp

    int temperature = 20; // Temperature value

    if (temperature > 90) {
        Serial.println("Turn on the fan!");
    } else if (temperature < 10) {
        Serial.println("Turn on the heater!");
    } else if (temperature == 20) {
        Serial.println("Temperature is 20 degrees!");
    } else {
        Serial.println("Temperature is just right!");
    }

    >>> Temperature is 20 degrees!

Single Comparisons
------------------

As you've noticed, **conditional statements** (code that evaluates to
``true`` or ``false``) are at the heart of control structures. These
statements allow your program to make decisions based on specific
conditions, enabling dynamic behavior.

Comparisons are at the heart of conditional statements. These are very
similar to what you've seen in math class, but with a few differences.
Here are the main comparison operators in Arduino:

- **``==``**: Checks if two values are equal. Note that we use ``==``
  instead of ``=`` to avoid confusion with the assignment operator when
  comparing values.
- **``!=``**: Checks if two values are not equal.
- **``<``**: Checks if the left value is less than the right value.
- **``>``**: Checks if the left value is greater than the right value.
- **``<=``**: Checks if the left value is less than or equal to the
  right value.
- **``>=``**: Checks if the left value is greater than or equal to the
  right value.

These operators are used to compare values and determine the flow of
your program based on the results.

For example:

.. code:: cpp

    if (buttonState == HIGH) {
        // Code to run when the button is pressed
        Serial.println("Button is pressed!");
    }

You can also assign the result of a comparison to a variable:

.. code:: cpp

    bool isButtonPressed = buttonState == HIGH;
    if (isButtonPressed) {
        // Code to run when the button is pressed
        Serial.println("Button is pressed!");
    }

It's common to do this when you need check the same condition multiple
times in your program, or if a condition is complex and you want to
break it down into simpler, easier-to-understand parts.

Logical (Boolean) Operators
---------------------------

**Logical operators** allow you to combine multiple conditions in a
single statement. The main logical operators are:

- **``&&`` (AND)**: Returns true if **both** conditions are true.
- **``||`` (OR)**: Returns true if **at least one** condition is true.
- **``!`` (NOT)**: Reverses the logical state of a condition.

These operators are used to create more complex conditions that can
handle multiple scenarios.

.. seealso::

   You can find all these operators on the `Arduino Language
   Reference <https://docs.arduino.cc/language-reference/#structure>`__,
   however, you do not need to know all them for this course.

For example:

.. code:: cpp

    if (temperature > 90 && humidity < 50) {
        // Code to run when the temperature is above 90
        // AND the humidity is below 50%
    }

In this example, the code inside the if block runs only if the
temperature is above 90 degrees **and** the humidity is below 50%.

.. code:: cpp

    if (buttonState == HIGH || switchState == LOW) {
        // Code to run when the button is pressed
        // OR the switch is off
    }

In this example, the code inside the if block runs if the button is
pressed **or** the switch is off.

.. code:: cpp

    if (!(temperature > 90)) {
        // Code to run when the temperature is not above 90
    }

In this example, the code inside the if block runs if the temperature is
**not** above 90 degrees. That example can be confusing, so let's break
it down by splitting the ``!`` operator into a separate variable:

.. code:: cpp

    bool temperatureGreaterThan30 = temperature > 90;
    bool notGreaterThan30 = !temperatureGreaterThan30;
    if (notGreaterThan30) {
        // Code to run when the temperature is not above 30
    }