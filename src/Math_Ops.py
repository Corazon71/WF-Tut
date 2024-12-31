def CmplxSum(a, b):
    return (a['real'] + b['real'], a['imag'] + b['imag'])

def CmplxDiff(a, b):
    return (a['real'] - b['real'], a['imag'] - b['imag'])

def CmplxProd(a, b):
    return (a['real'] * b['real'] - a['imag'] * b['imag'], a['real'] * b['imag'] + a['imag'] * b['real'])

def CmplxQuot(a, b):
    def round_up(value, decimals):
        factor = 10 ** decimals
        return ((value * factor) + 0.5) // 1 / factor

    den = b['real']**2 + b['imag']**2
    real_part = (a['real'] * b['real'] + a['imag'] * b['imag']) / den
    imag_part = (a['imag'] * b['real'] - a['real'] * b['imag']) / den

    return round_up(real_part, 2), round_up(imag_part, 2)
