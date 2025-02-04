/**
 * ----------------------------------------------------------------
 * Arduino Origami Bot
 * Created by Daniel Jordan, USF Department of Engineering
 * Updated by Trevor Flahardy, USF Department of Medical Engineering
 * Built Using Arduino IDE 1.8.19, updated using Arduino IDE 2.3.4
 * Tested on Feb. 4 2024
 * ----------------------------------------------------------------
 */

// Define the pins for the H-Bridge. Each pin corresponds
// to that pin on the H-Bridge. So, for example, IN1 is a connection
// from the pin labeled IN1 on the H-Bridge to the Arduino pin 4.

const int IN1 = 4; // connect IN1 on the H-Bridge to Arduino pin 4
const int IN2 = 5; // connect IN2 on the H-Bridge to Arduino pin 5

const int IN3 = 9;  // connect IN3 on the H-Bridge to Arduino pin 9
const int IN4 = 10; // connect IN4 on the H-Bridge to Arduino pin 10

/**
 * The setup function of the program. Sets all the pins as outputs
 * (ie, the Arduino is sending information to the H-Bridge).
 */
void setup()
{
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
}

/**
 * The loop function of the program. This is the main part of the program
 * that will run over and over again. It moves the robot forward, turns it,
 * moves it backwards, and stops it.
 */
void loop()
{
    // Moves the robot straight for 1.5 seconds
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);

    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    delay(1500);

    // Turns the robot for 1.0 seconds
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    delay(1000);

    // Moves the robot backwards for 1.0 seconds
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);

    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    delay(1000);

    // Stops the robot for 1.0 seconds
    digitalWrite(IN2, LOW);

    digitalWrite(IN4, LOW);
    delay(1000);
}
