.. _code_disclaimer:

Code Disclaimer
===============

Throughout this guide, you'll encounter example code blocks; these are designed to illustrate specific concepts. **Every code block will not work if copied directly into the Arduino IDE**, unless specifically noted otherwise. This is because,

- Arduino programs require special setup code (like ``setup()`` and ``loop()``) that isn't always included in examples.
- Many examples omit boilerplate code to focus on the new concept being taught.

When you see these whole code blocks, consider them as building blocks that will be used to expand your understanding. Whole examples are commonly incorporated into this book's full examples, so you can see how they fit into a complete program.

Whole Code Blocks
------------------

Some sections will explicitly state when you should follow along in your IDE. These examples will include complete, runnable code. **Only when you see a whole code block can you copy paste it into your Arduino IDE**. For example:

.. whole-code-block:: cpp

    void setup() {
        pinMode(13, OUTPUT);  // Set pin 13 as an output
    }

    void loop() {
        digitalWrite(13, HIGH);  // Turn on the LED
        delay(1000);             // Wait 1 second
        digitalWrite(13, LOW);   // Turn off the LED
        delay(1000);             // Wait 1 second
    }

When you see such complete examples, feel free to copy them into the Arduino IDE and experiment! For whole examples, consider them as building blocks that will be used to expand your understanding. Whole examples are commonly incorporated into this book's full examples, so you can see how they fit into a complete program.