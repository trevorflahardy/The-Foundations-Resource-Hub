.. _basic_arduino_structure:

Basic Arduino Structure
========================

The Arduino programming language is based on C++, with a simplified structure to make it beginner-friendly. It has a few key conventions and rules that you should know before diving into coding. Here's an overview of the foundational *ideas* of Arduino syntax:

Basic Syntax Rules
------------------

.. hint::

   Focus on the concepts and structure of the code, rather than the specific details. We will cover each of these elements in more detail as we progress through the book.

#. **Case Sensitivity**: Arduino code is case-sensitive. This means ``PinMode``, ``pinmode``, and ``pinMode`` are all treated as different terms. Always pay attention to capitalization.

   .. code:: cpp

      pinMode(13, OUTPUT);  // Correct
      PinMode(13, OUTPUT);  // Incorrect

#. **Semicolons (;)**: Every statement in Arduino code must end with a semicolon. This tells the compiler where each instruction ends.

   .. code:: cpp

      digitalWrite(13, HIGH);  // Correct
      digitalWrite(13, HIGH)   // Missing semicolon, will cause an error

#. **Curly Braces** (``{}``): Curly braces group code into **blocks**, such as for functions, loops, or conditional statements. Each opening brace ``{`` must have a matching closing brace ``}``.

   .. code:: cpp

      void loop() {
          digitalWrite(13, HIGH);  // Code inside loop()
      }  // Matching closing brace

   A **block** is a group of statements that are treated as a single unit. Blocks are used to define functions, loops, conditional statements, and other structures in Arduino code, all of which we will cover as we go along.

#. **Indentation and Whitespace**: Whitespace (spaces, tabs, or empty lines) **does not affect how the code runs** but is critical for readability. Proper indentation helps you and others understand the structure of the code.

   .. code:: cpp

      // Example of well-formatted code
      void loop() {
           if (millis() % 2 == 0) {
               digitalWrite(13, HIGH);
         } else {
               digitalWrite(13, LOW);
         }
      }


Comments and Code Readability
-----------------------------

It's also essential to understand
how to document your thoughts within your code—comments are the first
step in bridging the gap between your ideas and the logic you build.
Comments are a critical part of writing clean, maintainable code. They
allow you to explain what your code does, why it exists, or how it
should be used. While they don't affect the execution of the program,
they can make your code much easier for you—and others—to understand
later.

Single Line Comments
~~~~~~~~~~~~~~~~~~~~

Single-line comments start with ``//`` and extend to the end of the
line. These are perfect for brief explanations or notes:

.. code:: cpp

   // This is a single-line comment
   int number = 42; // This is another single-line comment

Multi-Line Comments
~~~~~~~~~~~~~~~~~~~

Multi-line comments start with ``/*`` and end with ``*/``. They can span
multiple lines and are useful for longer explanations or temporarily
disabling blocks of code:

.. code-block:: cpp

   /* This is a multi-line comment
      that spans multiple lines. */
   int number = 42;

Why is Commenting Important?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comments serve several key purposes:

#. **Improves Code Readability**: Comments make it easier to understand what the code is doing, especially for complex sections.
#. **Aids Debugging**: Well-placed comments help you locate issues or make changes without breaking the program.
#. **Facilitates Collaboration**: When you are working in a team, comments ensure that others can understand and use your code.
#. **Future-Proofing**: Even for your own code, comments can serve as reminders for why you wrote something a certain way.

In the examples throughout this book, comments are used to emphasize key
points, explain code snippets, and provide additional context. As you
write your own programs, consider how comments can help you organize
your thoughts and communicate your ideas effectively.

Best Practices for Commenting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Be concise but informative. Avoid stating the obvious.

  Example of a **bad** comment:

  .. code:: cpp

     int x = 42; // Assigns 42 to x

  Better comment:

  .. code:: cpp

     int delayTime = 1000; // Time in milliseconds for the LED to stay on

- Keep comments up to date. If the code changes, revise the comments to
  reflect the new logic.

- Use comments to explain *why* the code is doing something, not just
  *what* it does.

By incorporating thoughtful comments into your code, you'll create
programs that are not only functional but also accessible and easy to
manage.

Quiz
----

.. quizdown:: quizzes/basic_structure_quiz.md
