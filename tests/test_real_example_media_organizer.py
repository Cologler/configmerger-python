# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from configmerger import Merger

def test_multi_level_regexs():
    appconf = {
        'regexps_show': ['1', '2', '3'],
        'regexps_season': ['4', '5', '6'],
        'someotherfields': 'xxxxxx'
    }
    userconf = {
        'regexps_show': ['7', '8', '9'],
        'regexps_season': ['10', '11', '12']
    }
    assert Merger().merge([appconf, userconf]) == {
        'regexps_show': ['7', '8', '9', '1', '2', '3'],
        'regexps_season': ['10', '11', '12', '4', '5', '6'],
        'someotherfields': 'xxxxxx'
    }
