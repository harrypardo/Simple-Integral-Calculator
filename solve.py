import math

special_math = ['cos', 'sin', 'tan', 'log', 'pi', 'e', 'cosh', 'sinh', 'tanh', 'acosh', 'asinh', 'atanh', 'acos',
                'atan', 'asin', 'sqrt']

def evalEquation(equation, x):
    equation = equation.replace('^', '**')
    for sp in special_math:
        equation = equation.replace(sp, 'math.' + sp)
    equation = equation.replace('math.math.', 'math.')
    return eval(equation)

def integrate(equation, lowerbound, upperbound, n):
    deltaX = (upperbound - lowerbound) / n

    f_values = [lowerbound]
    a = lowerbound
    for i in range(0, n):
        f_values.append(a + deltaX)
        a += deltaX

    mid_points = []
    for i in range(0, len(f_values) - 1):
        mid_points.append((f_values[i] + f_values[i + 1]) / 2)
    m_sum = 0
    for m in mid_points:
        m_sum += evalEquation(equation, m)

    return m_sum * deltaX

