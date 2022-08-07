#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/cpufunc.h>
#include <util/delay.h>

#define MS_DELAY 500
#define TCB_TIMEOUT_VALUE 0x7fff
#define BUILTIN_LED_PORT PORTE
#define BUILTIN_LED_PIN PIN2_bm

void CLOCK_init (void);
void PORT_init (void);
void EVENT_SYSTEM_init (void);
void TCB0_init (void);

void CLOCK_init (void)
{
    /* Disable CLK_PER Prescaler */
    ccp_write_io( (void *) &CLKCTRL.MCLKCTRLB , (0 << CLKCTRL_PEN_bp));
    
    /* Select 32KHz Internal Ultra Low Power Oscillator (OSCULP32K) */
    ccp_write_io( (void *) &CLKCTRL.MCLKCTRLA , (CLKCTRL_CLKSEL_OSCULP32K_gc));
   
    /* Wait for system oscillator changing to finish */
    while (CLKCTRL.MCLKSTATUS & CLKCTRL_SOSC_bm)
    {
        ;
    }
}

void PORT_init (void)
{
    BUILTIN_LED_PORT.DIR |= BUILTIN_LED_PIN; /* Configure BUILTIN_LED_PIN as digital output */
    BUILTIN_LED_PORT.OUT |= BUILTIN_LED_PIN; /* Set initial level of BUILTIN_LED_PIN */

    PORTB.DIR |= PIN1_bm; /* Configure PB1 as digital output */
    PORTB.OUT |= PIN1_bm; /* Set initial level of PB1 */
    PORTB.DIR &= ~PIN2_bm; /* Configure PB2 as digital input */

    // PORTB.PIN2CTRL = PORT_PULLUPEN_bm; /* Enable the internal pullup */
}

void EVENT_SYSTEM_init (void)
{
    /* Set Port 1 Pin 2 (PB2) as input event*/
    EVSYS.CHANNEL0 = EVSYS_GENERATOR_PORT1_PIN2_gc;
    /* Connect user to event channel 0 */
    EVSYS.USERTCB0 = EVSYS_CHANNEL_CHANNEL0_gc;
}

void TCB0_init (void)
{
    /* Load the Compare or Capture register with the timeout value*/
    TCB0.CCMP = TCB_TIMEOUT_VALUE;
    
    /* Enable TCB and set CLK_PER divider to 1 (No Prescaling) */
    TCB0.CTRLA = TCB_CLKSEL_CLKDIV1_gc | TCB_ENABLE_bm;
    
    /* Configure TCB in Periodic Timeout mode */
    TCB0.CTRLB = TCB_CNTMODE_TIMEOUT_gc;
    
    /* Enable Capture or Timeout interrupt */
    TCB0.INTCTRL = TCB_CAPT_bm;
    
    /* Enable Event Input and Event Edge*/
    TCB0.EVCTRL = TCB_CAPTEI_bm | TCB_EDGE_bm;
}

ISR(TCB0_INT_vect)
{
    TCB0.INTFLAGS = TCB_CAPT_bm; /* Clear the interrupt flag */
    PORTB.OUTTGL = PIN1_bm; /* Toggle PB1 GPIO */
}

int main(void)
{
    CLOCK_init();
    PORT_init();
    EVENT_SYSTEM_init();
    TCB0_init();

    sei(); /* Enable Global Interrupts */
    
    while (1)
    {
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


