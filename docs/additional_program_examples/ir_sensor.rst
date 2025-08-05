.. _ir_sensor:

IR Sensor Example
=================

This example shows how to use an IR sensor with Arduino. IR sensors detect objects by bouncing infrared light off them and give simple HIGH/LOW signals.

**How IR Sensors Work:**

- **Object detected** = HIGH (5V)
- **No object** = LOW (0V)
- Most sensors have adjustable sensitivity (small potentiometer on sensor)

**Basic Troubleshooting:**

- **Always reads HIGH or LOW**: Check power connections, adjust sensitivity dial
- **Erratic readings**: Use `pinMode(pin, INPUT_PULLUP);` to reduce noise
- **Wrong detection range**: Adjust the sensitivity potentiometer on the sensor

**Common Uses:**
- Obstacle avoidance (stop when object detected)
- Counting objects
- Line following (detect line edges)

.. tip::
    Use `Serial.println(digitalRead(irPin) ? "DETECTED" : "CLEAR");` to debug sensor readings.

.. whole-literal-include:: ../../examples/ir_sensor.ino
    :language: cpp