def exp_odd(exp_a, exp_n):
    if exp_n == 0:
        return 1
    elif exp_a > 0 and exp_n > 0:
        return exp_a * exp_odd(exp_a, exp_n - 1)


def exp_even(exp_a, exp_n):
    if exp_n == 0:
        return 1
    elif exp_a > 0 and exp_n > 0:
        return (exp_a ** 2) ** (n / 2)


def exp(exp_a, exp_n):
    if exp_n % 2 == 0:
        return exp_even(exp_a, exp_n)
    else:
        return exp_odd(exp_a, exp_n)


a = float(input())
n = int(input())
print(exp(a, n))
