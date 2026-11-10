#! usr/bin/env python3

from word_count import word_count


def test_basic():
    assert word_count("a b a") == {"a": 2, "b": 1}


def test_case_insensitive():
    assert word_count("Hi hi HI") == {"hi": 3}


def test_punctuation():
    assert word_count("Hello, world! Hello.") == {"hello": 2, "world": 1}


def test_empty():
    assert word_count("") == {}
