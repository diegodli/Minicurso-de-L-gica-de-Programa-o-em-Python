#funcao que retorna o quadrado de um numero

def Quadrado(numero):
    return numero**2

#funcao que verifica se um numero é primo

def VerificarPrimo(numero):
    if numero <=1:
        return False
    for i in range(2,int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


#funcao que recebe uma lista e retorna a media dos elementos
def MediaLista(lista):
    for numero in lista:
        soma = soma + numero
    return soma/len(lista)


    
     

        


   