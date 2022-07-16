#include <avr/io.h>
#include <util/delay.h>

#define MS_DELAY 250
#define BUILTIN_LED_PORT PORTE
#define BUILTIN_LED_PIN _BV(2)

int main (void) {
    /*Set to one the fifth bit of DDRB to one
    **Set digital pin to output mode */
    BUILTIN_LED_PORT.DIRSET |= BUILTIN_LED_PIN;

    while(1) {
        /*Set to one the fifth bit of PORTB to one
        **Set to HIGH the pin */
        BUILTIN_LED_PORT.OUT |= BUILTIN_LED_PIN;

        /*Wait 3000 ms */
        _delay_ms(MS_DELAY);

        /*Set to zero the fifth bit of PORTB
        **Set to LOW the pin */
        BUILTIN_LED_PORT.OUT &= ~BUILTIN_LED_PIN;

        /*Wait 3000 ms */
        _delay_ms(MS_DELAY);
    }
}
