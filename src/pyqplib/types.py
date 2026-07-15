from enum import Enum, auto


class Sense(Enum):
    MINIMIZE = auto()
    MAXIMIZE = auto()


class ProblemVarType(Enum):
    CONTINUOUS = auto()
    BINARY = auto()
    MIXED_BINARY = auto()
    INTEGER = auto()
    GENERAL = auto()


class VarType(Enum):
    CONTINUOUS = auto()
    BINARY = auto()
    INTEGER = auto()


class ProblemObjType(Enum):
    LINEAR = auto()
    CONVEX_SYMM = auto()
    CONVEX = auto()
    GENERAL = auto()

    @property
    def convex(self):
        return self in [
            ProblemObjType.LINEAR,
            ProblemObjType.CONVEX_SYMM,
            ProblemObjType.SYMM,
        ]


class ProblemConsType(Enum):
    UNCONSTRAINED = auto()
    BOXED = auto()
    LINEAR = auto()
    CONVEX = auto()
    CONVEX_SYMM = auto()
    GENERAL = auto()
