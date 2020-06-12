import ll
from ll import LinkedList, head, map, filter

def cons(head, tail):
    return tail(head, (LinkedList,), {})

def tail(lst):
    return type(lst)

ll.tail = tail
ll.cons = cons
nil = ll.nil = LinkedList("<NIL>", (LinkedList,), {})

def test():
    assert head(cons("a", nil)) == "a"
    lst = cons("a", cons("b", nil))

    print(lst)
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

    assert "aabb" == ll.foldl(lambda a, b: a + b, "", lstlst)

def test_metaclass():
    class a(LinkedList, metaclass=nil):
        pass

    class b(LinkedList, metaclass=a):
        pass

    class c(LinkedList, metaclass=b):
        pass
