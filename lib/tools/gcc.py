# coding: utf-8


"""SCons Tool for generic GCC.
"""
import SCons
def generate(env):
    # print('GCC GENERATE')
    env['BUILDERS']['Object'] = SCons.Builder.Builder(
        action={
            '.c': SCons.Action.Action("$CCCOM", "$CCCOMSTR"),
            '.cpp': SCons.Action.Action("$CXXCOM", "$CXXCOMMSTR"),
            '.S': SCons.Action.Action("$ASCOM", "$ASCOMSTR"),
        },
        emitter={},
        prefix='$OBJPREFIX',
        suffix='$OBJSUFFIX',
        source_scanner=SCons.Tool.SourceFileScanner,
        single_source=1)
    env['BUILDERS']['Library'] = SCons.Builder.Builder(
        action= [SCons.Action.Action("$ARCOM", "$ARCOMSTR"),
                SCons.Action.Action("$RANLIB", "$RANLIBSTR")],
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
    env['CCCOM'] = ['$CC $CCFLAGS $CFLAGS $_CPPDEFFLAGS $_CPPINCFLAGS -o $TARGET -c $SOURCE']
    env['CPPDEFPREFIX'] = '-D'
    env['CPPDEFSUFFIX'] = ''
    env['INCPREFIX'] = '-I'
    env['INCSUFFIX'] = ''
    env['OBJSUFFIX'] = '.o'

    env['CXX'] = '${GPPPREFIX}g++${GPPSUFFIX}'
    env['CXXCOM']     = '$CXX -o $TARGET -c $CXXFLAGS $_CPPDEFFLAGS $_CPPINCFLAGS $SOURCES'


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
    env['ARCOM'] = '$AR $ARFLAGS rcs $TARGET $SOURCES'
    env['LIBPREFIX'] = 'lib'
    env['LIBSUFFIX'] = '.a'

    env['RANLIB'] = '${GPPPREFIX}ranlib${GPPSUFFIX} $TARGET'

    env['BUILDERS']['Rom'] = SCons.Builder.Builder(
        action=SCons.Action.Action("$ROMCOM"),
        suffix='$ROMSUFFIX',
        single_source=1)

def exists(env):
    return None
