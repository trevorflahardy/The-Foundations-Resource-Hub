.. _additional_program_examples:

Additional Program Examples
===========================

.. _servo_motor_control:

Servo Motor Control
-------------------

This example walks through how to control a Servo motor using an Arduino
board. Your project kit has a Servo. Servo motors are small devices that
have a shaft that can be positioned to specific angular positions.
Servos are used in many applications, including robotics,
remote control cars, and airplanes. In this example, we will learn how to
control a Servo using an Arduino board.

--------------

.. whole-code-block:: cpp

   /**
    * How to control a Servo using an Arduino
    * ---------------------------------------
    * Foundations of Engineering Lab
    * The University of South Florida
    * ---------------------------------------
    * A Servo is a small device that has a shaft that can be
    * positioned to specific angular positions. Servos are used
    * in many applications, including robotics, remote control
    * cars, and airplanes. In this example, we will learn how
    * to control a Servo using an Arduino board.
    *
    * The Servo in your project kit needs 5V to function
    * properly.
    *
    * The Arduino uses Pulse Width Modulation (PWM) to
    * communicate with Servos. The Servo we have in the Arduino
    * kit has about 160 degrees of motion (**assume 180 degrees
    * in your code**).
    *
    * To easily control a Servo, you will use the Servo library
    * that is included in the Arduino IDE by default.
    */

    #include <Servo.h> // Include the Servo library. This adds the Servo class to the code.

    const int SERVO_PIN = 12; // Define the pin that the Servo is connected to.

    /**
    * Instantiate a Servo object. The Arduino Uno can
    * handle up to 8 servos at a time.
    *
    * The syntax for this is as follows:
    * Servo <servo_variable_name>;
    *
    * Where "Servo" is a class given to us by the Servo library,
    * and "<servo_variable_name>" is the * name of the variable we
    * you to use to refer to the Servo object.
    */
    Servo my_servo;

    void setup()
    {
        Serial.begin(9600); // Start the Serial Monitor at 9600 baud

        // In the setup function, you must tell the Servo
        // instance ("my_servo" variable) which pin your
        // Servo is connected to. This is done using the
        // attach function.
        my_servo.attach(SERVO_PIN);
    }

    void loop()
    {
        // Using the builtin write function, we can set the angle
        // of the Servo. A 0 degree angle is the starting position
        // of the Servo. This is perpendicular to the shaft of the
        // Servo. A 90 degree angle is the middle position of the
        // Servo. A 180 degree angle is the maximum position of the Servo.

        // Let's tell the Servo to sweep from 0 to 180 degrees,
        // in 1 degree increments. You can use this in case
        // you need fine control of your servo's location.
        for (int angle = 0; angle <= 180; angle++)
        {
            my_servo.write(angle); // Set the angle of the Servo to "angle"

            // Print the angle to the Serial Monitor
            int current_angle = my_servo.read();
            Serial.print("Current angle: ");
            Serial.println(current_angle);

            // Then wait for 15 milliseconds. This is because the Servo
            // needs time to move to the new position. Writing a position
            // only tells the Servo where it should be, it is not an indicator of
            // where the Servo is currently. Thus, we need to wait for the Servo
            // to get to the angle we want.
            delay(15);
        }

        // The servo has now swept from 0 to 180 degrees. Now, set the
        // angle back to 0. You can use this if you don't need fine
        // control of your servo's location.
        my_servo.write(0);
        delay(1000); // Wait for 1 second before starting the loop again.

        Serial.println("Servo has completed a sweep.");
    }