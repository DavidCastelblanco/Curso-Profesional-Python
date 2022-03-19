import time
from unicodedata import numeric

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0
    stop_num =  input('Ingresa el número hasta el cual deseas realizar las secuencia de Fibonacci\n (si no ingresas un numero entero la secuencia será infinita): ')
    if stop_num =='' or stop_num.isnumeric() == False:
        stop_num = None
    else:
        stop_num = int(stop_num)
    while True:
        if counter == 0:
            counter +=1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            if not stop_num or aux <= stop_num:
                aux = n1 +n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break
            
if __name__=='__main__':
    fibonacci = fibo_gen()
    for i in fibonacci:
        print(i)
        time.sleep(1)