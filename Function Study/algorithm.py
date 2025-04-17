import time
import os

from sympy import symbols, simplify, limit, diff, S, oo, solveset, Interval
from sympy.calculus.util import continuous_domain
from sympy.plotting import plot
from sympy.functions import *
from sympy import symbols, Eq, solve
from sympy import solveset

class FunctionStudy():

    def __init__(self, expression, variable):
        
        self.expression = expression
        self.variable = variable

    def __str__(self):
        
        print(f"Selected function: ${self.expression}$")

    def get_domain(self):

        dom = continuous_domain(self.expression, self.variable, S.Reals)
        return dom
    
    def get_sign(self):

        x_intersection = Eq(self.expression, 0)

        positivity_diseq = self.expression > 0
        pos_interval = solveset(positivity_diseq, self.variable, FunctionStudy.get_domain())

        negativity_diseq = self.expression < 0
        neg_interval = solveset(positivity_diseq, self.variable, FunctionStudy.get_domain())
        