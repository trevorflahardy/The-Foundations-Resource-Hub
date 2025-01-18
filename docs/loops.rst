.. _loops:

Loops
=====

What if we needed to repeat the same task over and over in your code?
For example, imagine you want to blink an LED on and off 10 times. You
might write something like this:

.. code:: cpp

   digitalWrite(13, HIGH);
   delay(500);
   digitalWrite(13, LOW);
   delay(500);
   digitalWrite(13, HIGH);
   delay(500);
   digitalWrite(13, LOW);
   delay(500);
   // ...repeat eight more times

It gets the job done, but that's a lot of repetitive code! It's not just
tedious—it's also inefficient. What if you wanted to blink the LED 100
times? Or change the timing later? You'd have to rewrite or modify the
same lines repeatedly, which makes your code harder to manage and more
prone to errors.

This is where ``loops`` come in. Loops let you write the repetitive part
of your program once and have the Arduino handle the repetition for you.
They're like your code's personal assistant, taking care of the
repetitive grunt work so you can focus on the bigger picture.

Using loops, we can easily repeat the blinking of an LED without having
to write the same lines of code over and over:

.. code:: cpp

   for (int i = 0; i < 10; i++) {
       digitalWrite(13, HIGH);
       delay(500);
       digitalWrite(13, LOW);
       delay(500);
   }

Much cleaner, right? Not only is the code easier to read, but it's also
more flexible—you can change the number of repetitions (10 in this case)
just by updating one number.

Every time the loop runs it is called an **iteration**. In this example,
the loop runs 10 times, so it has 10 iterations. This is the power of
loops: they let you repeat a block of code as many times as you need
without having to write it out each time.

But how do they work?

``for`` Loops
~~~~~~~~~~~~~

The ``for`` loop is a powerful tool when you know how many times you
want to repeat something.

The ``for`` loop uses a special variable (called a **loop variable**)
that you create to count how many times the loop has run. You name this
variable yourself (like ``i``, ``count``, or anything else), and the
loop updates it automatically during each repetition.

How ``for`` Loops Work
^^^^^^^^^^^^^^^^^^^^^^

A ``for`` loop has 3 main parts:

1. ``Initialization``: Sets a starting point for your loop.
2. ``Condition``: Checks whether the loop should continue.
3. ``Increment/Decrement``: Updates the loop variable after each
   iteration.

For Loop Syntax
^^^^^^^^^^^^^^^

.. code:: cpp

   for (initialization; condition; increment/decrement) {
       // Code to execute
   }

In this syntax:

- **``Initialization``**: Sets the loop variable to an initial value.
  This is usually where you create the loop variable and set its
  starting value.
- **``Condition``**: Checks whether the loop should continue. If the
  condition is true, the loop runs; if it's false, the loop stops.
- **``Increment/Decrement``**: Updates the loop variable after each
  iteration. This is where you increase or decrease the loop variable to
  move the loop forward.

For Loop Example
^^^^^^^^^^^^^^^^

LED Example
""""""""""""

For example, you can use a ``for`` loop to turn an LED on and off 5
times:

.. code:: cpp

   // Turn on LEDs connected to pins 2 through 6
   for (int pin = 2; pin <= 6; pin++) {
       digitalWrite(pin, HIGH);  // Turn on the LED
       delay(500);               // Wait for half a second
   }

Here, the for loop iterates (cycles) through pin numbers ``2`` to ``6``,
turning on each LED.

.. _for_loop_summing_numbers_example:

Summing Numbers Example
"""""""""""""""""""""""

As another example, let's say you wanted to add all the numbers in
an array together. You could use a ``for`` loop to iterate through the
array and add each number to a total:

.. code:: cpp

   int numbers[] = {1, 2, 3, 4, 5};
   int total = 0;

   for (int i = 0; i < 5; i++) {
      total += numbers[i];  // Add the current number to the total
   }

   Serial.println(total);  // Print the total
   >>> 15

.. _for_loop_fibonacci_example:

Fibonacci Example
"""""""""""""""""

Let's say you wanted to store the first 10 fibonacci numbers in an array. You could use a ``for`` loop to iterate through the array and calculate each number instead of manually writing each number:

