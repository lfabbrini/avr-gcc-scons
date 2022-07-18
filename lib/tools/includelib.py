"""Tool SCons to include SConscript inside lib/.

"""
import os

def generate(env):
    env.AddMethod(IncludeLibrary)


def exists(env):
    return None


def IncludeLibrary(self, *dirs, **options):
    self.SetDefault(_LIBINCLUDED=set())
    variant_dir = options.get('variant_dir',None)
    self.SetDefault(LIBROOT=self.Dir('%s/lib'%variant_dir))
    self.VariantDir('%s/lib'%variant_dir, '#lib', duplicate=0)
    for lib in dirs:
        libpath = self['LIBROOT'].Dir(lib)
        if libpath not in self['_LIBINCLUDED']:
            self['_LIBINCLUDED'].add(self.Dir(libpath))
            # print(map(str,self['_LIBINCLUDED']))
            self.SConscript(dirs=[libpath], exports={ 'env': self, 'options': options })
