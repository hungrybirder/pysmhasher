#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import pysmhasher

key = 'abc'

print('murmurhash2, key={0}, hv={1}'.format(key, pysmhasher.murmurhash2(key)))
print('murmurhash2A, key={0}, hv={1}'.format(key, pysmhasher.murmurhash2A(key)))
print('murmurhash64A, key={0}, hv={1}'.format(key, pysmhasher.murmurhash64A(key)))
print('murmurhash64B, key={0}, hv={1}'.format(key, pysmhasher.murmurhash64B(key)))
print('murmurhash3_x86_32, key={0}, hv={1}'.format(key, pysmhasher.murmurhash3_x86_32(key)))


if platform.architecture()[0] == '64bit':
    print('murmurhash3_x64_128, key={0}, hv={1}'.format(key, pysmhasher.murmurhash3_x64_128(key)))
else:
    print('murmurhash3_x86_128, key={0}, hv={1}'.format(key, pysmhasher.murmurhash3_x86_128(key)))

