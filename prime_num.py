def is_prime(number: int) -> bool:
    contador: int =0
    for i in range(1, number+1):
        if i == 1 or i==number:
            continue
        if number % i ==0:
            contador +=1
    if contador >0:
        return False
    else:
        return True
            


def run():
    number = int(input('Elige un numero para saber si es primo: '))
    print(is_prime(number))

if __name__=='__main__':
    run()