.. _responsible_3d_printing:

========================
Responsible 3D Printing
========================

Many things go into 3D printing, so proper knowledge of the protocols is pivotal to producing quality prints. Additionally, 3D printers are sophisticated, delicate machines, and as such need to be treated with the utmost care.

This guide details the rules, expectations, and best practices you'll need to follow when 3D printing for ``EGN 3000L``.

DFX Lab
=======

.. important::

   You **must** complete the DFX lab safety training before using any equipment in the lab, including our 3D printers. Find a time and sign up for the training here: `see the training page <http://www.eng.usf.edu/dfx/labtrainings.html>`_.

The Foundations of Engineering Lab administration are not employees or representatives of the DFX lab, but, the courses' 3D printers are located there. So, in addition to the rules outlined in this guide, you **must** follow the DFX lab's rules and expectations as well. These are **non-negotiable** in the lab for your safety.

.. note::

   **Engineering Lab Course Printers vs. DFX Lab Printers**

   Foundations operates its own 3D printers within the DFX lab space. These course printers are **only for students enrolled in the Foundations course** and cannot be used by other students not enrolled in the course, including all DFX lab users.

   If you want to use the DFX lab's own 3D printers, you'll need to complete DFX's dedicated 3D printer training, and can sign up using the `DFX lab's training page <http://www.eng.usf.edu/dfx/labtrainings.html>`_.

The full list of DFX lab rules should be reviewed `here <http://www.eng.usf.edu/dfx/labrules.html>`_, but these are some of the most important ones to keep in mind:

- General operating hours are **Monday through Friday 8am to 5pm** when the University is normally open.
- **No food or drink** is allowed in this lab except for the designated storage areas.
- All tools, support supplies and accessory equipment housed in this lab are for consumption and use in this lab and **should not be removed** or borrowed unless approved by the laboratory manager.
- All **supplies or projects brought to the lab should NOT be stored in the lab** unless a storage area has been reserved by a lab staff member.
- Cleaning your work area is essential. For the rapid prototyping tools you will be shown how to leave the tool when you are finished. **Do not leave personal items in this lab**.
- Report any equipment problem, messes left by others, water leaks, missing items, or any unusual events to a TSS staff immediately. Tool or facilities modifications to equipment should not be done unless approved by the Lab Manager.
- You **must be trained and certified to use the tools in this lab**. Please see the NREC Office for monthly training sessions offered or card access rights to this lab.

Failing to follow the lab's rules may result in consequences from both the lab and from us. These can include permanent banishment from the lab, fees, and/or a failing grade in the course.

.. _printing_workflow_at_usf:

Printing Workflow Overview
==========================

It's helpful to understand the overall workflow. This guide will go deeper into detail, but here's a quick overview of the process:

1. **Prepare Your Design**
   Ensure your CAD model is ready and export it as an STL file. Double-check dimensions and make sure your design is printable.

2. **Slice Your Model**
   Use the lab computers or bring your own laptop with slicing software to prepare your print file (G-code).

3. **Start Your Print**
   Check everything (filament, bed, file) and begin your print, ensuring you stay nearby for the first few layers.

4. **Monitor Progress**
   Check on your print periodically. Long prints don't need constant supervision, but regular check-ins are important.

5. **Remove and Clean Up**
   Once finished and cooled, carefully remove your print and clean up any support material or debris.

.. _rules_etiquette_lab:

Rules & Etiquette around the Printers
=====================================

Beyond the official DFX lab rules, here are some key dos and don'ts to keep in mind when printing:

Before You Start
-----------------

✅ **DO:**

- Check that there's enough filament loaded for your print (look at the spool and estimate).
- Verify the bed is clean and free of previous print residue.
- Check that the build plate is properly installed and secure.

❌ **DON'T:**

- Start a print without checking filament levels
- Pause, cancel, or touch someone else's active print without permission.
- Leave prints unattended for at least several minutes after starting them.
- Bump, jostle, or unlock the wheels of the printer racks.

During Your Print
------------------

✅ **DO:**

- Monitor the first few layers closely - most failures happen early.
- Check on longer prints periodically (every 2-3 hours for prints over 4 hours).
- Take photos of any problems if you plan on requesting troubleshooting help.
- Keep the area around the printer clean and organized.

❌ **DON'T:**

- Bring food or drinks near the printers (this is a DFX lab rule).
- Adjust printer settings mid-print unless absolutely necessary.
- Touch or move the printer/racks while printing.
- Touch hot/moving parts of the printer.
- Walk away for hours without checking on your print.

After Your Print
-----------------

✅ **DO:**

- Let the bed cool completely before removing your print.
- Clean up any failed print material or support debris.
- Return the build plate immediately after removing your print.
- Report any issues or unusual printer behavior to staff.

.. _starting_your_first_print:

Starting Your First Print
=========================

.. TODO:
   Add images for the printers, spools, etc so students can have a visual walk-through and reference as well. This
   is vital.

Your first print is exciting, and following these steps will set you up for success:

Pre-Flight Checklist
---------------------

Before starting any print, run through this quick checklist:

