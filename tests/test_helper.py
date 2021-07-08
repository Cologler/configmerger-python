# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from configmerger import Merger

def test_trim_none_from_end():
    assert Merger._trim_none_from_end([1, 2, 3]) == [1, 2, 3]
    assert Merger._trim_none_from_end([1, 2, None]) == [1, 2]
    assert Merger._trim_none_from_end([1, None, None]) == [1]
    assert Merger._trim_none_from_end([None, None, None]) == []

    assert Merger._trim_none_from_end([None, 1, 2, 3]) == [None, 1, 2, 3]
    assert Merger._trim_none_from_end([None, 1, 2, None]) == [None, 1, 2]
    assert Merger._trim_none_from_end([None, 1, None, None]) == [None, 1]
    assert Merger._trim_none_from_end([None, None, None, None]) == []

    assert Merger._trim_none_from_end([1, None, 2, 3]) == [1, None, 2, 3]
    assert Merger._trim_none_from_end([1, None, 2, None]) == [1, None, 2]
    assert Merger._trim_none_from_end([1, None, None, None]) == [1]
    assert Merger._trim_none_from_end([None, None, None, None]) == []
