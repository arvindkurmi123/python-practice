# 3. LAMBDA FUNCTIONS (One-Line Functions)

square = lambda x: x * x
print(square(5))  # 25


arr = [(1, 3), (2, 1), (4, 2)]
arr.sort(key=lambda x: x[1])
print(arr)

# 25
# [(2, 1), (4, 2), (1, 3)]
