"""
  Convenience wrappers to provide a better interface to python's built-in linked list type.

  (FIXME: linked lists in python only support string values for some reason.)
"""
import json

def cons(head, tail):
    return LinkedList(head, (tail,), {})


def head(lst):
    return json.loads(lst.__name__)


def tail(lst):
    return lst.__base__


class LinkedList(type):
    def __new__(mcl, name, bases, namespace):
        return super().__new__(mcl, json.dumps(name), bases, namespace)

    def __repr__(cls):
        return "(" + " ".join(cls) + ")"

    def __iter__(cls):
        ptr = cls
        while ptr is not nil:
            yield head(ptr)
            ptr = tail(ptr)

    @classmethod
    def from_iter(cls, lst):
        result = nil
        for item in reversed(lst):
            result = cons(item, result)
        return result

    def __len__(cls):
        if cls is nil:
            return 0
        return 1 + len(tail(cls))

    def __eq__(cls, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        if cls is nil:
            return other is nil
        return head(cls) == head(other) and tail(cls) == tail(other)


nil = LinkedList("<NIL>", (), {})


def map(f, lst):
    if lst is nil:
        return nil

    return cons(
        f(head(lst)),
        map(f, tail(lst)))


def filter(f, lst):
    if lst is nil:
        return nil

    if f(head(lst)):
        return cons(head(lst), filter(f, tail(lst)))
    return filter(f, tail(lst))


def foldl(f, acc, lst):
    if lst is nil:
        return acc
    return foldl(f, f(acc, head(lst)), tail(lst))


def test():
    assert head(cons("a", nil)) == "a"
    lst = cons("a", cons("b", nil))

    assert len(nil) == 0
    assert len(lst) == 2

    lstlst = map(lambda x: x * 2, lst)
    assert head(lstlst) == "aa"

    assert list(lstlst) == ["aa", "bb"]

    assert "bb" in lstlst

    assert "(a b)" == repr(lst)

    assert nil == nil
    assert LinkedList.from_iter(["aa", "bb"]) == lstlst

    assert LinkedList.from_iter(["aa"]) == filter(lambda x: x.startswith("a"), lstlst)
    assert nil == filter(lambda x: x.startswith("c"), lstlst)

    assert "aabb" == foldl(lambda a, b: a + b, "", lstlst)


def test_class():
    class c(nil):
        pass

    class b(c):
        pass

    class a(b):
        pass

    assert tail(a) == b
    assert tail(tail(a)) == c
    assert len(a) == 3

if __name__ == "__main__":
    test()
