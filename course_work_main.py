from math import sqrt
# 1) Один алгоритм факторизації довгих цілих чисел на вибір:
#       ро-алгоритм Полларда або алгоритм квадратичного решета.
# 2) Один алгоритм знаходження дискретного логарифма на вибір:
#       ро-алгоритм Полларда або алгоритм «великий крок – малий крок».
# 3) Обчислення функцій Ейлера та Мьобіуса.
# 4) Обчислення символів Лежандра та Якобі.
# 5) Алгоритм Чіпполи знаходження дискретного квадратного кореня.
# 6) Один алгоритм перевірки чисел на простоту на вибір:
#       алгоритм Соловея-Штрассена або алгоритм Міллера-Рабіна.
# 7) Криптосистема Ель-Гамаля над еліптичними кривими.


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def _rho_pollard(number):
    answer = set()
    for d in range(2, min(int(sqrt(sqrt(number))) + 10, number)):
        if number % d == 0:
            answer.add(d)
        while number % d == 0:
            number //= d

    if number == 1:
        return answer

    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1

    while factor == 1:
        count = 1
        while count <= cycle_size and factor <= 1:
            x = (x * x + 1) % number
            factor = gcd(x - x_fixed, number)
            count += 1
        cycle_size *= 2
        x_fixed = x

    if factor == number:
        return {factor} | answer
    else:
        return {factor} | rho_pollard(number // factor) | answer


def rho_pollard(number):
    factors = _rho_pollard(number)

    factor_powers = {}

    for factor in factors:
        while number % factor == 0:
            factor_powers[factor] = factor_powers.get(factor, 0) + 1
            number //= factor

    sl = []
    for factor, power in factor_powers.items():
        sl.append(f'{factor}^{power}')

    return factor_powers, ' * '.join(sl)


print(rho_pollard(1582)[1])



def pho_pollard_logarithm(p, g, t):
    # 2) Один алгоритм знаходження дискретного логарифма: ро-алгоритм Полларда
    a, b, x = [], [], []
    a[0], b[0], x[0] = 0, 0, 1
    two_triples = []
    i = 1
    while not x_i == x_2i:

        def ai_bi(i, p, a, b):
            if 0 < x[i-1] < p/3:
                a[i], b[i] = (a[i-1] + 1) % (p - 1), b[i-1] % (p - 1)
            elif p/3 < x[i-1] < 2*p/3:
                a[i], b[i] = 2*a[i-1] % (p-1), 2*b[i-1] % (p-1)
            elif 2*p/3 < x[i-1] < p:
                a[i], b[i] = a[i-1] % (p-1), b[i] % (p-1)

            return a[i], b[i]

        # why can't x be more than p or less than 0?? TODO

        a_i, b_i = ai_bi(i, p, a, b)
        a_2i, b_2i = ai_bi(2*i, p, a, b)

        def xi(i, p, t, g, x):
            if 0 < x[i-1] < p/3:
                x[i] = t * x[i-1] % p
            elif p / 3 < x[i - 1] < 2 * p / 3:
                x[i] = (x[i-1] ** 2) % p
            elif 2 * p / 3 < x[i - 1] < p:
                g * x[i-1] % p

            return x[i]

        x_i = xi(i, p, t, g, x)
        x_2i = xi(2*i, p, t, g, x)

    # making up the equation TODO
    def eq(x, y, a_i, a_2i, p):
        (x * (a_2i - a_i)/gsd(a_2i - a_i, p - 1) + y * (p - 1)/(a_2i - a_i, p - 1)) % p = (b_i - b_2i) % p


