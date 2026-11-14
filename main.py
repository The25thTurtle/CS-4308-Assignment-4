from Complex_num import Complex
from Complex_op import add, subtract, multiply, divide

def read_input(filename: str):
    with open(filename, "r", encoding="utf-8") as input_file:
        values = []
        for line_number, line in enumerate(input_file, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split()
            if len(parts) != 2:
                raise ValueError(
                    f"Line {line_number} must contain exactly two numbers: real imag"
                )
            values.append((float(parts[0]), float(parts[1])))

        if len(values) != 2:
            raise ValueError("input.txt must contain exactly two complex numbers.")

        return Complex(*values[0]), Complex(*values[1])

    def run():
        first, second = read_input("input.txt")

        results = [
            f"First complex number: {first}",
            f"Second complex number: {second}",
            "",
            f"Addition: {add(first, second)}",
            f"Substraction: {subtract(first, second)}",
            f"Multiplication: {multiply(first, second)}",
        ]

        try:
            results.append(f"Division:  {divide(first, second)}")
        except ZeroDivisionError as error:
            results.append(f"Division:  Error - {error}")

        output = "\n".join(results)
        print(output)

        with open("output.txt", "w", encoding="utf-8") as output_file:
            output_file.write(output + "\n")

    if __name__ == "__main__":
        run()