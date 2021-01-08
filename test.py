import numpy as np
from bfloat16 import bfloat16
a1 = np.full([4], 2.45, dtype=bfloat16)
a2 = np.arange(4, dtype=bfloat16)
np.dot(a1, a2)
