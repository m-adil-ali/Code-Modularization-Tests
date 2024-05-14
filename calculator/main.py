# Importing other modules

from calculator.add import add
from calculator.sub import sub
from calculator.mul import mul
from calculator.div import div

def run_test():
    print(add(15,20))
    print(sub(8,20))
    print(mul(5,7))
    print(div(99,9))
    
if __name__ == "__main__":
    run_test()