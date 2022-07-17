import os
import sys


env = Environment(
    ENV=os.environ,
    tools = ['includelib'],
    toolpath=[Dir('lib/tools')],
    )

Export('env') # Export adds one or more variables to a global list of variables that are available for import by other SConscript files.
VariantDir('build', '.', duplicate=0) # VariantDir function to establish that target files should be built in a separate directory from the source files. You can specify the same duplicate=0 argument n which case SCons will disable duplication of the source files (otherwise SCons copy all files on build/)
# CacheDir(os.environ.get('SCONS_CACHEDIR'))

SConscript(dirs=[
    # 'build/appl/nanoevery/helloworld',
    # 'build/appl/uno/helloworld',
    'build/dbg/helloworld',
    'build/appl/uno/blink',
])

Default('build') #default target built if scons is launched without one
