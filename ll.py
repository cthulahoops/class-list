"""
  Convenience wrappers to provide a better interface to python's built-in linked list type.

  (FIXME: linked lists in python only support string values for some reason.)
"""


def cons(head, tail):
    return LinkedList(head, (tail,), {})


def car(lst):
    return lst.__name__


def cdr(lst):
    return lst.__base__


class LinkedList(type):
    def __repr__(self):
        return "(" + " ".join(self) + ")"

    def __iter__(self):
        ptr = self
        while ptr is not nil:
            yield car(ptr)
            ptr = cdr(ptr)

    @classmethod
    def from_iter(cls, lst):
        result = nil
        for item in lst[::-1]:
            result = cons(item, result)
        return result

    def __len__(self):
        if self is nil:
            return 0
        return 1 + len(cdr(self))

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return NotImplemented
        if self is nil:
            return other is nil
        return car(self) == car(other) and cdr(self) == cdr(other)


nil = LinkedList("<NIL>", (), {})


def map(f, lst):
    if lst is nil:
        return nil

    return cons(f(car(lst)), map(f, cdr(lst)))


def filter(f, lst):
    if lst is nil:
        return nil

    if f(car(lst)):
        return cons(car(lst), filter(f, cdr(lst)))
    return filter(f, cdr(lst))


def foldl(f, acc, lst):
    if lst is nil:
        return acc
    return foldl(f, f(acc, car(lst)), cdr(lst))


def tails(lst):
    return lst.mro()[:-1]


def test():
    assert car(cons("a", nil)) == "a"
    lst = cons("a", cons("b", nil))

    assert len(nil) == 0
    assert len(lst) == 2

    lstlst = map(lambda x: x * 2, lst)
    assert car(lstlst) == "aa"

    assert list(lstlst) == ["aa", "bb"]

    assert "bb" in lstlst

    assert "[(aa bb), (bb), ()]" == repr(tails(lstlst))

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

    assert cdr(a) == b
    assert cdr(cdr(a)) == c
    assert len(a) == 3

if __name__ == "__main__":
    test()
