from ll import *

test_list = cons("a", cons("b", nil))

def test_basic():
    assert head(test_list) == "a"
    assert head(tail(test_list)) == "b"

def test_length():
    assert len(nil) == 0
    assert len(test_list) == 2

def test_iter():
    assert list(test_list) == ["a", "b"]
    assert "b" in test_list

def test_map():
    lstlst = map(lambda x: x * 2, test_list)
    assert len(lstlst) == 2
    assert list(lstlst) == ["aa", "bb"]

def test_filter():
    x = filter(lambda x: x.startswith('b'), test_list)
    assert list(x) == ['b']

def test_foldl():
    assert foldl(lambda a, b: a + b, "", test_list) == "ab"

def test_repr():
    assert repr(nil) == "()"
    assert repr(test_list) == "('a' 'b')"

def test_from_iter():
    assert LinkedList.from_iter(["a", "b"]) == test_list

def test_class():
    class c(test_list):
        pass

    assert tail(c) == test_list
    assert head(c) == 'c'
    assert len(c) == 3
