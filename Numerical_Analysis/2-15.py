## 2.15
# (1)
sol_1 = 0
for i in range(50000):
    sol_1 += 0.00002
print('Solution #1 =>',sol_1)

# (2)
sol_2_1, sol_2_2 = 0, 0
for k in range(500):
    sol_2_1 += 0.00002
for kk in range(100):
    sol_2_2 += sol_2_1
print('Solution #2 =>',sol_2_2)

# (2)
sol_3_1, sol_3_2, sol_3_3 = 0, 0, 0
for u in range(50):
    sol_3_1 += 0.00002
for uu in range(10):
    sol_3_2 += sol_3_1
for uuu in range(10):
    sol_3_3 += sol_3_2

print('Solution #3 =>',sol_3_3)