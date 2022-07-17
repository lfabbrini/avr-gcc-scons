"""SCons Tool for AVR-GCC.

"""


import os
import SCons

def generate(env):
    import SCons.Tool.cxx

    env.PrependENVPath('PATH', env.subst(os.path.join('$GCCAVRDIR', 'bin')))
    #use Unique here because Scons enter here 2 times
    env.PrependUnique(CPPPATH=[
        os.path.join('$GCCAVRDIR','lib','gcc','avr','7.3.0','include'),
        os.path.join('$GCCAVRDIR','lib','gcc','avr','7.3.0','include-fixed'),
        os.path.join('$GCCAVRDIR','avr','include')
    ])
    # SCons.Tool.cxx.generate(env)
    env['CXX'] = '${GPPPREFIX}g++${GPPSUFFIX}'
    env['CXXFLAGS']   = SCons.Util.CLVar('-w -std=gnu++11 -fpermissive -fno-exceptions -fno-threadsafe-statics -Wno-error=narrowing')
    env['GPPPREFIX'] = 'avr-'
    env['CXXFILESUFFIX'] = '.cpp'
    env['CXXCOM']     = '$CXX -o $TARGET -c $CXXFLAGS $_CPPDEFFLAGS $_CPPINCFLAGS $SOURCES'




def exists(env):
    return None
