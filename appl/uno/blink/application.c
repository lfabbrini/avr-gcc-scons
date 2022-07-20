#include <Arduino.h>
#include "application.h"

#define MS_DELAY 500

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(MS_DELAY);                   // wait for MS_DELAY
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(MS_DELAY);                   // wait for MS_DELAY
}
