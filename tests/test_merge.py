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

def test_merge_many_none():
    assert Merger().merge([ None ]) is None
    assert Merger().merge([ None, None ]) is None
    assert Merger().merge([ None, None, None ]) is None

def test_merge_object_default():
    assert Merger().merge([
        {'a': 1},
        True,
        None
    ]) == True


def test_merge_dict_default():
    assert Merger().merge([
          {'a': 1,         'c': 7},
          {'a': 2, 'b': 3        },
          {        'b': 4        },
    ]) == {'a': 2, 'b': 4, 'c': 7}

def test_merge_dict_nested_default():
    merger = Merger()
    assert merger.merge([
        {'root': {'child': {'hided': 111}}},
        {'root': {'child': 1}},
        {'root': {'child': {'none_is_skiped': 222}}},
        {'root': {'child': None}},
        {'root': {'child': {'a': 1241, 'c': 1453}}},
        {'root': {'child': {'a': 4124, 'b': 4322}}}
    ]) == {'root': {'child': {'a': 4124, 'b': 4322, 'c': 1453, 'none_is_skiped': 222}}}

def test_merge_list_default():
    assert Merger().merge([
        None,
        [1, 2, 5],
        None,
        [4, 7],
        None,
    ]) == [4, 7, 1, 2, 5]

def test_merge_list_not_connect():
    merger = Merger()
    merger.configure(list, 'last')
    assert merger.merge([
        None,
        [1, 2, 5],
        None,
        [4, 7],
        None,
    ]) == [4, 7]

def test_merge_list_configured_first():
    merger = Merger()
    merger.configure(list, 'first')
    assert merger.merge([
        None,
        [1, 2, 5],
        None,
        [4, 7],
        None,
    ]) == [1, 2, 5]
