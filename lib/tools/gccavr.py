"""SCons Tool for AVR-GCC.

"""


import os
import gcc
import SCons
def generate(env):
    # print('AVR GENERATE')
    env.PrependENVPath('PATH', env.subst(os.path.join('$GCCAVRDIR', 'bin')))
    #use Unique here because Scons enter here 2 times
    env.PrependUnique(CPPPATH=[
        os.path.join('$GCCAVRDIR','lib','gcc','avr','7.3.0','include'),
        os.path.join('$GCCAVRDIR','lib','gcc','avr','7.3.0','include-fixed'),
        os.path.join('$GCCAVRDIR','avr','include')
    ])
    env['CCFLAGS'] = SCons.Util.CLVar('-std=gnu11 -pedantic -Wall -Wextra -Wno-unused-parameter -Werror')
    env['GCCPREFIX'] = 'avr-'
    env['MAPFILE'] = True

    env['PROGSUFFIX'] = '.elf'
    env['ROMSUFFIX'] = '.hex'
    env['ROMCOM'] = 'avr-objcopy -O ihex -R .eeprom $SOURCE $TARGET'
    env['ROMFORMAT'] = 'INHX'

    env['CXXFLAGS']   = SCons.Util.CLVar('-w -std=gnu++11 -fpermissive -fno-exceptions -fno-threadsafe-statics -Wno-error=narrowing')
    env['GPPPREFIX'] = 'avr-'
    env['CXXFILESUFFIX'] = '.cpp'


    env['AR'] = '${GCCPREFIX}ar${GCCSUFFIX}'
    env['ASFLAGS'] = '-x assembler-with-cpp'

def exists(env):
    return None
