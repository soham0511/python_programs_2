#Map function

# map(function_to_apply, list of inputs)

def square(n):
    return n**2

h1 = [1,2,4,5,7]
# sq =[]
# for item in h1:
#     sq.append(item**2)

sq = list(map(square, h1))
print(sq)

