.. _advanced_topics:

Advanced Topics
===============

Macros and Preprocessor Directives
----------------------------------

Macros and preprocessor directives allow you to manage constants, create
reusable code snippets, and optimize your program's performance. The
#define directive is particularly useful in Arduino programming for
simplifying hardware interaction and creating readable, maintainable
code. Here, we expand the section with practical, real-world examples
that demonstrate its utility.

Example 1: Defining Pin Numbers for Clarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When working with multiple hardware components, hardcoding pin numbers
throughout your program can make it difficult to read and maintain. By
using ``#define``, you can assign meaningful names to these pins:

.. whole-code-block:: cpp

    #define LED_PIN 13
    #define BUTTON_PIN 7

    void setup() {
        pinMode(LED_PIN, OUTPUT);
        pinMode(BUTTON_PIN, INPUT);
    }

    void loop() {
        if (digitalRead(BUTTON_PIN) == HIGH) {
            digitalWrite(LED_PIN, HIGH);  // Turn on LED when button is pressed
        } else {
            digitalWrite(LED_PIN, LOW);   // Turn off LED otherwise
        }
    }

This approach makes your code more understandable and easier to update.
For instance, if the button pin changes, you only need to modify the
``#define`` directive.

Example 2: Configuring Hardware Constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In robotics or sensor-driven applications, you might have constants like
maximum speed, sensor thresholds, or calibration values. Instead of
hardcoding these values, you can use ``#define`` to centralize them:

.. code:: cpp

    #define MAX_SPEED 255
    #define MIN_SPEED 0
    #define TEMP_THRESHOLD 30  // Degrees Celsius

    void loop() {
        int currentTemperature = readTemperatureSensor();
        if (currentTemperature > TEMP_THRESHOLD) {
            setMotorSpeed(MIN_SPEED);  // Stop motor if it's too hot
        } else {
            setMotorSpeed(MAX_SPEED);  // Run motor at full speed otherwise
        }
    }

This makes your program adaptable and easier to maintain when hardware
or operating conditions change.

Example 3: Conditional Compilation for Debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``#define`` directive can also enable or disable sections of code
for debugging purposes:

.. whole-code-block:: cpp

    #define DEBUG_MODE  // Comment this line to disable debugging

    void setup() {
        Serial.begin(9600);
        #ifdef DEBUG_MODE
        Serial.println("Debugging is enabled.");
        #endif
    }

    void loop() {
        #ifdef DEBUG_MODE
        Serial.println("Running the loop.");
        delay(1000);
        #endif
    }

Here, the ``DEBUG_MODE`` macro activates debug messages when enabled.
This approach avoids cluttering your program with unnecessary output in
the final version while making debugging more manageable during
development.

--------------

By using ``#define`` and preprocessor directives effectively, you can
simplify your code, make it more readable, and adapt it to changing
requirements with minimal effort. These tools are particularly valuable
in hardware projects where constants and modularity are crucial for
success.
