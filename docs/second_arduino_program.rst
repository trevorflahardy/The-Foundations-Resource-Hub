.. _your-second-arduino-program:

Your Second Arduino Program
===========================

With your Arduino Uno plugged into your computer, do you see the green
light on your Arduino board? That's the onboard LED, and we can control
it with our code! Let's write a program that turns the LED on and off
every second. In doing so, we're going to use some functions we saw
earlier: ``digitalWrite()`` and ``delay()``.

Step 1. Change the Code
-----------------------

Let's edit the code you already have from `your first Arduino
program <#your-first-arduino-program>`__.

You know that the ``loop()`` function runs continuously, so we can use
it to turn the LED on and off. Here's the updated code:

.. whole-code-block:: cpp

   void setup() {
      // Initialize Serial communication. Same as before, every
      // program has this in the setup.
      Serial.begin(9600);

      // Set the LED pin as an output. IE, tell the Arduino that
      // we want to SEND data to the LED. On the Arduino Uno,
      // pin 13 is connected to the onboard LED. Whenever we
      // send a HIGH signal to pin 13, the LED turns on.
      pinMode(13, OUTPUT);
   }

   void loop() {
      // Instead of printing a message, we're going to turn the LED on,
      // wait for 1 second, turn it off, and wait for another second.

      // Turn the LED on by sending a HIGH signal to pin 13.
      digitalWrite(13, HIGH);

      // Wait for 1 second (1000 milliseconds). Remember this
      // from the delay() function we learned about earlier?
      delay(1000);

      // Turn the LED off by sending a LOW signal to pin 13.
      digitalWrite(13, LOW);

      // Wait for another second.
      delay(1000);
   }

Let's break this down! In the ``setup()`` function, we're initializing
the Serial communication and setting pin 13 as an output. This tells the
Arduino that we want to send data to the LED connected to pin 13.

Next, in the ``loop()`` function, we're turning the LED on by sending a
``HIGH`` signal to pin 13 using ``digitalWrite(13, HIGH)``. We then wait
for 1 second using ``delay(1000)`` before turning the LED off by sending
a ``LOW`` signal to pin 13 with ``digitalWrite(13, LOW)``. We wait for
another second before repeating the process.

Why does this make the LED blink if we only turn it on and off one time?
This is because the ``loop()`` function runs continuously, so the LED
will turn on, wait for a second, turn off, wait for a second, and then
repeat the process indefinitely. This is why the LED blinks on and off
every second.

Step 2. Upload and Run the Program
----------------------------------

This step is the same as in the `example
before <#step-4-upload-and-run-the-program>`__, except this time, you're
controlling the onboard LED on your Arduino board and not printing
messages to the Serial Monitor.

Follow the same steps to upload the code to your Arduino Uno and open
the Serial Monitor to see the LED blink on and off every second.

Step 3. Update your Code to Print Messages
------------------------------------------

As a challenge, update your program to print messages to the Serial
Monitor when the LED turns on and off. This will help you understand the
relationship between the code you write and the actions you see on your
Arduino board.

.. raw:: html

   <details open>

.. raw:: html

   <summary>

Want to see the solution?

.. raw:: html

   </summary>

Well, you asked for it!

.. whole-code-block:: cpp

   void setup() {
      Serial.begin(9600);

      pinMode(13, OUTPUT);
   }

   void loop() {
      digitalWrite(13, HIGH);

      // Print a message to the Serial Monitor. to let the user
      // know the LED is on.
      Serial.println("LED is on!");

      delay(1000);

      digitalWrite(13, LOW);

      // Print a message to the Serial Monitor. to let the user
      // know the LED is off.
      Serial.println("LED is off!");

      delay(1000);
   }

..

   Note that the comments from the original code have been removed to
   make the code easier to read. You can keep the comments in your code
   to help you understand what each part does, if you wish.

.. raw:: html

   </details>