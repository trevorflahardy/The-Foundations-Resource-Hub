.. _advanced_topics:

Advanced Topics
===============

The topics in this section **are completely optional** and are intended
for those who want to deepen their understanding of Arduino programming
and explore more advanced concepts. **You do not need to master these
topics to create a successful Arduino program in this course.**

.. warning::

    These advanced topics require a deeper understanding of
    programming concepts and may be challenging for beginners. Moreover,
    the examples assume you understand all the material covered thus far
    in the course. If you are new to programming, it is recommended to
    focus on the core concepts first before diving into these advanced
    topics, if you wish.

.. _classes-and-objects:

Classes and Objects
-------------------

In the :ref:`Data Types <data_types>` section you were introduced to the concept
of data types, like ``String``, ``int``, and ``float``, which are used to
store and manipulate data in your program. In this section, we will
explore the basic concept of classes, which are used to create custom
data types in The Arduino Programming Language.

.. important::

    Notice in the :ref:`Servo Motor Control Example <servo_motor_control>` section
    the ``Servo`` type was used to control the servo motor. This type is given
    by the Arduino library and is an example of a class.

    Due to the advanced nature in explaining classes and objects, this idea was
    never introduced and rather brushed over as a type like any other builtin type.

Classes are a fundamental concept in object-oriented programming (OOP),
which is a programming paradigm that organizes code into objects that
interact with each other. A class is a blueprint for creating objects
that share common attributes and behaviors.

For example, let's say we wanted to represent a car in a program. We would store information like
make, model, and year of the car. We would also have behaviors like starting the engine and driving.

.. code-block:: cpp

    String make = "Mercedes";
    String model = "C-Class";
    int year = 2020;

    void startEngine() {
        Serial.println("Engine started.");
    }

    void drive() {
        Serial.println("Driving...");
    }

This code snippet represents a car using variables and functions. However, what if we wanted
to represent multiple cars in our program? We would have to create multiple variables and functions
for each car, which would be cumbersome and error-prone.

Classes provide a way to encapsulate data and behavior into a single unit called an **object**.
An object is an **instance** of a class, or the result of creating a class. Each object has its own
attributes (data) and methods (functions) that can be accessed and modified independently.

So if we were to create a class called ``Car`` to represent a car in our program:

.. code-block:: cpp

    class Car {
    public:
        String make;
        String model;
        int year;

        void startEngine() {
            Serial.println("Engine started.");
        }

        void drive() {
            Serial.println("Driving...");
        }
    };


Then, instead of creating individual variables and functions for each car, we can create objects
of the ``Car`` class:

.. code-block:: cpp

    Car my_car;
    my_car.make = "Mercedes";
    my_car.model = "C-Class";
    my_car.year = 2020;

    my_car.startEngine();
    >>> Engine started.

    my_car.drive();
    >>> Driving...

Class Definition Syntax
~~~~~~~~~~~~~~~~~~~~~~~

The syntax for defining a class in The Arduino Programming Language is as follows:

.. code-block:: cpp

    class <ClassName> {
    public:
        // Attributes (data members)
        DataType attributeName1;
        DataType attributeName2;
        ...

        ClassName([<parameter type> <parameter name>, ...]) {
            // Constructor implementation
        }

        // Methods (member functions)
        <return type> methodName1([<parameter type> <parameter name>], ...) {
            // Method implementation
        }

        // ... classes can have infinite methods
    };

- The ``class`` keyword is used to define a class.
- The class name (``ClassName``) should be capitalized by convention.
- The ``public:`` keyword specifies the access level of the attributes and methods. In this case, they are accessible from outside the class.

  .. note::

    There are other access specifiers like ``private`` and ``protected`` that control the visibility of class members. We
    will not cover them in this section.

- Attributes are variables that store data for each object of the class.
- The constructor is a special method that is called when an object is created. It is used to initialize the object's attributes (see :ref:`Constructors` below.)
- Methods are functions that define the behavior of the class.

.. _constructors:

Constructors
^^^^^^^^^^^^

A constructor is a special method that is called when an object is created. It is used to initialize the object's attributes. The syntax for defining a constructor is as follows:

.. code-block:: cpp

    ClassName([<parameter type> <parameter name>, ...]) {
        // Constructor implementation
    }

- The constructor **must** have the same name as the class.
- It can take parameters to initialize the object's attributes.
- If no constructor is defined, the compiler will provide a default constructor that initializes the attributes to their default values.

.. important::

    The constructor parameters cannot have the same name as the class attributes without
    using the ``this`` keyword. This is a common mistake that beginners make when defining constructors.
    If you do not understand the ``this`` keyword, it is recommended to avoid using the
    same name for the constructor parameters and the class attributes, as the following example demonstrates:

    .. code-block:: cpp
        :caption: A common mistake when defining a constructor.

        class Foo {
        public:
            int bar;

            Foo(int bar) {
                // This will not work as expected
                bar = bar;  // This will not work!
            }
        }

    The idea of ``this`` is out of the scope of this course. You must do independent research if you wish
    to use it.

    **Recommendation**: Avoid using the same name for the constructor parameters and the class attributes to prevent confusion.

    .. code-block:: cpp
        :caption: Author recommendation for new coding students to avoid confusion.

        class Foo {
        public:
            int bar;

            Foo(int new_bar) {
                bar = new_bar;  // This will work!
            }
        }


