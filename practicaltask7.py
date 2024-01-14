import math
import random
import string

# Constants for MRG32k3a
norm = 2.328306549295728e-10  # 1 / 2^32
m1 = 4294967087.0
m2 = 4294944443.0
a12 = 1403580.0
a13n = 810728.0
a21 = 527612.0
a23n = 1370589.0

# Seeds for MRG32k3a
s10 = 12345
s11 = 12345
s12 = 123
s20 = 12345
s21 = 12345
s22 = 123

def Rand():
    global s10, s11, s12, s20, s21, s22
    k, p1, p2 = 0, 0, 0

    # Component 1
    p1 = a12 * s11 - a13n * s10
    k = math.floor(p1 / m1)
    p1 -= k * m1
    if p1 < 0.0:
        p1 += m1
    s10 = s11
    s11 = s12
    s12 = p1

    # Component 2
    p2 = a21 * s22 - a23n * s20
    k = math.floor(p2 / m2)
    p2 -= k * m2
    if p2 < 0.0:
        p2 += m2
    s20 = s21
    s21 = s22
    s22 = p2

    # Combination
    if p1 <= p2:
        return ((p1 - p2 + m1) * norm)
    else:
        return ((p1 - p2) * norm)

def RandInt(a, b):
    return a + math.floor((b - a + 1) * Rand())

def RandFloat(a, b):
    return a + (b - a) * Rand()

def RandElement(A):
    return A[RandInt(0, len(A) - 1)]

def RandString(a):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(a))