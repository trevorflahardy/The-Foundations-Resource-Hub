### Which function runs once at the start of your Arduino program?
> This function is called before `loop()`.
1. [x] setup()
    > Correct. `setup()` runs a single time.
1. [ ] loop()
1. [ ] main()

### Where should you set `pinMode()` calls?
- [x] Inside `setup()`
    > Setup configures hardware before looping.
- [ ] Inside `loop()`
- [ ] Outside of any function

### What will the built-in LED do in this program?
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void loop() {}
```
> The LED is turned on once in `setup()`.
1. [x] It turns on and stays on.
    > `digitalWrite` sets the LED HIGH and `loop()` does nothing else.
1. [ ] It blinks forever.
1. [ ] It never turns on.
