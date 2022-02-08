def quadraticSolver(a, b, c):
    if a == 0:
        return "This Equation Is Not Quadratic"
    else:
        x1 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        return f"The roots of the quadratic equation are x = {x1} and x = {x2}"

print(quadraticSolver(1, -3, -10))