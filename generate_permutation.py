def perm(a, n):
    if n == 1:
        print(*a)
    else:
        for i in range(n):
            a[i], a[n - 1] = a[n - 1], a[i]
            perm(a, n - 1)
            a[i], a[n - 1] = a[n - 1], a[i]
