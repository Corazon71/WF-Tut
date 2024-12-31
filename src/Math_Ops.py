def CmplxSum(a, b):
    """Returns the sum of two complex numbers."""
    return {'real': a['real'] + b['real'], 'imag': a['imag'] + b['imag']}

def CmplxDiff(a, b):
    """Returns the difference of two complex numbers."""
    return {'real': a['real'] - b['real'], 'imag': a['imag'] - b['imag']}

def CmplxProd(a, b):
    """Returns the product of two complex numbers."""
    return {
        'real': a['real'] * b['real'] - a['imag'] * b['imag'],
        'imag': a['real'] * b['imag'] + a['imag'] * b['real']
    }

def CmplxQuot(a, b):
    """Returns the quotient of two complex numbers."""
    den = b['real']**2 + b['imag']**2
    real_part = (a['real'] * b['real'] + a['imag'] * b['imag']) / den
    imag_part = (a['imag'] * b['real'] - a['real'] * b['imag']) / den
    return {'real': round(real_part, 2), 'imag': round(imag_part, 2)}
