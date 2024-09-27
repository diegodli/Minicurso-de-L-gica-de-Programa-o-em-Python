from modulo_calculadora import Somar, Subtrair, Dividir, Multiplicar, ElevarAoQuadrado, RaizQuadrada

def main():
    a = 4
    b = 2
    
    soma = Somar(a,b)
    subtracao = Subtrair(a,b)
    divisao = Dividir(a,b)
    multiplicacao = Multiplicar(a,b)
    quadrado = ElevarAoQuadrado(a)
    raiz_quadrada = RaizQuadrada(a)

if __name__ == "__main__":
    main()
