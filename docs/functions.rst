.. _functions:

Functions
=========

Sometimes in programming, we need to repeat a set of instructions
multiple times. Instead of writing the same code over and over, we can
use **functions** to group these instructions together and call them
whenever needed. Functions are a fundamental concept in programming,
allowing you to create reusable blocks of code that perform specific
tasks.

What is a Function?
-------------------

A **function** is a reusable block of code designed to perform a
specific task. Functions allow you to break down your program into
smaller, more manageable parts, making it easier to read, debug, and
reuse code.

Functions in programming are similar to functions in mathematics.
Consider the math function ``f(x) = x^2``, something you have seen many
times. This function takes an input ``x``, squares it, and returns the
result. In programming, functions work similarly: they take input values
(called **parameters**), perform operations, and return a result.

In Arduino programming, functions play a key role in structuring your
code. By creating your own functions, you can define additional
behaviors and organize your code effectively.

Anatomy of a Function
---------------------

A function typically consists of the following parts:

1. **Return Type**: Specifies the `type <#data-types>`__ of value the
   function will return (e.g., ``int``, ``float``, ``void`` for no
   return).
2. **Function Name**: A unique identifier for the function, used to call
   it.
3. **Parameters**: Input values passed to the function, enclosed in
   parentheses.
4. **Body**: The block of code executed when the function is called,
   enclosed in curly braces ``{}``.

Here's an example of a simple function:

.. code:: cpp

   int addNumbers(int a, int b) {
       return a + b; // Returns the sum of a and b
   }

Breaking this down, we see that the function ``addNumbers`` has the
following components:

- ``int``: The **return** `type <#data-types>`__, indicating the
  function will return an integer.
- ``addNumbers``: The **function name**.
- ``int a``, ``int b``: **Parameters** for input values, specifying two
  integers. Notice how this is similar to defining variables. This
  simply means that the function expects to integers to be passed to it
  when it is called; and these integers will be referred to as ``a`` and
  ``b`` within the function.
- ``return a + b;``: The **body**, which adds the parameters and returns
  the result.

When we **call** this function, or when we use it in our code, we
provide the values for ``a`` and ``b`` and the function returns the sum
of these values (an integer).

.. code:: cpp

   addNumbers(5, 3); // Calls the function with 5 and 3

But wait! What happens when we call this function? How do we use the
result of the function? Well, we can store the result of the function in
a variable!

.. code:: cpp

   int sum = addNumbers(5, 3); // Calls the function with 5 and 3.

In this example, the function ``addNumbers`` is called with the values
``5`` and ``3``. The function adds these values together and returns the
result, which is then stored in the variable ``sum``.

--------------

Functions don't have to just take and return numbers, though, they can
take and return any `data type <#data-types>`__!

Let's say we wanted to create a function that multiplies two numbers
together. But, we want to multiply two decimal numbers, not integers. We
can do this by changing the data type of the parameters and return type
of the function.

.. code:: cpp

   float multiply(float x, float y) {
       return x * y; // Returns the product of x and y
   }

   float result = multiply(3.5, 2.0); // Calls the function with 3.5 and 2.0

Notice how the function ``multiply`` takes two ``float`` parameters and
returns a ``float`` value. This allows us to multiply decimal numbers
together and get a decimal result.

We could also check if a number is positive:

.. code:: cpp

   bool isPositive(int number) {
       // Check if this number is greater than 0 and store it in a variable.
       // See the section on "Boolean Logic" for more information on this comparison.
       // Hint: It's the same as in Math class!
       bool numberIsPositive = number > 0;

       // Return this boolean value. So, true if positive and false otherwise.
       return numberIsPositive;
   }

   int someNumber = 10; // Number to check
   bool result = isPositive(someNumber); // Calls the function with 10

In this example, the function ``isPositive`` takes only one parameter,
an ``int``, and returns a ``bool`` (true or false) value. The function
checks if the number is greater than ``0`` and returns ``true`` if it
is, and ``false`` otherwise.

