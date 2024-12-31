from src.Math_Ops import CmplxSum, CmplxDiff, CmplxProd, CmplxQuot

# Test data
X = {'real': 2, 'imag': 9}
Y = {'real': 1, 'imag': 7}
Z = {'real': 5, 'imag': 9}
W = {'real': 8, 'imag': 3}

def test_CmplxSum():
    """Test the addition of complex numbers."""
    assert CmplxSum(X, Y) == {'real': 3, 'imag': 16}
    assert CmplxSum(Z, W) == {'real': 13, 'imag': 12}

def test_CmplxDiff():
    """Test the subtraction of complex numbers."""
    assert CmplxDiff(X, Y) == {'real': 1, 'imag': 2}
    assert CmplxDiff(Z, W) == {'real': -3, 'imag': 6}

def test_CmplxProd():
    """Test the multiplication of complex numbers."""
    assert CmplxProd(X, Y) == {'real': -61, 'imag': 23}
    assert CmplxProd(Z, W) == {'real': 13, 'imag': 87}

def test_CmplxQuot():
    """Test the division of complex numbers."""
    assert CmplxQuot(Y, X) == {'real': 0.76, 'imag': 0.06}
    assert CmplxQuot(Z, W) == {'real': 0.92, 'imag': 0.78}
