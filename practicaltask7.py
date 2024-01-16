class MRG32k3a:
    def __init__(self, seed1, seed2, seed3, seed4, seed5, seed6):
        self.m1 = 2**32 - 209
        self.m2 = 2**32 - 22853
        self.a12 = 1403580
        self.a13n = 810728
        self.a21 = 527612
        self.a23n = 1370589
        self.norm = 2.32825e-10

        self.x = [seed1, seed2, seed3, seed4, seed5, seed6]

    def generate(self):
        k, h, p1, p2 = 0, 3, 0, 3
        q1 = self.m1 // self.a12
        q2 = self.m2 // self.a21

        k = self.x[h] // self.a13n
        p1 = self.a13n * (self.x[h] % q1) - k * q1

        if p1 < 0:
            p1 += self.m1

        self.x[h] = self.x[p1]

        k = self.x[h] // self.a23n
        p2 = self.a23n * (self.x[h] % q2) - k * q2

        if p2 < 0:
            p2 += self.m2

        self.x[h] = self.x[p2]

        if self.x[h] == 0:
            self.x[h] = self.m1 - 1

        return self.x[h] * self.norm


def Rand():
    # Set initial seeds
    seed1, seed2, seed3, seed4, seed5, seed6 = 12345, 12345, 12345, 12345, 12345, 12345
    generator = MRG32k3a(seed1, seed2, seed3, seed4, seed5, seed6)
    return generator.generate()


def RandInt(a, b):
    return int(Rand() * (b - a + 1) + a)


def RandFloat(a, b):
    return Rand() * (b - a) + a


def RandElement(A):
    return A[RandInt(0, len(A) - 1)]


def RandString(a):
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?,./"
    return ''.join(RandElement(symbols) for _ in range(a))


# Examples
print(RandInt(1, 10))  # Output: Random integer between 1 and 10
print(RandFloat(0.0, 1.0))  # Output: Random float between 0.0 and 1.0
print(RandElement([1, 2, 3, 4, 5]))  # Output: Random element from the array
print(RandString(8))  # Output: Random string of length 8