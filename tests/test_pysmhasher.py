#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-member

import pysmhasher


def test_murmurhash2():
    key = 'abc'
    assert pysmhasher.murmurhash2(key) == 324500635
