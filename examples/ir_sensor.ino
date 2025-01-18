/**
 * How to Read from an IR Sensor using an Arduino
 * ---------------------------------------------
 * Foundations of Engineering Lab
 * The University of South Florida
 * Created by Trevor Flahardy on 1/18/2025
 * ---------------------------------------------
 * An IR sensor is a type of sensor that detects objects by
 * emitting and receiving infrared light. In this example, we
 * will learn how to read from an IR sensor using an Arduino board.
 *
 * The IR sensor in your project kit is a digital sensor, which means
 * it will return a value of either HIGH or LOW. The IR sensor will
 * return a HIGH value when it is detecting an object, and a LOW value
 * when it is not detecting an object.
 *
 * The IR sensor is connected to pin 9, and the onboard LED is connected
 * to pin 13. When the IR sensor detects an object, the LED will turn OFF.
 * When the IR sensor does not detect an object, the LED will turn ON.
 */

const int IR_SENSOR_PIN = 9; // The IR sensor is connected to pin 9

void setup()
{
    Serial.begin(9600); // Start the Serial Monitor at 9600 baud

    // The IR sensor pin is being read from, so we need to
    // set it as an INPUT.
    pinMode(IR_SENSOR_PIN, INPUT);

    // The LED will be sent 5V when we detect an object
    // with the IR sensor, so we need to set it as an OUTPUT.
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
    // Read from the IR_SENSOR_PIN. When this value is HIGH,
    // it means that the IR sensor is detecting an object.
    int ir_sensor_value = digitalRead(IR_SENSOR_PIN);

    if (ir_sensor_value == HIGH)
    {
        // This IR sensor is detecting an object. Turn OFF the LED
        // because the object is too close.
        digitalWrite(LED_BUILTIN, LOW);

        // Print a message to the Serial Monitor.
        Serial.println("Object detected! LED OFF.");
    }
    else
    {
        // This IR sensor is not detecting an object. Turn ON the LED
        // because the object is too far away.
        digitalWrite(LED_BUILTIN, HIGH);

        // Print a message to the Serial Monitor.
        Serial.println("No object detected! LED ON.");
    }
}