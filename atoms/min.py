from atom import Atom
import cvxpy.expressions.types as types
from cvxpy.expressions.variable import Variable
from cvxpy.expressions.curvature import Curvature
from cvxpy.expressions.shape import Shape
from cvxpy.constraints.affine import AffEqConstraint, AffLeqConstraint
from monotonicity import Monotonicity
import cvxpy.interface.matrix_utilities as intf

class min(Atom):
    """ Maximum element in all arguments. """
    def __init__(self, *args):
        super(min, self).__init__(*args)

    # The shape is the same as the argument's shape.
    def set_shape(self):
        self._shape = Shape(1,1)

    # Default curvature.
    def base_curvature(self):
        return Curvature.CONCAVE

    def monotonicity(self):
        return len(self.args)*[Monotonicity.INCREASING]

    # Any argument size is valid.
    def validate_arguments(self):
        pass

    def graph_implementation(self, var_args):
        t = Variable()
        constraints = [AffLeqConstraint(t, x) for x in var_args]
        return (t, constraints)