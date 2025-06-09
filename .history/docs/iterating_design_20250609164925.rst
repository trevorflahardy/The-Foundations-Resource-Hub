Iterating Your Design
=====================

.. contents::
   :local:
   :depth: 1

Learning from Print Failures
----------------------------

Even experienced makers encounter warping, layer shifts, or stringing. Rather than discarding a failed print, treat it as data:

Common Print Failures and How to Respond
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Warping**  
    *Symptom:*  
        Corners lifting off the bed, inconsistent layer height.  
    *Possible causes:*  
        Poor first-layer adhesion, bed temperature too low  
    *What to try:*  
        Increase bed temperature by 5 °C, add a brim, or re-level the bed.

- **Layer Shifts**  
    *Symptom:*  
        Layers misaligned horizontally during the print  
    *Possible causes:*  
        Loose belts, stepper motor skips, or obstructions  
    *What to try:*  
        Tighten X/Y belts and inspect for any obstructions along the axes.

- **Stringing**  
    *Symptom:*  
        Fine threads or hairs between printed features  
    *Possible causes:*  
        Retraction settings too low  
    *What to try:*  
        Increase retraction distance by 1 mm and retraction speed by 5 mm/s.

.. note::
   Keep a simple log (in your notebook or Git) of each failed print: date, settings changed, and result. Over time you’ll build a personal troubleshooting database.

Design-Test-Repeat Mindset
---------------------------

A single successful print is just one iteration in the cycle:

#. **Design**  
   Sketch or model the part in CAD. Save each version as `part_v01.scad`, `part_v02.scad`, etc.

#. **Slice & Print**  
   Export G-code with your current settings. Record nozzle/bed temperatures and speed.

#. **Evaluate**  
   Measure critical dimensions with calipers. Compare against your CAD model. Note any deviations.

#. **Adjust**  
   Tweak the design or slicer settings:
   - Adjust wall thickness for strength  
   - Modify bridging angles to reduce sag  
   - Tweak infill percentage for rigidity vs. weight

#. **Repeat**  
   Re-slice, re-print, and re-evaluate. Each loop should get you closer to a perfect part.

.. tip::
   Use version control (Git) for both your CAD files and slicer profiles. Tag commits like `v02-strengthened-walls` so you can roll back or branch off experiments seamlessly.

Next Steps
----------

Once your iteration process is dialed in, tackle these in your next session:

- Experiment with different filament types (ABS, PETG).  
- Calibrate your printer’s E-steps for more accurate extrusion.  
- Try advanced slicer features: variable layer height, custom supports.

With a robust design–test–repeat workflow, you’ll transform every “failed” print into progress—and graduate from novice to confident maker.

