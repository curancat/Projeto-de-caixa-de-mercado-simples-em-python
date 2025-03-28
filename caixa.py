import os
import time

valor = 0
carrinho = []  # Lista para armazenar os produtos comprados

def apagar():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def salvar_nota():
    """Salva a nota fiscal manualmente em um arquivo .txt"""
    with open("nota_fiscal.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("--- NOTA FISCAL ---\n")
        for item in carrinho:
            linha = f"{item['nome'].capitalize():<15} R$ {item['preço']:.2f}\n"
            arquivo.write(linha)
        total = f"TOTAL: R$ {valor:.2f}\n"
        arquivo.write(total)
        arquivo.write("-------------------\n")
    print("\n✅ Nota fiscal salva como 'nota_fiscal.txt'.\n")
    time.sleep(2)
    apagar()

produtos = [
    {"nome": "feijão", "preço": 10},
    {"nome": "sal", "preço": 1},
    {"nome": "arroz", "preço": 10},
    {"nome": "açucar", "preço": 8.90},
    {"nome": "macarrão", "preço": 11.50},
    {"nome": "cuzcuz", "preço": 10.30},
    {"nome": "mantega", "preço": 9}
]

while True:
    registro = input("Insira um produto ('nota' para ver, 'salvar' para salvar, 'sair' para finalizar): ").strip().lower()

    if registro == "sair":
        break  # Sai do loop e imprime a nota final

    if registro == "nota":
        print("\n--- NOTA FISCAL ---")
        for item in carrinho:
            print(f"{item['nome'].capitalize():<15} R$ {item['preço']:.2f}")
        print(f"TOTAL: R$ {valor:.2f}")
        print("-------------------\n")
        time.sleep(3)
        apagar()
        continue  

    if registro == "salvar":
        salvar_nota()
        continue

    produto_encontrado = None
    for item in produtos:
        if item["nome"] == registro:
            produto_encontrado = item
            break

    if produto_encontrado:
        valor += produto_encontrado["preço"]
        carrinho.append(produto_encontrado)  # Adiciona o produto ao carrinho
        print("-"*10)
        print(f"Produto adicionado: {produto_encontrado['nome'].capitalize()}")
        print(f"Preço: R$ {produto_encontrado['preço']:.2f}")
        print("-"*10)
        time.sleep(2)
        apagar()
    else:
        print("-"*10)
        print("Produto não encontrado. Tente novamente.")
        print("-"*10)
        time.sleep(2)
        apagar()

# Salvar nota ao final
salvar_nota()
print("\n🛒 Compra finalizada. Nota fiscal salva automaticamente.")
