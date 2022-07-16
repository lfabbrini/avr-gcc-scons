"""SCons Tool for AVR-GCC.

"""


import os
import gcc

def generate(env):
    env.PrependENVPath('PATH', env.subst(os.path.join('$GCCAVRDIR', 'bin')))
    #use Unique here because Scons enter here 2 times
    env.PrependUnique(CPPPATH=[
        os.path.join('$GCCAVRDIR','lib','gcc','avr','7.3.0','include'),
        os.path.join('$GCCAVRDIR','lib','gcc','avr','7.3.0','include-fixed'),
        os.path.join('$GCCAVRDIR','avr','include')
    ])
    env['MAPFILE'] = True
    env['GCCPREFIX'] = 'avr-'
    env['PROGSUFFIX'] = '.elf'
    env['ROMSUFFIX'] = '.hex'
    env['ROMCOM'] = 'avr-objcopy -O ihex -R .eeprom $SOURCE $TARGET'
    env['ROMFORMAT'] = 'INHX'

    gcc.generate(env)
    env['AR'] = '${GCCPREFIX}avr-ar${GCCSUFFIX}'


def exists(env):
    return None
