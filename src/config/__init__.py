#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import importlib

def get_config(env):
    if not env:
        env = "local"
    return importlib.import_module(__name__ + ".%s" % env).Config
    