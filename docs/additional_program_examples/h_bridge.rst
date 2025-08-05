.. _h_bridge:

H-Bridge Control Example
========================

This example walks through how to control an H-Bridge using an Arduino board. Your project kit has an H-Bridge and two yellow DC motors. H-Bridges are used to control the speed and direction of a motor by controlling the direction of the current flow through the motor.

**Why Do We Need an H-Bridge?**

.. important::
    **The Problem**: Arduino pins can only provide about **20mA** of current, but your DC motors need much more power to spin effectively!

An H-Bridge solves this by:

1. **Controls motor direction**: Changes which way current flows through the motor
2. **Uses battery power**: Motors get 6V from batteries instead of Arduino's weaker 5V
3. **Protects Arduino**: Keeps high-current motor circuit separate from delicate Arduino pins

.. seealso::

    For more information on the H-Bridge and DC motors, see the YouTube tutorial on
    `Controlling DC Motors with the Arduino <https://youtu.be/j6D9-GKhAyc?si=qBnGTMy_sLqeOnyQ>`_
    guide developed specifically for USF students.

--------------


Common Troubleshooting
^^^^^^^^^^^^^^^^^^^^^^^

**Motor Not Spinning:**

1. **Check power**: Are batteries connected? Does Arduino LED light up?
2. **Wiggle wires**: Loose connections are the most common problem
3. **Check Common Ground**: Ensure the H-Bridge ground is connected to the Arduino ground **and** the battery ground. Most likely this means having two ground wires inserted in the middle screw terminal of the H-Bridge.
4. **Check motor connections**: Both motor wires must connect to the same side of H-Bridge

**Motor Spinning Wrong Direction:**

This is normal! Simply swap the two motor wires on the H-Bridge terminals.

.. tip::
    **Use your multimeter** to check battery voltage (should read ~6V) and verify connections when troubleshooting.


.. whole-literal-include:: ../../examples/h_bridge.ino
    :language: cpp