/**
 * How to use an HC-SR04 Ultrasonic Sensor with an Arduino
 * -------------------------------------------------------
 * Foundations of Engineering Lab
 * The University of South Florida
 * Created by Trevor Flahardy on 1/18/2025
 * -------------------------------------------------------
 *
 * The HC-SR04 Ultrasonic Sensor is a device that can measure
 * distance using ultrasonic sound waves. It is commonly used
 * in robotics and automation projects. In this example, we
 * will learn how to use the HC-SR04 Ultrasonic Sensor with an
 * Arduino board.
 *
 * The HC-SR04 Ultrasonic Sensor has four pins:
 * - VCC: Connect this pin to the 5V pin on the Arduino
 * - GND: Connect this pin to the GND pin on the Arduino
 * - TRIG: Connect this pin to digital pin 12 on the Arduino
 * - ECHO: Connect this pin to digital pin 11 on the Arduino
 *
 * The HC-SR04 Ultrasonic Sensor works by sending out an
 * ultrasonic pulse from the TRIG pin. The pulse bounces off
 * an object and returns to the sensor through the ECHO pin.
 * By measuring the time it takes for the pulse to return, we
 * can calculate the distance to the object.
 */

const int TRIG_PIN = 12; // Connect the TRIG pin to pin 12
const int ECHO_PIN = 11; // Connect the ECHO pin to pin 11

void setup()
{
    Serial.begin(9600); // Start the Serial Monitor at 9600 baud

    // In the setup function, we need to tell the Arduino
    // which pins are used for input and output. We do this
    // using the 'pinMode()' function. The TRIG_PIN is
    // used to send the ultrasonic pulse, so it is an output.
    // The ECHO_PIN is used to receive the ultrasonic pulse,
    // so it is an input.
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
}

void loop()
{
    // Clear the TRIG_PIN before sending any pulses.
    digitalWrite(TRIG_PIN, LOW);
    delay(2);

    // Send a 10 microsecond pulse to the TRIG_PIN. This
    // will trigger the ultrasonic sensor to send out an
    // ultrasonic pulse.
    digitalWrite(TRIG_PIN, HIGH);
    delay(10);
    digitalWrite(TRIG_PIN, LOW);

    // Using the ECHO_PIN, we can measure the time it takes
    // for the ultrasonic pulse to return to the sensor.
    // We can do this using the 'pulseIn()' function. This
    // function returns the duration of the pulse in microseconds.
    const float duration_us = pulseIn(ECHO_PIN, HIGH);

    // Take the duration of the pulse and convert it to
    // distance in centimeters. The speed of sound is 34300
    // cm/s, so we can use the formula:
    // distance = (duration * speed of sound) / 2
    const float distance_cm = (duration_us * 0.034) / 2;

    // Print the distance to the Serial Monitor.
    Serial.print("Distance: ");
    Serial.print(distance_cm);
}