import numpy as np
from bfloat16 import bfloat16

def test_creation():
    a0 = bfloat16(2.45)
    assert a0 == 2.45
    a1 = np.full([4], 2.45, dtype=bfloat16)
    assert a1 is not None and a1.dtype == bfloat16 and np.all(a1 == bfloat16(2.45))
    a2 = np.arange(4, dtype=bfloat16)
    np.dot(a1, a2)

def test_dot():
    a1 = np.full([4], 2.45, dtype=bfloat16)
    a2 = np.arange(4, dtype=bfloat16)
    np.dot(a1, a2)

def test_calc():
    a1 = np.full([4], 2.45, dtype=bfloat16)
    assert np.max(a1) == np.array(2.45, dtype=bfloat16)
    a2 = np.arange(4, dtype=bfloat16)
    assert np.max(a2) == np.array(3.0, dtype=bfloat16)
    r = a1 + a2
    assert np.array_equal(r, np.array([2.453125, 3.453125, 4.437500, 5.437500], dtype=bfloat16))
    ok = False
    try:
        r = a1 / a2
    except ArithmeticError:
        ok = True
    assert ok
    r = a2 / a1
    assert np.array_equal(r, np.array([0.000000, 0.408203, 0.816406, 1.226562], dtype=bfloat16))
    ok = False
    np.seterr(divide='ignore', invalid='ignore')
    r = a1 / 0.0
    # promotes to float so ieee reporting which is NAN
    assert np.array_equal(r, np.array([float('inf'), float('inf'), float('inf'), float('inf')], dtype=np.float32))
    assert np.all(np.isclose(a1 - a2, a1.astype(np.float32) - a2.astype(np.float)))
    r1 = a1 * a2
    r2 = a1.astype(np.float32) * a2.astype(np.float)
    assert np.all(np.isclose(r1, r2, atol=0.02))
    assert np.sum(a1) == 9.8125

def test_scalars():
    assert bfloat16(1.3) == np.array(1.3, dtype=bfloat16)
    assert int(bfloat16(1.2)) == 1
    assert float(bfloat16(1.2)) == 1.203125
