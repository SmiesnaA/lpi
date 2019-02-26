#!/usr/bin/env python3
import itertools
from typing import List, Mapping, MutableMapping, Sequence, Iterable, FrozenSet
import re
import sys

spyTheoryProblem = {'ls': ['RS', 'NS', 'SS', 'RM', 'NM', 'SM', 'RE', 'NE', 'SE'],
 'ts': ['Každý je buď Rus alebo Nemec', 'Práve jeden je Rus, ostatní dvaja sú nemci', 'Každý Rus musí byť špión', 'Stirlitz: „Müller, ty si taký Nemec, ako som ja Rus“', 'Celá teória'],
 'cs': ['impl', 'impl', 'impl', 'impl', 'eq'],
 'vs': [[False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [True, False, True, False, False],
 [True, False, True, False, False],
 [True, True, False, False, False],
 [True, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [True, False, True, False, False],
 [True, False, True, False, False],
 [True, True, False, False, False],
 [True, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [True, True, False, True, False],
 [True, True, False, True, False],
 [True, False, False, True, False],
 [True, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [True, True, True, True, True],
 [True, True, True, True, True],
 [True, False, False, True, False],
 [True, False, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, True, True, False, False],
 [False, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [True, False, True, False, False],
 [True, False, True, False, False],
 [True, True, False, False, False],
 [True, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [True, False, True, False, False],
 [True, False, True, False, False],
 [True, True, False, False, False],
 [True, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [True, True, False, True, False],
 [True, True, False, True, False],
 [True, False, False, True, False],
 [True, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [True, True, True, True, True],
 [True, True, True, True, True],
 [True, False, False, True, False],
 [True, False, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, True, True, False, False],
 [False, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [True, True, False, True, False],
 [True, True, False, True, False],
 [True, False, False, True, False],
 [True, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [True, True, False, True, False],
 [True, True, False, True, False],
 [True, False, False, True, False],
 [True, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [True, True, True, True, True],
 [True, True, True, True, True],
 [True, False, False, True, False],
 [True, False, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [True, True, True, True, True],
 [True, True, True, True, True],
 [True, False, False, True, False],
 [True, False, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [True, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [True, False, True, False, False],
 [True, False, True, False, False],
 [True, False, False, False, False],
 [True, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, True, True, True, False],
 [False, True, True, True, False],
 [False, False, False, True, False],
 [False, False, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, True, True, True, False],
 [False, True, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, True, True, True, False],
 [False, True, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, False, False, False],
 [False, False, False, False, False],
 [False, True, False, False, False],
 [False, True, False, False, False],
 [False, False, True, False, False],
 [False, False, True, False, False],
 [False, True, True, False, False],
 [False, True, True, False, False],
 [False, False, False, False, False],
 [False, False, True, False, False],
 [False, True, False, False, False],
 [False, True, True, False, False],
 [False, False, False, True, False],
 [False, False, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, True, False, True, False],
 [False, False, True, True, False],
 [False, False, True, True, False],
 [False, True, True, True, False],
 [False, True, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False],
 [False, True, False, True, False],
 [False, True, True, True, False]]}
spyGoalProblem = {'ls': ['RS', 'NS', 'SS', 'RM', 'NM', 'SM', 'RE', 'NE', 'SE'],
 'ts': ['Negácia „Eismann nie je ruský špión“'],
 'cs': ['eq'],
 'vs': [[False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True],
 [False],
 [False],
 [False],
 [False],
 [False],
 [True],
 [False],
 [True]]}


Clause = FrozenSet[str]
Interpretation = FrozenSet[str]
Theory = Iterable[FrozenSet[str]]


def parseClause(s : str) -> Clause: return frozenset(s.split())
def parseClauses(ss : Iterable[str]) -> Theory: return (parseClause(s) for s in ss)
def parseTheory(s: str) -> Theory:
  return [
    parseClause(l)
      for l in s.replace('¬', ' -').replace('∨', ' ').split('\n')
        if (not re.match(r'^\s*$',l) and not re.match(r'^\s*c',l))
  ]
def theoryLiterals(cls : Theory) -> FrozenSet[str]: return frozenset().union(*cls)
def unknownLiterals(c : Clause, problem) -> List[str]:
  knownLiterals = frozenset(problem['ls'])
  lits = frozenset((l[1:] if l[0] == '-' else l) for l in c)
  return list(lits - knownLiterals)
def satisfiesClause(i:Interpretation, c: Clause) -> bool: return bool(i&c)
def satisfies(i:Interpretation, t : Theory) -> bool : return all(satisfiesClause(i, c) for c in t)
def satisfiesCheck(sat : bool, expected : bool, check : str):
  if check == 'impl': return  (not sat) or expected
  elif check == 'eq': return sat == expected
  else: raise NotImplementedError('check not supported: "%s"' % check)

def interpretations(ls : Iterable[str]):
  return [frozenset(x) for x in itertools.product(*(['-'+l,l] for l in ls))]



##
# Check that all parts of theory are implied by the given theory.
#
# @param problem the problem description to check against
# @param t theory to check
#
# @returns list of results for each sub-theory: the first interpretation that
# fails, or true if the theory passes the check
#
def checkTheory(problem, t : Theory):
  fails = [[] for t in problem['ts']]
  satisfiable = False
  for ii, interpretation in enumerate(interpretations(problem['ls'])):
    satisfied = satisfies(interpretation, t)
    satisfiable = satisfiable or satisfied
    for ti, f in enumerate(fails):
      if not f:
        if not satisfiesCheck(satisfied, problem['vs'][ii][ti], problem['cs'][ti]):
#          print('== sat %s exp %s   i %s     t %s' % (repr(satisfied), repr(problem['vs'][ii][ti]), repr(interpretation), repr(list(t))))
          f.append(interpretation)
  return (satisfiable, [(f[0] if f else True) for f in fails])

def readFile(name : str) -> str:
  with open(name, 'r') as f:
    return f.read()
def readTheory(name : str) -> Theory: return parseTheory(readFile(name))


def formatInterpretation(i : Interpretation) -> str:
  # [...i].map(l => (l[0] === '-' ? l.slice(1) : l) + '↦' + (l[0] === '-' ? 'f' : 't')).join(',')
  return '{ ' + ', '.join((l[1:] if l[0] == '-' else l) + '↦' + ('f' if l[0] == '-' else 't') for l in i) + ' }'

def printColor(s : str, ansi : str, idle : str) -> None:
  try: sys.stdout.shell.write(s, idle) # IDLE hack ;)
  except AttributeError: sys.stdout.write('%s%s%s' % (ansi, s, '\033[0m'))

def printGreen(s : str) -> None: printColor(s, '\033[32m', 'STRING')
def printRed(s : str) -> None: printColor(s, '\033[31m', 'COMMENT')
# ✕ ✖ ❌
def printPass() -> None: printGreen('✓')
def printFail() -> None: printRed('✕')

def printResult(problem, res, errorUnsat):
  ret = True
  sat, fails = res
  if errorUnsat and not sat:
    printFail()
    print("  teória je nesplniteľná")
    return False

  for name, f, check in zip(problem['ts'], fails, problem['cs']):
    ok = f == True # type: bool
    ret = ret and ok
    printStatus = printPass if ok else printFail
    printStatus()
    print(' %s' % (name,))
    if f != True:
      if check == 'eq':
        print("    Nezhoduje sa pre ohodnotenie")
      else:
        print("    Nie je splnené v ohodnotení")
      print("      %s" % (formatInterpretation(f)))
    print()

  return ret

def testTheory(problem, fileName, errorUnsat = True):
  print('Testing %s' % (fileName,))
  print()
  try:
    t = readTheory(fileName)
    unknownLits = unknownLiterals(theoryLiterals(t), problem)
    if unknownLits:
      printFail()
      print('  Neznáme literály: %s' % ', '.join(unknownLits))
      return
    res = checkTheory(problem, t)
    return printResult(problem, res, errorUnsat)
  except FileNotFoundError:
    printFail()
    print(' %s not found' % (fileName))
    return False

print()
okT = testTheory(spyTheoryProblem, 'spyTheory.txt')
print()
print()
okG = testTheory(spyGoalProblem, 'spyGoal.txt', errorUnsat = False)
print()

if not (okT and okG):
  sys.exit(1)
