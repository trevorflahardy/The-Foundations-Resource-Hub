### Which loop is best for iterating a known number of times?
> Use this loop when you know exactly how many iterations you need.
1. [x] for loop
    > Correct. `for` loops handle a fixed count.
1. [ ] while loop
1. [ ] loop()
    > `loop()` is the main Arduino function, not a counting loop.

### Which statement stops a loop immediately?
> Think about prematurely ending the loop.
1. [ ] continue
1. [x] break
    > `break` exits the loop immediately.
1. [ ] next

### What numbers does this loop print?
```cpp
for (int i = 1; i <= 3; i++) {
    Serial.println(i);
}
```
> Look at the starting value and end condition.
1. [x] 1 2 3
    > The loop begins at 1 and stops after printing 3.
1. [ ] 0 1 2
1. [ ] 0 1 2 3
1. [ ] 2 3 4
