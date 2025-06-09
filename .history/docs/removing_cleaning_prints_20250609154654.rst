Removing & Cleaning Your Prints
================================

.. contents::
   :local:
   :depth: 2

Getting Your Print Off the Bed
------------------------------

1. **Let the bed cool completely.**  
   The build plate is still very hot when the printer finishes. Removing a print too soon risks deforming the bottom layers or burning your fingers. Wait until the plate reaches room temperature before attempting removal.

2. **Use light, even pressure.**  
   Attempt to pop prints off the plate without tools. If this doesn't work, slide a plastic putty knife beneath the edge of the print and gently rock it back and forth, but never pry from one corner only.

3. **Flex removable build plates.**  
   If your printer uses a flexible steel or PEI sheet, unclip it, bend it slightly until the print pops free, then immediately reclip. Keep hold of the plate so the part doesn’t flop off unexpectedly.

.. warning::
   Never discard or lay a heated build plate down—doing so can warp the plate or damage whatever surface it rests on. Always return it to the printer before setting it down.

.. figure:: images/flex-pop-sequence.jpg
   :alt: Flexing and popping the print off the bed
   :figwidth: 80%

Removing Supports
-----------------

1. **Trim bulk supports first.**  
   Use flush-cutters to snip away the thickest support “trees,” working from the top down.

2. **Peel finer struts by hand.**  
   Grip smaller supports between thumb and forefinger, twisting gently to detach them along their natural layer lines.

3. **Clean up nubs with a hobby knife.**  
   Lightly score any remaining stubs flush with the surface—slice away from yourself in multiple shallow passes.

.. tip::
   If supports cling too stubbornly, soak the part briefly in warm (not hot) water; this can soften the interface without harming PLA.

.. image:: images/remove-supports.gif
   :alt: Removing supports animation
   :class: gif

Sanding Basics
--------------

1. **Progress through grits in order.**  
   - **120–150** grit to knock down larger artifacts.  
   - **220–320** grit to smooth layer lines.  
   - **400–600** grit for a near-polished finish.

2. **Wet-sand above 400 grit.**  
   Use a drop of water on the paper to trap dust and prevent clogging—wet-sanding also keeps the plastic cool, reducing heat-induced smearing.

3. **Sand with the grain.**  
   Stroke in a single, consistent direction. Cross-hatching can leave swirl marks that are harder to eliminate later.

.. note::
   Wear a dust mask and goggles. PLA and ABS particles can irritate lungs and eyes even in small quantities.

.. list-table::
   :header-rows: 1
   :widths: 33 33 34

   * - **120 grit**
     - **220 grit**
     - **400 grit**
   * - .. image:: images/sand-120.jpg
         :alt: 120 grit sanding
     - .. image:: images/sand-220.jpg
         :alt: 220 grit sanding
     - .. image:: images/sand-400.jpg
         :alt: 400 grit sanding

Final Cleanup & Inspection
--------------------------

- **Brush or blow away dust.**  
  A soft paintbrush or canned air will clear sanding residue without scratching.

- **Wipe with isopropyl alcohol.**  
  A lint-free cloth dampened with 70 % IPA removes fingerprints and grease, readying the part for painting or assembly.

- **Inspect for flaws.**  
  Hold the part up to the light—small cracks or missed supports often reveal themselves in high-contrast backlighting.

.. tip::
   A quick G-code snippet can preheat or cool your bed automatically before removal:

   .. code-block:: gcode

      ; Cool bed to 30 °C before beep
      M190 R30
      M300 S440 P200

.. raw:: html

   <model-viewer src="models/part_inspection.stl"
                 alt="Interactive backlighting demo"
                 camera-controls
                 auto-rotate></model-viewer>

Your print is now ready for any further finishing—painting, assembly, or simply enjoying the fruits of your care and patience!
