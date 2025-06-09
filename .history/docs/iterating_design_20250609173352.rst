Iterating Your Design
=====================

.. contents::
   :local:
   :depth: 1

Learning from Print Failures
----------------------------

Engineering wouldn't be possible without iteration. You should expect to encounter failures, but it's important you learn from them! 
If something isn't working, don't just try again, but instead take a step back and analyze the problem. Start by checking for common issues, then adjust your design or slicing settings accordingly.

Common Print Failures and How to Respond
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Warping
~~~~~~~

**Symptom:**  
Corners lifting off the bed

**Possible causes:**  
Poor first-layer adhesion; bed temperature too low

**What to try:**  
 - Increase bed temperature by 5 °C in your slicer settings.
 - Add a one-layer brim to expand contact area.   
 - Increase first-layer height or width (e.g., 120 % extrusion width or 0.24 mm layer height). 
 - If you've tried everything else, apply a **thin** layer of glue stick to the build plate to increase adhesion.   

Layer Shifts
~~~~~~~~~~~~

**Symptom:**  
Layers misaligned horizontally during print

**Possible causes:**  
Print speed or motion settings too aggressive

**What to try:**  
 - Reduce print speed by 10–20 mm/s in your slicer.   
 - Ensure the wheels of the printer rack are locked so it can't move during printing.

Stringing
~~~~~~~~~

**Symptom:**  
Fine threads or hairs between printed features

**Possible causes:**  
Insufficient support; nozzle temperature too high

**What to try:**  
 - Check supports, especially overhangs (areas with no material beneath).   
 - Lower nozzle temperature by 5–10 °C.

.. note::  
   Keep a simple log of each failed print: iteration number, slicer changes, and outcome. Over time you’ll build a personal troubleshooting database. it  

Design-Test-Repeat Mindset
---------------------------

Iteration is the heart of 3D-printing success. Each cycle refines your part’s fit, finish, or function:

#. **Design**  
   Model your part in CAD. Save each version as `part_v01.scad`, `part_v02.scad`, etc., so you can track changes. it  
#. **Slice & Print**  
   Export G-code with documented settings (nozzle temp, bed temp, speeds). Print under supervised lab conditions.  
#. **Evaluate**  
   Measure critical dimensions with calipers; inspect surface quality and structural integrity.  
#. **Adjust**  
   Tweak your CAD or slicer profile: wall thickness, bridging angles, infill percentage, etc.  
#. **Repeat**  
   Re-slice, re-print, and re-evaluate. Each loop should converge toward a reliable, high-quality part. it  

.. tip::  
   Use version control (Git) for both CAD files and slicer profiles. Tag commits like `v02-stronger-walls` for easy rollback and branching. it  

Next Steps
----------

Once you’ve honed your core workflow, explore:

- Printing with different materials (e.g., PETG, ABS).  
- Advanced slicing features: variable layer heights, custom support patterns.  
- Simulation tools for stress analysis before printing.  

With a disciplined design-test-repeat routine, every “failure” becomes a step toward mastering 3D printing.
:it
