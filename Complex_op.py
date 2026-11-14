from Complex_num import Complex

def add(a: Complex, b: Complex) -> Complex:
    return Complex(a.real + b.real, a.imag + b.imag)

def subtract(a: Complex, b: Complex) -> Complex:
    return Complex(a.real - b.real, a.imag - b.imag)

def multiply(a: Complex, b: Complex) -> Complex:
    real = a.real * b.real - a.imag * b.imag
    imag = a.real * b.imag - a.imag * b.real
    return Complex(real, imag)

def divide(a: Complex, b: Complex) -> Complex:
    denominator = b.real ** 2 + b.imag ** 2

    if denominator == 0:
        raise ZeroDivisionError("Can't divide by a complex number equal to 0 + 0i.")

    real = (a.real * b.real + a.imag * b.imag) / denominator
    imag = (a.imag * b.real - a.real * b.imag) / denominator
    return Complex(real, imag)