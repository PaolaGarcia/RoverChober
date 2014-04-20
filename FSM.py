import time

def adelante():
    print("u")
    return 0
def atras():
    print("d")
    return 0
def Mderecha():
    print("d")
    print("d")
    print("r")
    print("r")
    return 0
def Mizquierda():
    print("d")
    print("d")
    print("l")
    print("l")
    return 0

def Izquierda():
    print("d")
    print("l")
    print("l")
    print("l")
    print("l")
    return 0

def Derecha():
    print("d")
    print("r")
    print("r")    
    print("r")
    print("r")
    return 0
    
class Estado:
    def __init__(self, f, proximos, delay):
        self.f = f
        self.delay = 20
        self.proximos=proximos

FSM=[
Estado(adelante, [0,1,0,1,0,5,0,1,0,2,0,5,0,2,0,4,0,2,0,5,0,1,0,1,0,2,0,5,0,2,0,3],1),
Estado(Mizquierda, [0,1,0,1,0,5,0,1,0,2,0,5,0,2,0,4,0,2,0,5,0,1,0,1,0,2,0,5,0,2,0,3],50),
Estado(Mderecha, [0,1,0,1,0,5,0,1,0,2,0,5,0,2,0,4,0,2,0,5,0,1,0,1,0,2,0,5,0,2,0,3], 50),
Estado(atras, [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,3],100),
Estado(Derecha, [0,1,0,1,0,5,0,1,0,2,0,5,0,2,0,4,0,2,0,5,0,1,0,1,0,2,0,5,0,2,0,3], 50),
Estado(Izquierda, [0,1,0,1,0,5,0,1,0,2,0,5,0,2,0,4,0,2,0,5,0,1,0,1,0,2,0,5,0,2,0,3], 50)
    ]
S=0
while True:
    FSM[S].f();
    time.sleep(FSM[S].delay/1000);
    input1=int(raw_input("Lectura"));
    S=FSM[S].proximos[input1]
    
               
