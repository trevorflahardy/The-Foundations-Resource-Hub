/**
 * How to Read from a Photocell using an Arduino
 * ---------------------------------------------
 * Foundations of Engineering Lab
 * The University of South Florida
 * Created by Trevor Flahardy on 1/18/2025
 * ---------------------------------------------
 * A photocell is a type of resistor that changes its resistance
 * based on the amount of light it is exposed to. In this example,
 * we will learn how to read from a photocell using an Arduino board.
 *
 * The photocell in your project kit is an analog sensor, which means
 * it will return a value between 0 and 1023. The photocell will return
 * a higher value when it is in the light, and a lower value when it is
 * in the dark.
 */

const int LED_PIN = 13;        // Connect the positive leg of an LED to this pin
const int PHOTO_CELL_PIN = A0; // Connect the positive leg of a photocell to the A0 pin

// When reading from the photocell, a higher value
// means the photocell is in the light, and a lower
// value means the photocell is in the dark. The
// 'DARK_THRESHOLD' determines the minimum value at which
// the LED will turn on.
const int DARK_THRESHOLD = 100;

void setup()
{
    Serial.begin(9600); // Start the Serial Monitor at 9600 baud

    // We are reading from the photocell, so we need to set the pin
    // mode to INPUT.
    pinMode(PHOTO_CELL_PIN, INPUT);

    // We are sending 5V to the LED when the photocell is in the dark,
    // so we need to set the pin mode to OUTPUT.
    pinMode(LED_PIN, OUTPUT);
}

void loop()
{
    // Read from the photocell pin.
    // Because the photocell is a variable resistor, the value
    // read from the photocell will be between 0 and 1023.
    int photocell_value = analogRead(PHOTO_CELL_PIN);

    if (photocell_value <= DARK_THRESHOLD)
    {
        // If the photocell value is less than or equal to the
        // DARK_THRESHOLD, turn on the LED because it must be
        // dark.
        digitalWrite(LED_PIN, HIGH);
        Serial.print("It's DARK, turn on the LED: ");
        Serial.println(photocell_value);
    }
    else
    {
        // If the photocell value is greater than the DARK_THRESHOLD,
        // turn off the LED because it must be light.
        digitalWrite(LED_PIN, LOW);
        Serial.print("It's LIGHT, turn off the LED: ");
        Serial.println(photocell_value);
    }
}