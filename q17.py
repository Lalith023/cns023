def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def multiplicative_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('No multiplicative inverse found')
    else:
        return x % phi

def find_p_q(n):
    p = 2
    while p * p <= n:
        if n % p:
            p += 1
        else:
            return p, n // p
    return n, 1

def find_private_key(e, n):
    p, q = find_p_q(n)
    phi = (p - 1) * (q - 1)
    return multiplicative_inverse(e, phi)

# Test the function
e = 31
n = 3599
private_key = find_private_key(e, n)

print(f"Private key: {private_key}")
