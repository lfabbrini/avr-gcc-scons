#include <avr/io.h>
#include <util/delay.h>

#define MS_DELAY 1000
#define BUILTIN_LED_PORT PORTB
#define BUILTIN_LED_DDR  DDRB
#define BUILTIN_LED_PIN _BV(5)

int main (void) {
    /*Set to one the fifth bit of DDRB to one
    **Set digital pin 13 to output mode */
    BUILTIN_LED_DDR |= BUILTIN_LED_PIN;

    while(1) {
        /*Set to one the fifth bit of PORTB to one
        **Set to HIGH the pin 13 */
        BUILTIN_LED_PORT |= BUILTIN_LED_PIN;

        /*Wait 3000 ms */
        _delay_ms(MS_DELAY);

        /*Set to zero the fifth bit of PORTB
        **Set to LOW the pin 13 */
        BUILTIN_LED_PORT &= ~BUILTIN_LED_PIN;

        /*Wait 3000 ms */
        _delay_ms(MS_DELAY);
    }
}
