import numpy as np
def test( got, expected):

    eq = False
    if type(expected) == type(got) == type(np.array([])):
       eq = np.allclose(expected,got)
    else:
       eq = expected==got

    if eq:
        print "test ok"
        return 1
    else:
        print "test not ok: got", got, "expected", expected
        return 0