.. code:: cpp

   int fibonacci[10];
   fibonacci[0] = 0;
   fibonacci[1] = 1;

   for (int i = 2; i < 10; i++) {
      fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
   }

   for (int i = 0; i < 10; i++) {
      Serial.println(fibonacci[i]);
   }

``while`` loops
~~~~~~~~~~~~~~~

A ``while`` loop is ideal for situations where you don't know in advance
how many times a task needs to repeat. Unlike a ``for`` loop, which runs
a set number of times, a ``while`` loop keeps going **as long as its
condition evaluates to true**.

The key feature of a ``while`` loop is its **condition**—a boolean
expression that is checked at the start of each loop iteration. If the
condition is ``true``, the loop runs; if it's ``false``, the loop stops.

This makes ``while`` loops great for tasks where the stopping point
depends on a dynamic or unpredictable factor, like user input or sensor
readings.

How ``while`` Loops Work
^^^^^^^^^^^^^^^^^^^^^^^^

A while loop has 2 main parts:

1. **``Condition``**: The loop checks a condition before every
   iteration. If the condition is false, the loop exits immediately.
2. **``Repetition``**: If the condition is true, the code inside the
   loop executes and then rechecks the condition.

While Loop Syntax
^^^^^^^^^^^^^^^^^

.. code:: cpp

   while (condition) {
       // Code to execute
   }

While Loop Example 1: Waiting for a Button Press
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To see a ``while`` loop in action, let's assume that we want to wait for
a button press before continuing with our program. We can use a
``while`` loop to keep checking the button state until it's pressed.

For this example, assume that the button is connected to pin 7, and we
want to wait until the button is pressed before moving on.

.. code:: cpp

   int buttonState = LOW;

   // Keep looping until the button is pressed:
   while (buttonState == LOW) {
       buttonState = digitalRead(7); // Check the button state on pin 7

       if (buttonState == LOW) {
           // If the buttonState is LOW (ie. no one has pressed it),
           // then let the user know we're waiting for a button press.
           Serial.println("Waiting for button press...");
       }

       delay(100); // Small delay to reduce rapid checking
   }

   Serial.println("Button pressed!");

In this example:

- The loop keeps running while ``buttonState`` is ``LOW`` (button not
  pressed).
- Once the button is pressed (``buttonState`` becomes ``HIGH``), the
  loop exits, and the program continues.

While Loop Example 2: Countdown Timer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can also use a ``while`` loop to create a countdown timer. For
example, let's count down from 10 to 1, printing each number to the
Serial Monitor and then printing “Liftoff!” when the countdown reaches
0.

.. code:: cpp

   int countdown = 10;

   while (countdown > 0) {              // Keep looping until the countdown reaches 0
       Serial.println(countdown);       // Print the current countdown value
       delay(1000);                     // Wait 1 second
       countdown--;                     // Decrease the countdown by 1
   }

   Serial.println("Liftoff!");

Here:

- The loop starts with ``countdown = 10`` and repeats until
  ``countdown > 0`` is false.
- On each iteration, the value of ``countdown`` decreases by 1.

When you run this program, you'll see the countdown from 10 to 1, with
each **iteration** taking 1 second, followed by “Liftoff!” when the
countdown reaches 0. The program will run for 10 seconds in total.

   If you haven't noticed, this example can also be done with a ``for``
   loop! The choice between ``for`` and ``while`` loops depends on the
   specific task you're trying to accomplish.

   .. code:: cpp

      for (int i = 10; i > 0; i--) { // From 10 to 1
          Serial.println(i); // Print the current countdown value
          delay(1000); // Wait 1 second
      }

While Loop Key Points
^^^^^^^^^^^^^^^^^^^^^

- Make sure the condition will *eventually* become false; otherwise, the
  loop will run forever (infinite loop). For example:

  .. code:: cpp

     while (true) {
         // This will run forever unless you break the loop manually
     }

- Use a delay or modify the condition inside the loop to prevent
  unnecessary CPU usage or infinite looping.

With ``while`` loops, you have flexibility for dynamic, real-time
decision-making, making them powerful for tasks like waiting for an
input or monitoring a sensor.

