#!/usr/bin/env python
#! coding: utf-8

import os
import sys
import platform
import subprocess
from distutils.core import setup, Extension

# avoid building universal binary (ppc) on osx non-ppc platforms
if sys.platform == 'darwin':
    arch = platform.machine()
    if arch in ('i386', 'x86_64'):
        os.environ['ARCHFLAGS'] = '-arch i386 -arch x86_64'

extra_compile_args = ['-g', '-fPIC', '-Wall', '-O2']

VERSION = '0.1.5'

if not os.path.exists('smhasher/src'):
    sys.stderr.write('run command:\ngit submodule update --init\n')
    p = subprocess.Popen(args=['git', 'submodule', 'update', '--init'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outs, errs = p.communicate()
    p.wait()
    sys.stderr.write(outs)
    sys.stderr.write(errs)

here = os.path.abspath(os.path.dirname(__file__))

readme_path = os.path.join(here, 'README.md')
try:
    import pypandoc
    long_description = pypandoc.convert(readme_path, 'rst')
except (IOError, ImportError):
    long_description = open(readme_path).read()

cpp_files = [
    'smhasher/src/MurmurHash2.cpp',
    'smhasher/src/MurmurHash3.cpp',
    'pysmhasher.cpp'
]

pysmhasher_ext = Extension(
    'pysmhasher',
    sources=cpp_files,
    include_dirs=['smhasher/src'],
    define_macros=[('MODULE_VERSION', '"{}"'.format(VERSION))],
    extra_compile_args=extra_compile_args
)

setup(
    name='pysmhasher',
    version=VERSION,
    author='Yong Li',
    author_email='liyong19861014@gmail.com',
    url='https://github.com/airhuman/pysmhasher.git',
    description='Python Extensions for SMHasher',
    long_description=long_description,
    keywords='hash hashing smhasher',
    license='MIT',
    ext_modules=[pysmhasher_ext],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
