def prime_num(a):
    if a <= 1:
        return "not a prime number"
    for i in range(2,a):
        if a % i == 0:
            return "not a prime number"
            
    return "prime number"
    
print(prime_num(37))