.. note::

   **Advanced: Shorthand [OPTIONAL]**: You should shorthand the
   isPositive function as common practice,

   \```cpp bool isPositive(int number) { return number > 0; };

Functions can also accept arrays as parameters, allowing you to pass
multiple values to a function. For example, you could create a function
to set the first element of an array to a specific value:

.. code:: cpp

   void setFirstElement(int array[], int value) {
       array[0] = value; // Sets the first element of the array to the specified value
   }

   int myArray[3] = {1, 2, 3}; // Array to modify
   setFirstElement(myArray, 10); // Sets the first element to 10

   // We can use this function as many times as we want! So,
   // if we wanted to overwrite the first element with 20, we can do that too!
   setFirstElement(myArray, 20); // Sets the first element to 20
   >>> myArray == 20

Hold on! There are two important things in the ``setFirstElement``
function!

- What does ``void`` mean? ``void`` is a return type that indicates the
  function does not return a value. This is used when the function
  performs an action but doesn't need to return a result.
- What's up with ``int array[]``? This is a way to pass an array to a
  function. The function expects an array of integers, and the ``[]``
  indicates that it's an array. The function can then access and modify
  the array's elements. Note how this is similar to making an array
  variable, but in this case, we're passing the array to a function.

Calling a Function
------------------

As shown in the examples above, when you “**call**” a function, you are
telling the program to execute the code inside of the function. A
function may, depending on its design, take input values (parameters)
and return a result.

To call a function, you use the function name followed by parentheses
``()``. If the function expects parameters, you provide them inside the
parentheses. If the function returns a value, you can store it in a
variable or use it directly in your code.

.. code:: cpp

   int sum = addNumbers(5, 3); // Calls the function named 'addNumbers' with 5 and 3

When you call a function, you must provide the required parameters in
the correct order. For example, if a function expects two integers, you
must pass two integers when calling it:

.. code:: cpp

   int addNumbers(int a, int b) {
       return a + b;
   }

   int sum = addNumbers(5, 3); // Calls the function with 5 and 3

   int this_fails = addNumbers(5); // Error! The function expects two integers.
   int this_also_fails = addNumbers(5, 3, 2); // Error! The function expects two integers.

Built-in vs. User-Defined Functions
-----------------------------------

In Arduino programming, functions can be divided into two categories:
**built-in** and **user-defined**.

--------------

Built-in Functions
~~~~~~~~~~~~~~~~~~

Arduino provides a library of built-in functions to handle common tasks.
These functions are pre-defined, so you don't need to write them
yourself, just call them when needed. Here are some important functions
you'll use frequently:

- **``digitalRead(pin)``**: Reads the digital state (HIGH or LOW) of a
  specified pin on the Arduino board. Example:

  .. code:: cpp

     int buttonState = digitalRead(2); // Reads the state of pin 2
     Serial.println(buttonState); // Prints the state to the Serial Monitor

- **``digitalWrite(pin, value)``**: Sets the specified pin on the
  Arduino board to ``HIGH`` or ``LOW``. Example:

  .. code:: cpp

     digitalWrite(13, HIGH); // Turns on an LED connected to pin 13

- **``analogRead(pin)``**: Reads the analog value (0-1023) from an
  analog pin on the Arduino board. Example:

  .. code:: cpp

     int sensorValue = analogRead(A0); // Reads the value from analog pin A0

- **``analogWrite(pin, value)``**: Writes an analog value (PWM signal)
  to a specified pin on the Arduino board. Example:

  .. code:: cpp

     analogWrite(9, 127); // Writes a PWM signal to pin 9

- **``delay(milliseconds)``**: Pauses the program for the specified
  time. Example:

  .. code:: cpp

     delay(1000); // Pauses the program for 1 second

- **``pinMode(pin, mode)``**: Sets a pin on your Arduino board as either
  an ``INPUT`` or ``OUTPUT``. Example:

  .. code:: cpp

     pinMode(7, OUTPUT); // Sets pin 7 as an output

Special Built-in Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

``setup()`` and ``loop()``
''''''''''''''''''''''''''

Some built-in functions in Arduino are so critical that they form the
backbone of every program. Two of these functions—``setup()`` and
``loop()``—are automatically called by the Arduino board and are present
in every sketch. These functions structure your program and define its
behavior.

What do these functions do?

1. **``setup()``** The ``setup()`` function runs **once** when the
   Arduino board is powered on or reset. This is where you initialize
   settings like pin modes, Serial communication, or any one-time setup
   tasks.

   Example:

   .. whole-code-block:: cpp

      void setup() {
         pinMode(13, OUTPUT);   // Set pin 13 as an output
         Serial.begin(9600);   // Start Serial communication
      }

2. **``loop()``** The ``loop()`` function runs **continuously** after
   ``setup()`` finishes. It acts as the main cycle of your program,
   where tasks are repeated indefinitely. This is where you define
   ongoing behaviors, like blinking an LED, checking sensor inputs, or
   controlling a motor.

   Example:

   .. whole-code-block:: cpp

      void loop() {
         digitalWrite(13, HIGH);  // Turn the LED on
         delay(1000);             // Wait 1 second
         digitalWrite(13, LOW);   // Turn the LED off
         delay(1000);             // Wait 1 second
      }

--------------

**Key Distinctions Between ``setup()`` and ``loop()``**

While both functions are essential, their purposes are distinct:

- ``setup()``: Executes once for initialization tasks.
- ``loop()``: Executes repeatedly to handle ongoing tasks.

Here's a helpful analogy:

   Think of ``setup()`` as the “start-up checklist” for your
   Arduino—setting up everything it needs before it starts working.
   ``loop()`` is like the machine's operating cycle, running
   continuously to keep things functioning.

``Serial.print()`` and ``Serial.println()``
'''''''''''''''''''''''''''''''''''''''''''

The **Serial Monitor** is one of your most valuable tools for debugging
and monitoring your Arduino programs. The functions ``Serial.print()``
and ``Serial.println()`` allow you to send data to the Serial Monitor
for display.

**How They Work:**

- ``Serial.print()``: Outputs text or data to the Serial Monitor without
  moving to the next line.
- ``Serial.println()``: Outputs text or data and then moves to the next
  line, making it easier to format output.

**Example**:

.. code:: cpp

   Serial.print("Temperature: ");
   Serial.println(25);
   >>> Temperature: 25

**Comparison Example:** The difference between ``print`` and
``println``:

.. code:: cpp

   Serial.print("Arduino ");
   Serial.print("is ");
   Serial.print("awesome!");
   >>> Arduino is awesome!

   Serial.println("This is a new line.");
   >>> This is a new line.

``Serial.begin()``
''''''''''''''''''

The ``Serial.begin()`` function initializes Serial communication. You
must include this function in setup() to enable data transfer between
the Arduino and the Serial Monitor.

**Example**:

.. code:: cpp

   void setup() {
       Serial.begin(9600);  // Initialize Serial communication at 9600 baud
   }

..

.. note::

   **Advanced: Baud Rate (Optional)**: The ``9600`` in
   ``Serial.begin(9600)`` specifies the baud rate—the speed of
   communication. Both the Arduino and the Serial Monitor must use the
   same baud rate to communicate correctly. The default baud rate for
   most projects is ``9600``.

--------------

**Important Reminder**: While these built-in functions are critical to
Arduino programming, understanding how to structure your program with
``setup()`` and ``loop()`` is foundational. Make sure you're comfortable
with their roles before diving deeper into control structures and
advanced topics.

User-Defined Functions
~~~~~~~~~~~~~~~~~~~~~~

In Arduino programming, **user-defined functions** are custom blocks of
code that you create to perform specific tasks. Unlike built-in
functions, which are pre-programmed into the Arduino framework (e.g.,
``digitalWrite()``, ``delay()``), user-defined functions are written
entirely by you to meet the unique needs of your program.

How Are User-Defined Functions Different from Built-In Functions?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

- **Built-In Functions**: These come prepackaged with the Arduino
  library, providing functionality like controlling pins
  (``digitalWrite``), reading sensors (``analogRead``), or handling
  delays (``delay``). You don't need to write them—they're ready to use.
- **User-Defined Functions**: These are custom functions you create to
  organize and encapsulate tasks specific to your program. They allow
  you to implement behaviors that are not directly available through
  built-in functions.

For example, while ``digitalWrite`` controls a pin, you might create a
user-defined function like blinkLED to toggle an LED on and off in a
structured way.

Why Do We Need User-Defined Functions?
''''''''''''''''''''''''''''''''''''''

- **Encapsulation**: Combine multiple related instructions into a single
  function, reducing repetition.
- **Readability**: Give meaningful names to tasks, making your code
  easier to understand.
- **Reusability**: Use the same function multiple times in different
  parts of the program, avoiding duplication.
- **Debugging**: Simplify troubleshooting by isolating logic into
  self-contained blocks.

Example: Organizing Code with User-Defined Functions
''''''''''''''''''''''''''''''''''''''''''''''''''''

Let's consider a scenario where you want to blink an LED with varying
delays. Instead of duplicating the same instructions repeatedly, you can
encapsulate the behavior in a user-defined function.

.. whole-code-block:: cpp

   void blinkLED(int pin, int delayTime) {
      digitalWrite(pin, HIGH);  // Turn LED on
      delay(delayTime);         // Wait for delayTime milliseconds
      digitalWrite(pin, LOW);   // Turn LED off
      delay(delayTime);         // Wait again
   }

   void setup() {
      pinMode(13, OUTPUT);  // Set pin 13 as output
   }

   void loop() {
      blinkLED(13, 500);  // Blink with 500ms delay
      blinkLED(13, 1000); // Blink with 1000ms delay
   }