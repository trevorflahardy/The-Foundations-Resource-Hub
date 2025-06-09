### Which character begins a single-line comment in Arduino?
1. [x] //
    > Correct. Double slashes begin a comment.
1. [ ] /**
1. [ ] <!--

### Which two functions must be present in every Arduino sketch?
> These functions define what happens once and what repeats.
- [x] setup()
- [x] loop()
    > Both are required by the Arduino framework.
- [ ] main()
- [ ] start()

### What does this sketch print to the Serial Monitor?
```cpp
void setup() {
  Serial.begin(9600);
  Serial.println("Hi");
}

void loop() {}
```
> `setup()` runs once before `loop()`.
1. [ ] It prints nothing.
1. [x] It prints "Hi" once.
    > `Serial.println` in `setup()` executes a single time.
1. [ ] It prints "Hi" repeatedly.
1. [ ] It prints "HiHi".
