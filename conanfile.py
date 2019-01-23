#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostDisjoint_SetsConan(base.BoostBaseConan):
    name = "boost_disjoint_sets"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_disjoint_sets"
    lib_short_names = ["disjoint_sets"]
    header_only_libs = ["disjoint_sets"]
    cycle_group = "boost_level14group"
    b2_requires = [
        "boost_level14group",
    ]


    