x = np.arange(1, 21, 1)
y = my_func(x + np.random.normal(1, 0.4, 20))

def my_func(x):
    b0 = 500
    S = b0 * 4
    k = 0.15
    return S - (S -b0) * np.exp(-k * x)

list(zip(np.arange(0, 20, 1), my_func(np.arange(0, 20, 1))))