num = int(input('fala o numerinho '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('{}, {}, {}, {}, {}'.format(num, u, d, c, m))