You do not need to define a constructor for every class; like in the car example above we simply used the default constructor
and then set the attributes of the object manually.

So, let's say we wanted to redefine the ``Car`` class with a constructor that initializes the attributes:

.. code-block:: cpp
    :caption: Defining a constructor for the ``Car`` class that initializes its attributes.
    :emphasize-lines: 7, 8, 9, 10, 11

    class Car {
    public:
        String make;
        String model;
        int year;

        Car(String car_make, String car_model, int car_year) {
            make = car_make;
            model = car_model;
            year = car_year;
        }

        void startEngine() {
            Serial.println("Engine started.");
        }

        void drive() {
            Serial.println("Driving...");
        }
    };

In this example, the constructor takes three parameters (``car_make``, ``car_model``, and ``car_year``) and initializes the object's attributes with these values.

Creating Objects
~~~~~~~~~~~~~~~~

To create an instance of a class, aka. a new **object** you use the following syntax:

.. code-block:: cpp

    ClassName objectName([<parameter value>, ...]);

where,

- ``ClassName`` is the name of the class.
- ``objectName`` is the name of the object.
- ``parameter value`` is the value passed to the constructor (if any).

For example, to create a ``Car`` object using the new constructor:

.. code-block:: cpp

    Car my_car("Mercedes", "C-Class", 2020); // Constructor with parameters

Accessing Attributes and Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can access the attributes and methods of an object using the dot operator (``.``):

.. code-block:: cpp
    :caption: Changing the make and model of the car object and then call the ``drive()`` method.

    my_car.make = "Toyota";
    my_car.model = "Corolla";
    my_car.drive();


Real World Example of a Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, let's say you want to create a class
for the ``HC-SR04`` ultrasonic sensor like the ``Servo`` library does for servo motors. You could define a class like this:

.. code-block:: cpp

    class UltrasonicSensor {
    private:
        int trig_pin;
        int echo_pin;

    public:
        UltrasonicSensor(int trig, int echo) {
            trig_pin = trig;
            echo_pin = echo;
        }

        /**
            The 'getDistance()' method reads the distance from the ultrasonic sensor
            and returns it in centimeters.
        */
        float getDistance() {
            // Clear the trigger pin.
            digitalWrite(trig_pin, LOW);
            delayMicroseconds(2);

            // Send a 10 microsecond pulse to the trigger pin.
            digitalWrite(trig_pin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig_pin, LOW);

            // Read the pulse duration from the echo pin and calculate the distance,
            // return it in centimeters.
            return (pulseIn(echo_pin, HIGH) * 0.034) / 2;

        }
    };

Then you can use your new ``UltrasonicSensor`` class and call the ``getDistance()`` method to get the distance from the sensor:

.. code-block:: cpp

    UltrasonicSensor SENSOR(2, 3);  // Sensor connected to pins 2 and 3

    void setup() {
        pinMode(SENSOR.trig_pin, OUTPUT);
        pinMode(SENSOR.echo_pin, INPUT);
    }

    void loop() {
        float distance = SENSOR.getDistance();
        Serial.print("Distance: ");
        Serial.print(distance);
        Serial.println(" cm");
        delay(1000);
    }

Taking this idea even further, we can use this new type to create an array of sensors and read
the distance from many sensors at once:

.. code-block:: cpp

    const int SENSOR_COUNT = 2;
    UltrasonicSensor SENSORS[SENSOR_COUNT] = {
        UltrasonicSensor(2, 3),  // Sensor 1 connected to pins 2 and 3
        UltrasonicSensor(4, 5)   // Sensor 2 connected to pins 4 and 5
    };

    void setup() {
        for (int i = 0; i < SENSOR_COUNT; i++) {
            pinMode(SENSORS[i].trig_pin, OUTPUT);
            pinMode(SENSORS[i].echo_pin, INPUT);
        }
    }

    void loop() {
        for (int i = 0; i < SENSOR_COUNT; i++) {
            float distance = SENSORS[i].getDistance();
            Serial.print("Sensor ");
            Serial.print(i + 1);
            Serial.print(" Distance: ");
            Serial.print(distance);
            Serial.println(" cm");
        }
        delay(1000);
    }

.. _macros-and-preprocessor-directives:

Macros and Preprocessor Directives
----------------------------------

Macros and preprocessor directives allow you to manage constants, create
reusable code snippets, and optimize your program's performance. The
``#define`` directive is particularly useful in Arduino programming for
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

.. whole-code-block:: cpp

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
