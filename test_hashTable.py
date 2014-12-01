#!usr/bin/python
import pytest
from hashTable import HashTable


table = HashTable(1024)

with open('/usr/share/dict/words') as f:
    word = " "
    while word != "":
        word = f.readline()
        table.set(word, word)


def test_hashtable():
    with open('/usr/share/dict/words') as f:
        word = " "
        while word != "":
            word = f.readline()
            assert table.get(word) == word

    try:
        table.set(42, 'Python')
    except TypeError:
        assert True
    else:
        assert False

    try:
        table.get('arglebargle')
    except KeyError:
        assert True
    else:
        assert False
