# coding: utf-8


"""SCons Tool for generic GCC.
"""


import SCons


def generate(env):
    env['BUILDERS']['Object'] = SCons.Builder.Builder(
        action={
            '.c': SCons.Action.Action("$CCCOM", "$CCCOMSTR"),
        },
        emitter={},
        prefix='$OBJPREFIX',
        suffix='$OBJSUFFIX',
        single_source=1)
    env['BUILDERS']['Library'] = SCons.Builder.Builder(
        action=SCons.Action.Action("$ARCOM", "$ARCOMSTR"),
        emitter='$LIBEMITTER',
        prefix='$LIBPREFIX',
        suffix='$LIBSUFFIX',
        src_suffix='$OBJSUFFIX',
        src_builder='Object')
    env['BUILDERS']['Program'] = SCons.Builder.Builder(
        action=SCons.Action.Action("$LINKCOM", "$LINKCOMSTR"),
        emitter='$PROGEMITTER',
        prefix='$PROGPREFIX',
        suffix='$PROGSUFFIX',
        src_suffix='$OBJSUFFIX',
        src_builder='Object',
        target_scanner=SCons.Tool.ProgramScanner)
    env['CC'] = '${GCCPREFIX}gcc${GCCSUFFIX}'
    env['CFLAGS'] = SCons.Util.CLVar('')
    env['CCFLAGS'] = SCons.Util.CLVar('-std=gnu11 -pedantic -Wall -Wextra -Wno-unused-parameter -Werror')
    env['CCCOM'] = ['$CC $CCFLAGS $CFLAGS $_CPPDEFFLAGS $_CPPINCFLAGS -o $TARGET -c $SOURCE']
    env['CPPDEFPREFIX'] = '-D'
    env['CPPDEFSUFFIX'] = ''
    env['INCPREFIX'] = '-I'
    env['INCSUFFIX'] = ''
    env['OBJSUFFIX'] = '.o'

    env['AS'] = '${GCCPREFIX}gcc${GCCSUFFIX}'
    env['ASCOM'] = '$AS $CCFLAGS $ASFLAGS -o $TARGET -c $SOURCES'

    env['LINK'] = '${GCCPREFIX}gcc${GCCSUFFIX}'
    env['LINKFLAGS'] = SCons.Util.CLVar('')
    env['LINKERSCRIPT'] = SCons.Util.CLVar('')
    env['_MAPFILE'] = ('MAPFILE' in env) and '-Xlinker -Map -Xlinker ${TARGET.base}.map' or ''
    env['_LINKFILE'] = '${LINKERSCRIPT and ("-T%s" % LINKERSCRIPT) or ""}'
    env['_LINKARGS'] = '$CCFLAGS $LINKFLAGS $_LINKFILE $_MAPFILE -o $TARGET $SOURCES $_LIBDIRFLAGS $_LIBFLAGS'
    env['LINKCOM'] = '$LINK $_LINKARGS'
    env['LIBDIRPREFIX'] = '-L'
    env['LIBDIRSUFFIX'] = ''
    env['LIBLINKPREFIX'] = '-l'
    env['LIBLINKSUFFIX'] = ''

    env['AR'] = '${GCCPREFIX}ar${GCCSUFFIX}'
    env['ARFLAGS'] = SCons.Util.CLVar('')
    env['ARCOM'] = '$AR $ARFLAGS rc $TARGET $SOURCES'
    env['LIBPREFIX'] = 'lib'
    env['LIBSUFFIX'] = '.a'

    env['BUILDERS']['Rom'] = env.Builder(
        action=SCons.Action.Action("$ROMCOM"),
        suffix='$ROMSUFFIX',
        single_source=1)

def exists(env):
    return None
