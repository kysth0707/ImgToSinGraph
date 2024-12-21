from sympy import latex
from sympy import sympify
from sympy.parsing.latex import parse_latex
from pyperclip import copy

target = input("입력ㄱㄱㄱ")
print(target)

def LatexToMath(expr):
    # Input a string written in latex format. Have the math format copied to clipboard
    return copy(str(parse_latex(expr)))
def MathToLatex(expr):
    # Input a string written in regular math format. Have the corresponding latex format copied to clipboard
    return copy(latex(sympify(expr, evaluate=False)))

LatexToMath(target)