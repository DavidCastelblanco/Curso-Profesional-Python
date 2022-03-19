
def firma (func):
    def agregar_firma(*args, **kwargs):
        func(*args, **kwargs)
        print ('\nEste código ha sido creado por David Castelblanco')
    return agregar_firma

@firma
def is_prime(number: int) -> bool:
    contador: int =0
    for i in range(1, number+1):
        if i == 1 or i==number:
            continue
        if number % i ==0:
            contador +=1
    if contador >0 or number==1:
        print('El numero elegido NO es primo')
    else:
        print('El numero elegido SI es primo')
           


def run():
    number = int(input('Elige un numero para saber si es primo: '))
    is_prime(number)

if __name__=='__main__':
    run()