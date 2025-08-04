.. _preparing_to_print:

******************
Preparing to Print
******************

You now have a model, but now what? Before you can print, you need to prepare it using slicing software. This is where we turn your 3D model into instructions that the printer can understand.

.. _what_is_slicing:

What is Slicing?
================

:Slicing: is the process of turning your digital 3D model into printable instructions—layer by layer. These instructions are saved as a special file called :term:`G-code`, which your printer follows line by line.

Think of it like converting a sculpture into instructions for a robot to carve it out—except instead of carving, it's building it up, one layer at a time!

Understanding Key Slicing Concepts
----------------------------------

Before we dive into using the software, let's cover some basic slicing terms. Don't worry if you don't get all the terms right away; you'll become familiar with them as you slice models and continue through this guide.

Infill
^^^^^^^

:term:`Infill` is the internal pattern that fills the inside of your model. Our model's cannot be hollow, can they? Of course, not, so infill gives our object **strength and stability**. You won't see it the inside of your model once it is done printing, but infill is crucial for making sure your print doesn't fall apart.

There are several types of infill patterns you can use, each with their own strengths and weaknesses. Let's walk through the most common ones you'll encounter.

Rectilinear Infill Pattern [#f1]_
""""""""""""""""""""""""""""""""""

.. figure:: /images/3d_printing/infill_types/rectilinear.png
  :align: center
  :alt: Rectilinear Infill Pattern

This pattern features a single diagonal line direction per layer, with alternating orientations between adjacent layers (e.g., layers 1, 3, and 5 share the same direction, while layers 2, 4, and 6 are perpendicular), forming a non-continuous grid structure.

The use of a single-direction line per layer significantly shortens the print path, greatly improving print speed and reducing filament consumption. It is suitable for scenarios where the model does not require high structural strength.

Gyroid Infill Pattern [#f1]_
""""""""""""""""""""""""""""

.. list-table:: Gyroid Infill Examples
   :widths: 33 33 33
   :header-rows: 0

   * - .. figure:: /images/3d_printing/infill_types/gyroid_1.png
          :align: center
          :alt: Gyroid Pattern 1

          **Low Density (10%)**

     - .. figure:: /images/3d_printing/infill_types/gyroid_2.png
          :align: center
          :alt: Gyroid Pattern 2

          **Medium Density (25%)**

     - .. figure:: /images/3d_printing/infill_types/gyroid_3.png
          :align: center
          :alt: Gyroid Pattern 3

          **High Density (50%)**

This infill pattern is a type of three-period minimal surface (TPMS) lattice structure. The spiral shape provides excellent support in all dimensions, and since there are no intersecting lines within the same layer, it offers relatively fast printing speeds.

However, due to the more complex printing path, slicing time will be longer, resulting in larger G-code files. Additionally, at higher densities and during high-speed printing, significant vibrations may occur.

----

At USF, you will mainly be using the **Grid** infill pattern, as it provides a good balance of strength and print speed. However, you can experiment with others as you become more comfortable with slicing.

But what about when your model has **overhangs** or **bridges**? These are parts of the model that extend out without support underneath, and they can be tricky to print. That's where :term:`supports` come in.

Supports
^^^^^^^^

When printing models with overhangs (parts that extend out without support underneath), you may need to add :term:`supports`. These are temporary structures printed alongside your model to hold up any parts that would otherwise sag or fall during printing.

Supports come in many types, but the only you will be using at the USF print lab is the :term:`tree supports` and :term:`normal supports`.

Tree Supports
"""""""""""""

:term:`Tree supports <tree supports>` samples the overhangs to get something called "nodes". Each node is represented as a circle, the nodes are propagated (joined) down to the heat bed. During propagation, the circles may be enlarged to get better strength and may be moved away from the object so the supports are less likely to collide with the object [#f2]_.

But when do I use tree supports over normal supports? For objects with **complex structures** and most of the :term:`overhangs <Overhang>` are small, non-planar surfaces, tree supports give stronger support structure, less material, and less time cost, while keeping similar surface quality [#f2]_.

.. image:: /images/3d_printing/supports/when_tree.png
  :align: center
  :alt: When to use Tree Supports

How about non-complex structures? Tree supports are still useful for large overhangs, as they provide a strong support structure with less material used compared to normal supports. They also make it easier to remove the supports after printing.

Normal Supports
""""""""""""""""

:term:`Normal supports <normal supports>` are the traditional support structures that are printed directly under the :term:`overhangs <Overhang>`. They can be removed after printing, but they may leave marks on the model.

But when do I use normal supports over tree supports? For **large planar overhang**, Normal supports usually give better surface quality than tree supports.

.. image:: /images/3d_printing/supports/when_normal_1.png
  :align: center
  :alt: When to use Normal Supports


.. image:: /images/3d_printing/supports/when_normal_2.png
  :align: center
  :alt: When to use Normal Supports

Key Differences
"""""""""""""""
So we have covered both types of supports, normal and tree, but which one should you use? It really depends on your model's geometry and the specific overhangs you need to support.

- **Tree Supports**:
  - Best for complex structures with small, non-planar overhangs.

  - Stronger support with less material.

  - Less time cost.

  - Easier to remove.
- **Normal Supports**:
  - Best for large planar overhangs.

  - Better surface quality.

  - May leave marks on the model.

  - More material used.

Which to use depends on your model's geometry and the specific overhangs you need to support. As you gain experience, you'll develop a feel for which type works best in different situations. Always feel free to reach out for help if you are unsure!

.. ! NOTE: Keep walking through the following list items and making them their own section, using the Bambu Labs wiki as reference
.. ! for images, content, and flow of document.

..
  [TODO]: Walk through bambu labs and make these their own section:

Layer Height
^^^^^^^^^^^^^

Layer height refers to the vertical thickness of each deposited layer of molten material (measured in millimeters), and it is one of the most critical parameters influencing both print quality and print speed.

.. image:: /images/3d_printing/layer_height_1.png
  :align: center
  :alt: An image showing what layer height is.

For example, with a 0.4 mm nozzle:

- A **smaller layer height** (e.g., **0.12 mm**) results in finer layering, producing smoother surfaces and better detail, but **significantly increases** print time.
- A **larger layer height** (e.g., **0.28 mm**) allows for **faster print speeds**, but may lead to **visible layer lines** and loss of detail.

.. image:: /images/3d_printing/layer_height_2.png
  :align: center
  :alt: An image showing the difference in layer height.

**Recommended settings** for layer height:

- **Standard Quality**: 0.2 mm
- **High Quality**: 0.12 mm
- **Draft Quality**: 0.28 mm

Wall Count
^^^^^^^^^^^^^
This parameter defines the number of outer shell layers, which directly affects both the strength and surface quality of the printed model. It is generally recommended to set it between 2 and 4 layers, depending on your specific needs.

As shown in the image below, the wall structure typically includes:

- **Orange**: Outer walls
- **Yellow**: Inner walls

.. image:: /images/3d_printing/wall_count_1.png
  :align: center
  :alt: An image showing the wall count.

**Recommended Settings:**

- **Functional parts**: Set to 3-4 walls to enhance structural strength and durability.
- **Decorative models**: 2 walls are sufficient to save material and improve print efficiency.

Brim/Raft
^^^^^^^^^^^^^
A :term:`brim` is a single-layer flat area around the base of your model. Its purpose is to keep the edges of your print down and make the contact area between your print and the build plate bigger.

- The bigger surface area allows your print to stick better on the build plate. This is pretty useful for tall and thin objects.
- Brim can also help improve the bonding of the edges on the bottom of the model. Having a brim of sufficient width will keep the model edges in place, preventing this warping.

.. image:: /images/3d_printing/brim_1.png
  :align: center
  :alt: An image showing the brim.

As discussed in :ref:`bed_adhesion`, a brim is a great way to improve bed adhesion, especially for models with small contact areas. In Orca Flashforge, you can enable a brim in the slicing settings.

It is **recommended** to set the brim to **auto** for most prints, as it will automatically adjust the brim width based on the model's size and shape.

.. image:: /images/3d_printing/brim_2.png
  :align: center
  :alt: An image showing the brim settings in Orca Flashforge.

..
  Skipped brim-object gap and manual brim information. Maybe add in the future, but it felt excessive for now.

Orientation
^^^^^^^^^^^^^
  How your part is positioned on the print bed. This affects print time, strength, and support needs.

Plate
^^^^^^
  A virtual “build plate” in Orca Flashforge. You can organize prints across multiple plates if needed.

.. tip::

   You don't need to change all these settings manually—our printer profiles will handle most of it. But knowing what these mean will help you troubleshoot and customize when you're ready!

---

.. _orca_flashforge_setup:

Getting Started with Orca Flashforge
====================================

So we know *about* slicing now, but we need to get your slicing software ready to go! Orca Flashforge is a customized version of OrcaSlicer, built specifically for the FlashForge Adventurer 5M series that you'll be using in the lab.

Installing Orca Flashforge
--------------------------

1. **Download Orca Flashforge**

Head to the `Flashforge Downloads Page <https://www.flashforge.com/blogs/download-document/adventurer-5m-pro#>`_ and grab the latest installer for your operating system (Windows 10+ or macOS 10.15+).

.. ! TODO: image needed

2. **Run the Installer**

Follow the on-screen prompts. The setup is simple and shouldn't take more than a minute or two.

.. ! TODO: image needed

3. **Launch the App**

Open Orca Flashforge, and the setup wizard will guide you through initial configuration.

.. ! TODO: image needed

Setup Wizard Walkthrough
-------------------------

The first time you launch Orca Flashforge, you'll see a few friendly setup prompts:

- **Login Region** - Simply pick your region (“North America”).
- **Select Printer** - Choose the printer model you'll be using: ``Adventurer 5M``.
- **Select Nozzle Size** - Pick the nozzle size available in the lab: ``0.4mm``.
- **Select Filaments** - Choose the filaments you'll be printing with: ``PLA``.

.. ! TODO: images needed

That's it! You're now ready to load models and start slicing.

.. important::

  Although Orca Flashforge can wirelessly connect to 3D printers, at USF, you'll export G-code to a USB drive and physically plug it into the printer. Easy and reliable!

We'll cover how to export your sliced models below.

-----

.. [#f1] Adapted from Bambu Labs tutorial on infill patterns, available at: https://wiki.bambulab.com/en/software/bambu-studio/fill-patterns

.. [#f2] Adapted from Bambu Labs Wiki on supports, available at: https://wiki.bambulab.com/en/software/bambu-studio/support