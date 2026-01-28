class CalculadoraAvancada:
    def __init__(self):
        self.historico = []
    
    def adicionar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado
    
    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(f"{a} × {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        resultado = a / b
        self.historico.append(f"{a} ÷ {b} = {resultado}")
        return resultado
    
    def mostrar_historico(self):
        return self.historico[-5:] if self.historico else "Sem histórico"

# Interface principal
def main():
    calc = CalculadoraAvancada()
    print("=== Calculadora Avançada ===")
    
    while True:
        print("\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Histórico\n6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '6':
            break
        
        if opcao in ['1', '2', '3', '4']:
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
                
                if opcao == '1':
                    print(f"Resultado: {calc.adicionar(a, b)}")
                elif opcao == '2':
                    print(f"Resultado: {calc.subtrair(a, b)}")
                elif opcao == '3':
                    print(f"Resultado: {calc.multiplicar(a, b)}")
                elif opcao == '4':
                    resultado = calc.dividir(a, b)
                    print(f"Resultado: {resultado}")
                    
            except ValueError:
                print("Erro: Digite números válidos!")
        elif opcao == '5':
            print("\nHistórico recente:")
            for calc in calc.mostrar_historico():
                print(calc)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