1. **Filament Check**: Ensure there's enough filament for your entire print, plus some extra.
2. **Bed Preparation**: Ensure the build plate is free of debris and leftover filament.
3. **File Verification**: Double-check your G-code file is correctly named so staff doesn't cancel it.

Starting the Print
------------------

1. **Load Your File**
   Transfer your G-code file to the printer via USB-drive.

2. **Start and Stay Close**
   Begin the print and **stay nearby for at least the first 10 minutes**. This is when most issues occur:

   - Watch the first layer go down - it should stick well to the bed.
   - Listen for unusual sounds (grinding, clicking, or excessive noise).
   - Look for proper filament extrusion from the nozzle.

What to Watch For
-----------------

During those crucial first layers, keep an eye out for:

- **Poor bed adhesion**: Corners lifting or entire first layer not sticking.
- **Over/under-extrusion**: Too much plastic (blobbing) or too little (gaps in lines).
- **Nozzle clogs**: No filament coming out, or very thin/inconsistent extrusion.
- **Layer misalignment**: Print shifting horizontally between layers.

.. tip::

   If something looks wrong in the first few layers, it's usually better to stop the print early and troubleshoot rather than letting it continue to waste time and material.

.. _troubleshooting_basics:

Troubleshooting Basics
======================

Even experienced engineers expect to encounter failures occasionally. The key is knowing when to intervene and when to let the print continue.

**Quick Decision Guide:**

- **Cancel immediately**: Major bed adhesion failure, severe layer shifts, or filament jams
- **Monitor closely**: Minor stringing, small layer shifts, or support issues that don't affect the main print
- **Quick fixes**: Minor warping (press down gently), loose filament, or temperature fluctuations

For detailed troubleshooting of specific issues like warping, layer shifts, and stringing, see the iterating design page.

.. _safety_first:

Safety First
============

3D printers involve high temperatures, moving parts, and electrical components. Here's how to stay safe while printing:

What NOT to Touch
-----------------

.. warning::

   These components can cause burns, injury, or damage to the printer if touched during operation:

- **Hot End/Nozzle**: Can reach 200-260°C (390-500°F).
- **Heated Bed**: Typically 50-80°C (120-175°F).
- **Moving parts**: Print head, bed, and any moving carriages during operation.
- **Electrical connections**: Never attempt to repair or modify electrical connections. This includes the power cable, power supply, and any internal wiring.

Mechanical Cautions
-------------------

- Don't force any moving parts - they should move smoothly.
- Never try to "help" the printer by pushing or pulling parts during operation.
- Keep fingers, hair, and loose clothing away from moving components.
- Don't attempt to clear jams or clogs, just stop the print and ask for help.
- The filament spool should not be touched or removed. If you need to change filament, stop the print **before it reaches the end** and ask for assistance.

If Something Goes Wrong
-----------------------

In case of critical issues follow these steps in order:

1. **Stop the Print**: Attempt to stop the print using the screen. The job should stop immediately, and the extruder will return to the home position.

2. **Power Off**: If the screen on the printer is unresponsive, use the printer power switch, located on the back of the printer near its power cable.

3. **Get Help Immediately**: Contact a TA or DFX staff member right away. Don't try to fix electrical or mechanical issues yourself.

4. **Document the Issue**: Take photos if safe to do so - this helps staff diagnose problems and understand what went wrong.

Emergency Contacts
------------------

- **For immediate safety concerns**: Call campus security or 911.
- **For equipment issues**: Contact DFX lab staff or your TA immediately.
- **Never attempt repairs yourself** - this can break printers or cause further issues.

.. note::

   Equipment can be replaced, but injuries cannot be undone. When in doubt, stop the print and ask for help. No print is worth risking your safety or the safety of others.

Personal Safety Gear
---------------------
Close-toed shoes are the only requirement for 3D printing, however if you're using other tools in the DFX lab you may need specialized safety gear. Always reference the DFX lab's safety guidelines for the specific tools you're using.

.. _consequences_violations:

Consequences for Rule Violations
================================

Violating the 3D printing rules of our course or the DFX lab will lead to serious consequences.

- If you break a DFX lab rule and they choose to take action, we will also impose our own, separate consequences.
- Breaking one of our course rules will result in our own punishment, but may not result in DFX lab consequences.

Consequences for rule violations are typically assessed on a case-by-case basis but can include:

- **Academic:** Point deductions, failing assignments, or failing the course in severe cases.
- **Lab Access:** The DFX lab may revoke entire-lab access if you violate their rules, but violating our course rules will not result in loss of access to the DFX lab.
- **Printing Privileges:** You may lose the ability to use our 3D printers. If this happens it will be indefinitely.
- **Financial:** All violations that damage equipment or require repairs will hold you responsible for the repair cost and possible extra fees. Financial reparations are the bare minimum, and are always accompanied by conventional consequences.

**Common violations include:** Not cleaning up, damaging equipment, safety violations, or filament overuse.

We will not hesitate to enforce the rules, regardless of if you're ignorant or simply choose to ignore them.

----

3D printing in ``EGN 3000L`` is an incredible opportunity to manufacture parts like professional engineers. Success requires preparation, attention, and following the rules.