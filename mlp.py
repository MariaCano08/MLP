import math
import random
import numpy as np
#Todos los metodos de una clase siempre reciben self
# ya activaste el entorno virtual?
class MLP:
    # def __init__(self,n_hidden, entry,hidden_layer,learning_rate,best_err,nl): #constructor
    #     self.n_hidden= n_hidden
    #     self.error_actual=0
    #     self.hidden_layer=hidden_layer
    #     self.learning_rate=learning_rate
    #     self.best_err=best_err
    #     self.epoch=0
    #     self.nl=nl #neuronas por capa

    #     #1.-Obtener el conjunto de muestras de entrenamiento
    #     #2.-Asociar la salida deseada para cada muestra obtenida
    #     self.entry=entry
    #     #3.-Inicializar las matrices de pesos (dependiendo de la cantidad de capas 
    #     # son la cantidad de matrices)
    #     self.weight=matrices()#recibe la cantidad de capas ocultas

    def __init__(self):
        self.hidden_layer=3
        self.nl=4
        self.out_layer=3 #clases existentes
        self.weight =self.matrices()
        self.learning_rate=0.1
        self.presicion=0.2
        self.limit_epoch=10000
        self.humbral_out=[1 for i in range(0,self.out_layer)]
        print("humbral out layer",self.humbral_out)

        self.di=0
        self.err_total=1
        self.err_cm=0 #error cuadratico medio
        self.err_previo=0
        self.errores=[]

        

    def start(self):
        pass

    def matrices(self):
        w=[]
        ent=2
        for i in range(0,self.hidden_layer):
            w_=[]
            for en in range(0,ent):
                layer=[1]+[random.random() for k in range(0,self.nl)]
                
                w_.append(layer)
            w.append(w_)
            ent=self.nl
        w.append([[1]+[random.random() for k in range(0,self.out_layer) ]for i in range(0, self.nl)])

        
        for w_ in w:
            for ww in w_:
                print(ww)
            print("")
        return w

   
