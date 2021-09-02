# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from configmerger import trim_none_from_end, get_typed_values_from_end

def test_trim_none_from_end():
    assert trim_none_from_end([1, 2, 3]) == [1, 2, 3]
    assert trim_none_from_end([1, 2, None]) == [1, 2]
    assert trim_none_from_end([1, None, None]) == [1]
    assert trim_none_from_end([None, None, None]) == []

    assert trim_none_from_end([None, 1, 2, 3]) == [None, 1, 2, 3]
    assert trim_none_from_end([None, 1, 2, None]) == [None, 1, 2]
    assert trim_none_from_end([None, 1, None, None]) == [None, 1]
    assert trim_none_from_end([None, None, None, None]) == []

    assert trim_none_from_end([1, None, 2, 3]) == [1, None, 2, 3]
    assert trim_none_from_end([1, None, 2, None]) == [1, None, 2]
    assert trim_none_from_end([1, None, None, None]) == [1]
    assert trim_none_from_end([None, None, None, None]) == []

def test_get_typed_values_from_end():
    assert get_typed_values_from_end([1, 2, 3], int) == [1, 2, 3]
    assert get_typed_values_from_end([1, 2, 3], str) == []
    assert get_typed_values_from_end([None, 1, None, 2, None, 3, None], int) == [1, 2, 3]
    assert get_typed_values_from_end(['df', 3, 't4', 'sd'], str) == ['t4', 'sd']
