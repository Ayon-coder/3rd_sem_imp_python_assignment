def isPrime(n):

    for i in range(2, n):

        if n % i == 0:
            return False
    return n > 1

def primeSum(num):
    s = 0
    primes = []

    for i in range(2, num):
        if isPrime(i):
            s += i
            primes.append(i)
        if s == num:
            print(num, "=", " + ".join(map(str, primes)))
            return
        if s > num:
            break

    print("Not psooible")

num = int(input("Enter a number: "))
primeSum(num)