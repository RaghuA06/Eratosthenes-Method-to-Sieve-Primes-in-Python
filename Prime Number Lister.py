#Raghu Alluri
#Lists any number of prime numbers

user_integer = input("Enter the number of prime numbers you want to be listed: ")
num_primes = int(user_integer)

def list_primes(length):
    num_lst = []
    
    for num in range(1, length):
        num_lst.append(num + 1)

    for prime_num in num_lst:
        for num in num_lst:
            if num % prime_num == 0 and num != prime_num:
                num_lst.remove(num)

    return num_lst


print(list_primes(num_primes))
