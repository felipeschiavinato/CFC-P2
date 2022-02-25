from logging import exception
import random as rd
from enlace import *
import time
import numpy as np

serialName = "COM8"

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
        
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        #print um aviso de que a recepção vai começar.

        print("Reception is about to start")
        
        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen
      
        #acesso aos bytes recebidos
        rxBuffer_size, nRx = com1.getData(1)
        print(rxBuffer_size)
        rxBuffer_size_int = int.from_bytes(rxBuffer_size, byteorder='big')

        print("-------------------------")
        print(f"BitSize recived {rxBuffer_size_int}")
        
        

        rxBuffer, nRx = com1.getData(int.from_bytes(rxBuffer_size, byteorder='big'))
        print(rxBuffer)
        print(f"Os dados foram recebidos")

        # print(type(rxBuffer))
        # print(str(rxBuffer))
        # print(type(str(rxBuffer)))


        i=0
        n_comandos=0
        iteracao = 0
        while i<len(rxBuffer):

            command_size = rxBuffer[i]

            n_comandos+=1

            i += command_size+1

            # print(f'interacao: {iteracao}')
            # print(f'i: {i}')
            # print(f'ncomandos: {n_comandos}')
            # print(f'comanddize: {command_size}')
            # print('*'*50)
            iteracao+=1

        

        com1.sendData(np.asarray(n_comandos.to_bytes(1, byteorder='big')))

        print("-------------------------")
        print(f"foi enviado oo Client que o Server recebeu {n_comandos})")
        #Envia tamanho da lista
       

        
        
        
        


        # Encerra comunicação
        com1.disable()
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        

        print("\n-------------------------")
        print(f"tempo total foi: {(time.time()-tempo_inicial):.2f} segundos")
        print(f"foram mandados {rxBuffer_size_int} bytes e recebidos {len(rxBuffer)} bytes")
        print("-------------------------\n")

    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()

if __name__ == "__main__":
    main()