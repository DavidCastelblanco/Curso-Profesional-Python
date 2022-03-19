import time
from unicodedata import numeric


class FiboIter():
    
    def __init__(self, stop_num=None):
        stop_num =  input('Ingresa el número hasta el cual deseas realizar las secuencia de Fibonacci\n (si no ingresas un numero entero la secuencia será infinita): ')
        if stop_num =='' or stop_num.isnumeric() == False:
            stop_num = None
        else:
            stop_num = int(stop_num)
        
        self.stop_num = stop_num

    def __iter__(self):
        
        self.n1 =0
        self.n2 = 1
        self.counter = 0
        self.aux = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if not self.stop_num or self.aux <= self.stop_num:
                self.aux = self.n1 +self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux #Esto es un swaping, un intercambio de variables
                self.counter +=1
                return self.aux
            else:
                raise StopIteration

def run():    
    fibonacci = FiboIter()
    for i in fibonacci:
        print(i)
        time.sleep(1)
   

if __name__=='__main__':
    run()
    