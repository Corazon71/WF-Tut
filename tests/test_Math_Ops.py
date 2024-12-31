from src.Math_Ops import CmplxSum, CmplxSub, CmplxMul, CmplxDiv

X = {'real': 2, 'imag': 9}
Y = {'real': 1, 'imag': 7}
Z = {'real': 5, 'imag': 9}
W = {'real': 8, 'imag': 3}

def test_CmplxSum():
    assert CmplxSum(X, Y) == (3, 16)
    assert CmplxSum(Z, W) == (13, 12)

def test_CmplxSub():
    assert CmplxSub(X, Y) == (1, 2)
    assert CmplxSub(Z, W) == (-3, 6)

def test_CmplxMul():
    assert CmplxMul(X, Y) == (-61, 23)
    assert CmplxMul(Z, W) == (13, 87)

def test_CmplxDiv():
    assert CmplxDiv(Y, X) == (0.77, 0.06)
    assert CmplxDiv(Z, W) == (0.92, 0.78)