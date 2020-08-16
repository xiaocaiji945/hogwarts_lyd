#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest


@pytest.mark.last
def test_zfoo():
    assert True


@pytest.mark.second
def test_foo():
    assert True


@pytest.mark.first
def test_bar():
    assert True


@pytest.mark.second_to_last
def test_afoo():
    assert True

@pytest.mark.parametrize('a',[1,2,3,4])
def test_time_wait(a):
    sleep(3)