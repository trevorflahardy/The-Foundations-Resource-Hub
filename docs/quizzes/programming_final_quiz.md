### Which file extension do Arduino sketches use?
1. [ ] .cpp
1. [x] .ino
   > Arduino saves code in sketch files that end with the .ino extension.
1. [ ] .exe

### Which microcontroller board is used in this course?
1. [x] Arduino Uno
   > The guide uses the Arduino Uno because it is beginner friendly and well supported.
1. [ ] Raspberry Pi Pico
1. [ ] ESP32

### Which function runs once when your board starts?
1. [x] setup()
   > The setup() function executes a single time at startup for initialization.
1. [ ] loop()
1. [ ] start()

### Which function contains code that repeats forever?
1. [ ] setup()
1. [x] loop()
   > Code inside loop() runs continuously after setup() finishes.
1. [ ] repeat()

### Which character ends most lines of Arduino code?
1. [x] ;
   > A semicolon terminates statements in the Arduino language.
1. [ ] :
1. [ ] ,

### How do you write a single-line comment?
1. [x] // comment
   > Two forward slashes mark the start of a single-line comment.
1. [ ] <!-- comment -->
1. [ ] /* comment */

### Which data type stores whole numbers like 42?
1. [x] int
   > The int type holds integer values.
1. [ ] float
1. [ ] char

### Which data type holds true or false values?
1. [ ] int
1. [ ] float
1. [x] bool
   > Boolean variables store either true or false.

### Why would you use an array in your sketch?
1. [x] To store a collection of related values under one name
   > Arrays keep grouped data organized and accessible.
1. [ ] To run code repeatedly
1. [ ] To comment multiple lines at once

### What index accesses the first element of an array?
1. [x] 0
   > Arduino arrays are zero-indexed, so the first element uses index 0.
1. [ ] 1
1. [ ] 2

### How do you reference the third element of `values`?
1. [x] values[2];
   > Index 2 retrieves the third element because arrays start counting at 0.
1. [ ] values(3);
1. [ ] values<2>;

### Which keyword sends a value back from a function?
1. [x] return
   > The return keyword passes data back to the caller.
1. [ ] send
1. [ ] break

### Which operator yields the remainder of a division?
1. [ ] /
1. [x] %
   > The modulus operator % returns the remainder.
1. [ ] *

### Which control structure is ideal for checking many discrete cases of a variable?
1. [x] switch
   > A switch statement branches based on specific constant values.
1. [ ] if
1. [ ] while

### Which loop is best for repeating an action a set number of times?
1. [x] for loop
   > A for loop combines initialization, condition, and update for fixed iterations.
1. [ ] while loop
1. [ ] if-else chain

### Which loop always executes its body at least once?
1. [ ] while loop
1. [x] do...while loop
   > A do...while loop evaluates its condition after the first iteration.
1. [ ] for loop

### Which function initializes serial communication at 9600 bps?
1. [x] Serial.begin(9600);
   > Serial.begin sets up the serial port speed.
1. [ ] Serial.print(9600);
1. [ ] Serial.open(9600);

### On the Arduino Uno, which pin is connected to the onboard LED used in the second program?
1. [ ] 7
1. [x] 13
   > Pin 13 controls the built-in LED on the Uno.
1. [ ] A0

### Which directive adds an external library to your sketch?
1. [x] #include <Servo.h>
   > The #include directive pulls in library code for use in your program.
1. [ ] import Servo;
1. [ ] using Servo;

### According to the code disclaimer, why might a snippet fail if pasted directly into the IDE?
1. [x] It may omit setup(), loop(), or other required parts
   > Many examples focus on concepts and leave out surrounding boilerplate code.
1. [ ] The IDE blocks copied code
1. [ ] Arduino boards cannot run pasted code

### Which toolbar button verifies code without uploading it?
1. [x] The checkmark/Verify button
   > Verify compiles your sketch to check for errors without uploading.
1. [ ] The Upload arrow
1. [ ] The serial monitor icon
