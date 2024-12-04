def b(x, y):
    x1, x2, x3, x4 = x
    y1, y2, y3, y4 = y

    return 4 * x1 * y1 + 3 * x2 * y1 + 2 * x3 * y1 + 3 * x1 * y2 + 3 * x2 * y2 + 2 * x3 * y2 + x4 * y2 + 2 * x1 * y3 + 2 * x2 * y3 + 2 * x3 * y3 + x4 * y3 + x2 * y4 + x3 * y4 + 2 * x4 * y4


kappa1 = (0, -1, 1, 0)
kappa2 = (1, -2, 0, 1)
kappa3 = (-1, 1, 0, 0)
kappa4 = (0, 0, 0, 1)

print(b(kappa4, kappa4))
