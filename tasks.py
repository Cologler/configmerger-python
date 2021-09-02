# -*- coding: utf-8 -*-
#
# Copyright (c) 2021~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from invoke import task

@task
def test(c, html=False):
    cmd = 'poetry run python -m pytest --cov=configmerger --cov-report=term'
    if html:
        cmd += ' --cov-report=html'
    c.run(cmd)
