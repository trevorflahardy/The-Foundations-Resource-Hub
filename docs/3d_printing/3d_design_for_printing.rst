.. _3d_design_for_printing:

***********************
3D Design for Printing
***********************

..
  - **intro-to-3d-modeling**
    - What is a 3D model?
    - File types: STL, OBJ, STEP, 3MF
  - **design-thinking-for-printing**
    - Thinking in layers: how printers interpret shapes
    - Overhangs, bridging, supports
    - Common beginner mistakes (thin walls, unsupported features, tiny details)
  - **tools-for-3d-modeling**
    - Tinkercad (for USF students) - taught in class but will touch on the subject here as a "what is"
    - How to export for printing - instructions for this - will add images later.

Welcome to the "3D Design for Printing" section! Here, we'll explore how to create effective 3D models for printing, understand key file formats, and utilize tools like Tinkercad to bring your designs to life.

Introduction to 3D Modeling
===========================

What is a 3D Model?
-------------------

A 3D model is a digital representation of a physical object, defined by its geometry, shape, and structure. These models are created using Computer-Aided Design (CAD) software and are essential for 3D printing, as they provide the blueprint that printers follow to build objects layer by layer.

Common 3D File Formats
----------------------

Understanding different file formats is crucial for 3D printing:

- STL (Stereolithography): The most widely used format, representing models as a mesh of triangles. It doesn't support color or material information.
- OBJ (Object File): Supports color and texture information, making it suitable for more detailed models.
- STEP (Standard for the Exchange of Product Model Data): Used for sharing models between different CAD programs, preserving complex geometry and assembly information.
- 3MF (3D Manufacturing Format): A modern format that includes color, material, and other metadata, aiming to be a comprehensive solution for 3D printing needs.

Design Thinking for Printing
============================

Thinking in Layers
-------------------

3D printers build objects layer by layer. This additive process means that each new layer must be supported by the one below it.
Designing with this in mind ensures structural integrity and printability.

Overhangs, Bridging, and Supports
----------------------------------

- Overhangs: Parts of the model that extend outward without support beneath can cause issues. Angles greater than 45 degrees typically require support structures to print successfully.
- Bridging: Spanning gaps between two points can be challenging. Short bridges (less than 5mm) can often be printed without support, but longer spans may need additional structures.
- Supports: Temporary structures added during printing to support overhangs and bridges. They are removed after printing but can affect surface finish where they contact the model.

Common Beginner Mistakes
-------------------------
- Thin Walls: Walls thinner than the printer's nozzle diameter can lead to weak prints or failures.
- Unsupported Features: Elements like floating parts or steep overhangs without support can cause print issues.
- Tiny Details: Features smaller than the printer's resolution may not print accurately.


Tools for 3D Modeling
=====================

Tinkercad
---------

Tinkercad is an online, user-friendly CAD tool ideal for beginners. It allows you to create 3D models using simple shapes and operations, making it perfect for educational purposes and basic designs.


Exporting for Printing
----------------------

.. ! NOTE: Need images here and better explanation.

Once your design is complete in Tinkercad:

1. **Click on "Export"**: Located in the upper-right corner of the Tinkercad interface.
2. **Choose the File Format**: Select .STL for 3D printing.
3. **Download the File**: The file will be saved to your computer, ready to be imported into slicing software like OrcaSlicer.

-----

By understanding 3D modeling principles, file formats, and using tools like Tinkercad, you're well-equipped to create designs ready for 3D printing. Remember to consider the printing process during design to ensure successful prints.