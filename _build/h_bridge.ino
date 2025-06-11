/**
 * How to control two DC motors with an H-Bridge
 * ---------------------------------------------
 * Foundations of Engineering Lab
 * The University of South Florida
 * Created by Trevor Flahardy on 1/19/2025
 * ---------------------------------------------
 *
 * The L298N H-Bridge is a device that allows you to control
 * the direction and speed of a DC motor (or motors). It is commonly used
 * in robotics and automation projects. In this example, we will learn
 * how to control two DC motors using an L298N H-Bridge and an Arduino board.
 *
 * The L298N H-Bridge has two pins for each motor:
 * - IN1: Connect this pin to digital pin 2 on the Arduino.
 * - IN2: Connect this pin to digital pin 3 on the Arduino.
 * - IN3: Connect this pin to digital pin 4 on the Arduino.
 * - IN4: Connect this pin to digital pin 5 on the Arduino.
 *
 * It also has two pins for each motor to control the speed. These pins are
 * controlled using PWM (Pulse Width Modulation) signals, so the pins
 * they are connected to should be PWM pins on the Arduino. These are denoted
 * using a '~' symbol next to the pin number on the Arduino board. In this example,
 * we will use the following pins:
 * - ENA: Connect this pin to pin 9 on the Arduino
 * - ENB: Connect this pin to pin 10 on the Arduino
 *
 * The L298N H-Bridge works by sending signals to the IN1 and IN2 pins
 * to control the direction of the motor. Sending the following signals
 * to the IN1 and IN2 pins, or the IN3 and IN4 pins respectively, will result
 * in the motors spinning in the following directions:
 *
 * - Spin Motor 1 Forward: IN1 = HIGH, IN2 = LOW
 * - Spin Motor 1 Backward: IN1 = LOW, IN2 = HIGH
 * - Stop Motor 1: IN1 = LOW, IN2 = LOW
 *
 * Or, for the second motor:
 *
 * - Spin Motor 2 Forward: IN3 = HIGH, IN4 = LOW
 * - Spin Motor 2 Backward: IN3 = LOW, IN4 = HIGH
 * - Stop Motor 2: IN3 = LOW, IN4 = LOW
 *
 * When controlling speed, you can use the 'analogWrite()' function to
 * send a PWM signal to the ENA and ENB pins. The higher the value you
 * pass to 'analogWrite()', the faster the motor will spin. The range
 * of values you can pass to 'analogWrite()' is between 0 and 255, with
 * 0 being the slowest speed and 255 being the fastest speed.
 *
 * This example assumes you have two DC motors connected to the L298N
 * H-Bridge. If you only have one motor, you can simply remove the
 * sections that control the second motor.
 */

// Control for one motor, has two pins for control and one for speed:
const int H_BRIDGE_IN1 = 2;
const int H_BRIDGE_IN2 = 3;
const int H_BRIDGE_ENA = 9; // Speed control pin

// Control for the other motor, has two pins for control and one for speed:
const int H_BRIDGE_IN3 = 4;
const int H_BRIDGE_IN4 = 5;
const int H_BRIDGE_ENB = 10; // Speed control pin

void setup()
{
    Serial.begin(9600); // Start the Serial Monitor at 9600 baud

    // In the setup function, we need to tell the Arduino
    // which pins are used for input and output. We do this
    // using the 'pinMode()' function. The 'H_BRIDGE_IN1' and
    // 'H_BRIDGE_IN2' pins are used to control the motor, so
    // they are 'OUTPUT's. The same goes for 'H_BRIDGE_IN3' and
    // 'H_BRIDGE_IN4'.
    pinMode(H_BRIDGE_IN1, OUTPUT);
    pinMode(H_BRIDGE_IN2, OUTPUT);
    pinMode(H_BRIDGE_IN3, OUTPUT);
    pinMode(H_BRIDGE_IN4, OUTPUT);

    // The 'H_BRIDGE_ENA' and 'H_BRIDGE_ENB' pins are used to
    // control the speed of the motor, so they are 'OUTPUT's as well.
    pinMode(H_BRIDGE_ENA, OUTPUT);
    pinMode(H_BRIDGE_ENB, OUTPUT);
}

/**
 * This function will set a motor to move forward.
 *
 * If you test this function with a motor and it is spinning
 * backward, you can either:
 * 1. Swap the 'H_BRIDGE_IN1' and 'H_BRIDGE_IN2' pins in the
 *   'forward()' function, or
 * 2. Swap the connections to the motor.
 *
 * ^ All this means is that the polarity of the motor is reversed
 * and you need to adjust the connections accordingly.
 */
void forward(int in1, int in2)
{
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
}

/**
 * This function will set a motor to move backward.
 *
 * Similarly to the 'forward()' function, if your motors
 * are spinning forward the wrong direction - simply follow
 * one of the options listed in the comment of the 'forward()'
 * function.
 */
void backward(int in1, int in2)
{
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
}

void stop(int in1, int in2)
{
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
}

void setSpeed(int speed, int en)
{
    analogWrite(en, speed);
}

/**
 * In this `loop()` function, the motors are engaged to follow
 * the same repeating pattern (with a 2s delay in between):
 *
 * 1. Move the first motor forward at full speed while the second motor is stopped
 * 2. Stop the first motor and move the second motor forward at full speed
 * 3. Stop all the motors
 * 4. Make both the motors spin half speed in the opposite direction (backward)
 * 5. Stop all the motors
 *
 * We defined functions for moving the motors forward, backward,
 * and stopping them to ease the readability of the code and
 * make it easier to maintain. The functions are defined above
 * the `loop()` function.
 */
void loop()
{
    // 1. Move the first motor forward at full speed while the second motor is stopped
    setSpeed(255, H_BRIDGE_ENA);
    forward(H_BRIDGE_IN1, H_BRIDGE_IN2);

    delay(2000); // Wait for 2 seconds

    // 2. Stop the first motor and move the second motor forward at full speed
    stop(H_BRIDGE_IN1, H_BRIDGE_IN2);
    setSpeed(255, H_BRIDGE_ENB);
    forward(H_BRIDGE_IN3, H_BRIDGE_IN4);

    delay(2000); // Wait for 2 seconds

    // 3. Stop all the motors.
    stop(H_BRIDGE_IN1, H_BRIDGE_IN2);
    delay(2000); // Wait for 2 seconds

    // 4. Make both the motors spin opposite direction (backward) at half speed
    setSpeed(127, H_BRIDGE_ENA);
    setSpeed(127, H_BRIDGE_ENB);
    backward(H_BRIDGE_IN1, H_BRIDGE_IN2);
    backward(H_BRIDGE_IN3, H_BRIDGE_IN4);

    delay(2000); // Wait for 2 seconds

    // 5. Stop all the motors.
    stop(H_BRIDGE_IN1, H_BRIDGE_IN2);
    stop(H_BRIDGE_IN3, H_BRIDGE_IN4);

    delay(2000); // Wait for 2 seconds
}