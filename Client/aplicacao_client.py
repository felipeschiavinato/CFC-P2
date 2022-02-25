import random as rd
from enlace import *
import time
import numpy as np

#Gera um numero aleatorio de 10 - 30
n_codigos = rd.randint(10,30)
print(n_codigos)

#Lista de comandos
comandos = {}
comandos[1] = [b'\x00',b'\xFF',b'\x00',b'\xFF']
comandos[2] = [b'\x00',b'\xFF',b'\xFF',b'\x00']
comandos[3] = [b'\xFF']
comandos[4] = [b'\x00']
comandos[5] = [b'\xFF',b'\x00']
comandos[6] = [b'\x00',b'\xFF']

#Faz a lista de comandos
l_comandos = []
for i in range(n_codigos):
    l_comandos.append(comandos[rd.randint(1,6)])


#Preve o tamanho da lista final
l_size = n_codigos + 1
for l in l_comandos:
    l_size += len(l)

l_size -= 1

#Cria lista a ser enviada ao arduino
l_send = []
l_send.append(l_size.to_bytes(1, byteorder='big'))
for i in l_comandos:
    size = len(i).to_bytes(1, byteorder='big')
    l_send.append(size)
    for e in i:
        l_send.append(e)





serialName = "COM7"

def main():
    try:
        tempo_inicial = time.time()
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Comunication open") 
  

        
        txBuffer = l_send
        print(txBuffer)
        print("\n-------------------------")
    
        print("The file transfer is about to start")

        print("\n-------------------------")


        inicio_timer = time.time()
        com1.sendData(np.asarray(txBuffer), inicio_timer)
        

        print("Command sent")  
        print("-------------------------")

        
        print("\n-------------------------")
        print(f"foram mandados {len(txBuffer)} bytes e {n_codigos} comandos")
        print("-------------------------\n")

    
        
        rxBuffer, nRx = com1.getData(1, inicio_timer)
        if rxBuffer == None:
            com1.disable()
            return
        
            
            



        
        print("\n-------------------------")
        print(f"Server received {rxBuffer[0]} commands")
        print("-------------------------\n")

        com1.disable()

        print(n_codigos)

    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()

    
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()