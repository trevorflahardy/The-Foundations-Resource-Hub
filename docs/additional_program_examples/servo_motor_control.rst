.. _servo_motor_control:

Servo Motor Control Example
===========================

This example shows how to control a servo motor using Arduino. Servo motors can move to specific angles (0-180 degrees) using PWM signals.

**Servo vs DC Motor:**

- **DC Motor**: Spins continuously, hard to control exact position
- **Servo Motor**: Moves to specific angles, holds position automatically

**Basic Connections:**
- **Red wire**: Power (5V)
- **Brown/Black wire**: Ground  
- **Orange/Yellow wire**: Control signal (connect to Arduino pin 9)

**Simple Troubleshooting:**
- **Servo jitters**: Check power connections, may need external power supply
- **Doesn't move**: Verify control wire is connected to correct pin

.. seealso::

    For more information on the Servo motor, see the YouTube tutorial on
    `Controlling a Servo Motor with the Arduino <https://youtu.be/qatqVNh9uj4?si=49OuYT9s4RvW9hb0>`_
    , a guide developed specifically for USF students.

--------------

.. whole-literal-include:: ../../examples/servo_motor.ino
    :language: cpp