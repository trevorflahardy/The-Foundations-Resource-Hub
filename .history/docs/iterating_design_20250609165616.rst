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

Layer Shifts
~~~~~~~~~~~~

**Symptom:**  
Layers misaligned horizontally during print

**Possible causes:**  
Print speed or motion settings too aggressive

**What to try:**  
- Reduce print speed by 10–20 mm/s in your slicer. :contentReference[oaicite:4]{index=4}  
- Lower acceleration and jerk values for smoother direction changes. :contentReference[oaicite:5]{index=5}  

Stringing
~~~~~~~~~

**Symptom:**  
Fine threads or hairs between printed features

**Possible causes:**  
Insufficient retraction; nozzle temperature too high

**What to try:**  
- Increase retraction distance by ~1 mm and retraction speed by 5 mm/s. :contentReference[oaicite:6]{index=6}  
- Raise travel (non-printing move) speed to minimize oozing. :contentReference[oaicite:7]{index=7}  
- Lower nozzle temperature by 5–10 °C. :contentReference[oaicite:8]{index=8}  
- Enable coasting or wipe-while-retracting in your slicer. :contentReference[oaicite:9]{index=9}  

.. note::  
   Keep a simple log (notebook or Git) of each failed print: date, slicer changes, and outcome. Over time you’ll build a personal troubleshooting database. :contentReference[oaicite:10]{index=10}  

Design-Test-Repeat Mindset
---------------------------

Iteration is the heart of 3D-printing success. Each cycle refines your part’s fit, finish, or function:

#. **Design**  
   Model your part in CAD. Save each version as `part_v01.scad`, `part_v02.scad`, etc., so you can track changes. :contentReference[oaicite:11]{index=11}  
#. **Slice & Print**  
   Export G-code with documented settings (nozzle temp, bed temp, speeds). Print under supervised lab conditions.  
#. **Evaluate**  
   Measure critical dimensions with calipers; inspect surface quality and structural integrity.  
#. **Adjust**  
   Tweak your CAD or slicer profile: wall thickness, bridging angles, infill percentage, etc.  
#. **Repeat**  
   Re-slice, re-print, and re-evaluate. Each loop should converge toward a reliable, high-quality part. :contentReference[oaicite:12]{index=12}  

.. tip::  
   Use version control (Git) for both CAD files and slicer profiles. Tag commits like `v02-stronger-walls` for easy rollback and branching. :contentReference[oaicite:13]{index=13}  

Next Steps
----------

Once you’ve honed your core workflow, explore:

- Printing with different materials (e.g., PETG, ABS).  
- Advanced slicing features: variable layer heights, custom support patterns.  
- Simulation tools for stress analysis before printing.  

With a disciplined design-test-repeat routine, every “failure” becomes a step toward mastering 3D printing.
::contentReference[oaicite:14]{index=14}
