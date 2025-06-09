Iterating Your Design
=====================

.. contents::
   :local:
   :depth: 1

Learning from Project Failures
-------------------------------

Even experienced Arduino developers encounter common issues like faulty connections, logic errors, or sensor malfunctions. Rather than discarding a failed project, use it as feedback to improve your next iteration.

Common Arduino Issues and How to Respond
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload Failures
~~~~~~~~~~~~~~~

**Symptom:**  
Code won't upload to Arduino

**Possible causes:**  
Wrong board selected; incorrect COM port; faulty USB cable

**What to try:**  
- Verify the correct board is selected in Tools > Board
- Check the COM port in Tools > Port  
- Try a different USB cable or port
- Press the reset button on Arduino before uploading

Sensor Reading Issues
~~~~~~~~~~~~~~~~~~~~

**Symptom:**  
Inconsistent or incorrect sensor readings

**Possible causes:**  
Loose connections; interference; incorrect wiring

**What to try:**  
- Check all connections are secure
- Add pull-up resistors where needed
- Use shielded cables for long sensor runs
- Add delay() between readings to allow sensor to stabilize

Code Logic Errors
~~~~~~~~~~~~~~~~~

**Symptom:**  
Arduino runs but doesn't behave as expected

**Possible causes:**  
Logic errors; incorrect variable types; timing issues

**What to try:**  
- Use Serial.print() to debug variable values
- Check if/else conditions are correctly structured
- Verify loop timing with millis() instead of delay()
- Review variable scope and initialization

.. note::  
   Keep a simple log (notebook or Git) of each failed project: date, changes made, and outcome. Over time you'll build a personal troubleshooting database.

Design-Test-Repeat Mindset
---------------------------

Iteration is the heart of Arduino development success. Each cycle refines your project's functionality, reliability, or performance:

#. **Design**  
   Plan your circuit and code structure. Save each version as ``project_v01.ino``, ``project_v02.ino``, etc., so you can track changes.
#. **Build & Upload**  
   Assemble your circuit and upload code with documented settings. Test under controlled conditions.
#. **Evaluate**  
   Test all functions systematically; check sensor accuracy and timing with the Serial Monitor.
#. **Adjust**  
   Modify your code or circuit: adjust delays, change pin assignments, add error handling, etc.
#. **Repeat**  
   Re-upload, re-test, and re-evaluate. Each loop should converge toward a reliable, robust project.

.. tip::  
   Use version control (Git) for both code files and circuit diagrams. Tag commits like ``v02-improved-timing`` for easy rollback and feature branching.

Next Steps
----------

Once you've refined your core development workflow, explore:

- Working with different sensor types (analog vs. digital).
- Advanced Arduino features: interrupts, timers, sleep modes.
- Integration with other platforms like Raspberry Pi or cloud services.

With a disciplined design-test-repeat routine, every "failure" becomes a step toward mastering Arduino development.
