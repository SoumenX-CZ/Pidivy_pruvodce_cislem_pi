import math
import random
from decimal import Decimal, getcontext
from time import time

# Nastavení přesnosti na 50 desetinných míst
getcontext().prec = 52

# 1. Archimédův algoritmus (přiblížení pomocí mnohoúhelníků)
def archimedes_pi():
    n = 6  # Počet stran mnohoúhelníku
    side_length = 1  # Délka strany
    for _ in range(20):
        n *= 2
        side_length = math.sqrt(2 - 2 * math.sqrt(1 - (side_length / 2) ** 2))
    perimeter = n * side_length
    return Decimal(perimeter / 2)

# 2. Madhavova řada (základní řada)
def madhava_pi():
    pi_approx = Decimal(0)
    for k in range(500):
        pi_approx += Decimal((-1) ** k) / (2 * k + 1) * (Decimal(3) ** (-k))
    return Decimal(math.sqrt(12)) * pi_approx

# 3. Gregory-Leibnizova řada
def gregory_leibniz_pi():
    pi_approx = Decimal(0)
    for k in range(100000):
        pi_approx += Decimal((-1) ** k) / (2 * k + 1)
    return Decimal(4) * pi_approx

# 4. Machinův vzorec
def machin_pi():
    return 4 * (4 * Decimal(math.atan(1 / 5)) - Decimal(math.atan(1 / 239)))

# 5. Monte Carlo metoda
def monte_carlo_pi(samples=10**7):
    inside_circle = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    return Decimal(4 * inside_circle / samples)

# 6. Borweinova metoda
def borwein_pi():
    a = Decimal(1 / math.sqrt(2))
    b = Decimal(1)
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    for _ in range(10):
        a_next = (a + b) / 2
        b = Decimal(math.sqrt(a * b))
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2
    return (a + b) ** 2 / (4 * t)

# 7. Gauss-Legendreův algoritmus
def gauss_legendre_pi():
    a = Decimal(1)
    b = Decimal(1) / Decimal(math.sqrt(2))
    t = Decimal(1) / 4
    p = Decimal(1)
    for _ in range(10):
        a_next = (a + b) / 2
        b = Decimal(math.sqrt(a * b))
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2
    return (a + b) ** 2 / (4 * t)

# 8. Chudnovského algoritmus
def chudnovsky_pi():
    def chudnovsky_term(k):
        numerator = Decimal(math.factorial(6 * k)) * (545140134 * k + 13591409)
        denominator = Decimal(math.factorial(3 * k)) * (math.factorial(k) ** 3) * (640320 ** (3 * k))
        return Decimal(numerator) / Decimal(denominator)

    total = Decimal(0)
    for k in range(20):
        total += chudnovsky_term(k)
    constant = Decimal(426880) * Decimal(math.sqrt(10005))
    return constant / total

# Výsledky
algorithms = {
    "Archimédův algoritmus": archimedes_pi,
    "Madhavova řada": madhava_pi,
    "Gregory-Leibnizova řada": gregory_leibniz_pi,
    "Machinův vzorec": machin_pi,
    "Monte Carlo metoda": monte_carlo_pi,
    "Borweinova metoda": borwein_pi,
    "Gauss-Legendreův algoritmus": gauss_legendre_pi,
    "Chudnovského algoritmus": chudnovsky_pi,
}

true_pi = Decimal("3.141592653589793238462643383279")

for name, func in algorithms.items():
    start_time = time()
    result = func()
    end_time = time()
    elapsed_time = end_time - start_time
    formatted_result = result.quantize(Decimal('1.00000000000000000000'))
    accuracy = round(formatted_result/true_pi *100, 20) if formatted_result <= true_pi else round(true_pi/formatted_result *100, 20)
    print(f"{name}: {formatted_result}\nDoba výpočtu: {elapsed_time:.5f} sekund\nPřesnost: {accuracy}\n")
