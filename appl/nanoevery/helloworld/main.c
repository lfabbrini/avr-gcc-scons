#include <avr/io.h>
#include <util/delay.h>

#define MS_DELAY 1000
#define BUILTIN_LED_PORT PORTE
#define BUILTIN_LED_PIN _BV(2)

int main (void) {

    /*Set to one the BUILTIN_LED_PIN bit
    **Set digital pin to output mode */
    BUILTIN_LED_PORT.DIRSET = BUILTIN_LED_PIN;
    _PROTECTED_WRITE(CLKCTRL_MCLKCTRLB, 0x00); //set No division on clock
    while(1) {
        /*Set to one the BUILTIN_LED_PIN
        **Set to HIGH the pin */
        BUILTIN_LED_PORT.OUTSET = BUILTIN_LED_PIN;

        /*Wait MS_DELAY ms */
        _delay_ms(MS_DELAY);

        /*Set to zero the BUILTIN_LED_PIN
        **Set to LOW the pin */
        BUILTIN_LED_PORT.OUTCLR = BUILTIN_LED_PIN;

        /*Wait MS_DELAY ms */
        _delay_ms(MS_DELAY);
    }
}
