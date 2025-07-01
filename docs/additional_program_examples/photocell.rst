.. _photocell:

Using a Photocell Example
=========================

This example shows how to use a photocell (light sensor) with an Arduino. Photocells change their resistance based on the amount of light, which we can read as changing voltage values.

**How Photocells Work:**

- **Bright light** = Low resistance = Lower voltage reading
- **Dark** = High resistance = Higher voltage reading
- Use with a **10kΩ resistor** to create a voltage divider circuit

**Basic Troubleshooting:**

- **Same reading always**: Check wiring connections
- **Erratic readings**: Make sure connections are secure in breadboard
- **Not sensitive enough**: Try covering/uncovering sensor to test range

.. tip::
    Use `Serial.println(analogRead(A0));` to see the actual sensor values and adjust your code thresholds accordingly.

--------------

.. whole-literal-include:: ../../examples/photocell.ino
    :language: cpp