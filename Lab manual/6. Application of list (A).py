def add(A, B, m, n): 
    size = max(m, n) 
    sum = [0 for i in range(size)] 
    for i in range(0, m, 1): 
        sum[i] = A[i] 
    for i in range(n): 
        sum[i] += B[i] 
    return sum 

def printPoly(poly, n): 
    for i in range(n): 
        print(poly[i], end="") 
        if i != 0: 
            print("x^", i, end="") 
        if i != n - 1: 
            print(" + ", end="") 
    print()

# The following array represents 
# polynomial 5 + 10x^2 + 6x^3 
A = [5, 0, 10, 6] 

# The following array represents 
# polynomial 1 + 2x + 4x^2 
B = [1, 2, 4] 

m = len(A) 
n = len(B) 

print("First polynomial is:") 
printPoly(A, m) 

print("Second polynomial is:") 
printPoly(B, n) 

sum = add(A, B, m, n) 
size = max(m, n) 

print("Sum polynomial is:") 
printPoly(sum, size)