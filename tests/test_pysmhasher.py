#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member

import pysmhasher


def test_murmurhash2():
    key = 'abc'
    assert pysmhasher.murmurhash2(key) == 324500635

def test_cityhash64():
    key = 'DBE4CBA7-2ADC-4F32-8D54-D8F065FED9CC'
    assert pysmhasher.cityhash64(key) == 6587470800993669582
