# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import pytest

from configmerger import Merger

def test_merge_nothing():
    with pytest.raises(ValueError):
        assert Merger().merge([])

def test_merge_dict():
    assert Merger().merge([
        {'a': 1},
        {'a': 2, 'b': 3},
        {'b': 4}
    ]) == {'a': 2, 'b': 4}

def test_merge_nested_dict():
    assert Merger().merge([
        {'root': {'child': {'hided': 111}}},
        {'root': {'child': 1}},
        {'root': {'child': {'none_is_skiped': 222}}},
        {'root': {'child': None}},
        {'root': {'child': {'a': 1241, 'c': 1453}}},
        {'root': {'child': {'a': 4124, 'b': 4322}}}
    ]) == {'root': {'child': {'a': 4124, 'b': 4322, 'c': 1453, 'none_is_skiped': 222}}}

def test_merge_list():
    assert Merger().merge([
        [1, 2, 5],
        None,
        [4, 7]
    ]) == [4, 7, 1, 2, 5]

def test_merge_list_without_connect():
    merger = Merger()
    merger.connect_list = False
    assert merger.merge([
        [1, 2, 5],
        None,
        [4, 7]
    ]) == [4, 7]

def test_merge_object():
    assert Merger().merge([
        {'a': 1},
        True,
        None
    ]) == True

def test_merge_all_none():
    assert Merger().merge([ None ]) == None
    assert Merger().merge([ None, None ]) == None
    assert Merger().merge([ None, None, None ]) == None

def test_merge_stop_when_type_changed():
    assert Merger().merge([
        {'a': 1},
        1,
        {'b': 2},
        None,
        {'c': 3},
    ]) == {'b': 2, 'c': 3}
