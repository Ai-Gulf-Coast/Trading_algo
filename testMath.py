amount = 100000

def x(f, c, r):
    var = ((1 + (f/100)) ^ (c*(r/100)) * (1 - (f/100))^(c*(1 - (r/100))) - 1) * 100
    print(var)

x(50,288,60)

'''
f: fluctuation as a percentage of 100
c: number of 5 minute periods taken into account
r: success rate of model as a percentage of 100
'''


lp = 288






for i in range(365):
    amount = amount * 1.00035
print(amount)

2