Why Use Loops?
~~~~~~~~~~~~~~

Think of loops as the “secret sauce” to efficient coding. They save you
time, reduce errors, and make your code adaptable to change.

- **for Loops**: Use these when you know in advance how many times you
  want to repeat something, like iterating through an array or cycling
  through a fixed number of pins.
- **while Loops**: These are ideal for conditions that depend on
  real-time input, such as waiting for a sensor to detect a specific
  value or monitoring a button press.

Break and Continue Statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you need to break out of a loop early or skip an iteration
based on a specific condition. This is where **``break``** and
**``continue``** statements come in.

- **``break``**: Exits the loop immediately, regardless of the loop
  condition.
- **``continue``**: Skips the rest of the current iteration and moves to
  the next one.

These statements give you more control over the flow of your loops,
allowing you to fine-tune your code based on specific conditions.

Break Statement Example
^^^^^^^^^^^^^^^^^^^^^^^

Let's say we wanted to continue looping until we found a specific
number, then exit the loop early. We can use the ``break`` statement to
do this.

.. code:: cpp

   int number_to_find = 5;

   for (int i = 0; i < 10; i++) {
       Serial.println(i);

       if (i == number_to_find) {
           Serial.println("Number found!");
           break;  // Exit the loop early
       }
   }

   Serial.println("Loop finished!");

In this example, the loop is set to run from ``0`` to ``9``, printing
each number. When ``i`` equals ``number_to_find`` (5), the loop exits
early with the ``break`` statement. The program then prints “Number
found!” and “Loop finished!”.

So, when you run this program, you'll see:

.. code:: cpp

   0
   1
   2
   3
   4
   5
   Number found!
   Loop finished!

Continue Statement Example
^^^^^^^^^^^^^^^^^^^^^^^^^^

``continue`` is similar to ``break``, however, ``continue`` will simply
skip to the next loop iteration instead of stopping the loop. Let's say
that we hate ANY number that ends in ``5``. We can use the ``continue``
to skip any number that ends in ``5``.

.. code:: cpp

   int number_we_hate = 5;

   for (int i = 0; i < 10; i++) {
       if (i % 10 == number_we_hate) {
           Serial.println("We hate number: " + i);
           continue;  // Skip this iteration
       }

       Serial.println(i);
   }

This program will print every number from ``0`` to ``9``, except for
``5``. When you run this program, you'll see:

.. code:: cpp

   0
   1
   2
   3
   4
   We hate number: 5
   6
   7
   8
   9

.. note::

   Note how the use of the modulus (``%``) operator is used here. As
   mentioned in `Math Operations <#math-operations>`__, the modulus
   operator returns the remainder of a division operation. Consider if
   we made the loop go all the way to 20 instead of 10. When we hit 15,
   ``15 % 10`` is ``5``, so the program would skip printing ``15`` as
   well. The same would happen for ``25``, ``35``, etc.

--------------

You can use ``continue`` and ``break`` with both ``for`` and ``while``
loops. These statements give you more control over the flow of your
loops, allowing you to fine-tune your code based on specific conditions.

Loops vs. ``loop()``
~~~~~~~~~~~~~~~~~~~~

The loop() function and for/while loops serve different purposes in
Arduino programming.

- The ``loop()`` function is a special system function that runs
  indefinitely on your Arduino board, cycling through its code block as
  long as the board has power. It handles the overarching repetition of
  your program.
- A ``for`` or ``while`` loop, on the other hand, performs controlled
  repetitions of specific tasks within the ``loop()`` function or
  elsewhere in your code.

.. code:: cpp

   void loop() {
       // This is the `loop()` function that runs indefinitely.

       // Example of a `for` loop within `loop()`
       for (int i = 0; i < 3; i++) {
           Serial.println(i);  // Prints 0, 1, 2
       }

       // Example of a `while` loop within `loop()`
       int x = 0;
       while (x < 3) {
           Serial.println(x);  // Prints 0, 1, 2
           x++;
       }
   }

**Remember**: Think of loop() as your program's big picture cycle, while
for and while loops handle specific, smaller repetitions inside it.