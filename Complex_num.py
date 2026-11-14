class Complex:

    def __init__(self, real: float, imag: float):
        self.real = float(real)
        self.imag = float(imag)

    def __str__(self) -> str:
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real:g} {sign} {abs(self.imag):g}i"
