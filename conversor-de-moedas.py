import requests

url = "https://api.exchangerate-api.com/v6/latest" #endereço da API da corretora para montar um conversor de moedas
requisicao = requests.get(url)
print(requisicao.status_code) #verificação se o endereço está funcionando - retornando (obj: 200) está tudo ok

dados = requisicao.json() #Recuperando os dados da requisição - Pega o json retornado da API e transforma num dicionario (mapa)
print(dados)

# Conversor de moedas:

ciclo = 0
while (ciclo >= 0):
    moeda = float(input("Qual conversão deseja realizar?\n 1 - Dolar/Real\n 2 - Real/Dolar\n"))
    cotacao = dados["rates"]["BRL"]  # Na posição [rates] pegar o valor da chave [BRL] - valor da cotação

    if moeda == 2:
        valor_moeda = float(input("Qual o valor em R$ a ser convertido?\n"))  # float para converter em number
        print(f"R$ {valor_moeda} valem $ {(valor_moeda / cotacao):.2f}.\n")
    elif moeda == 1:
        valor_moeda = float(input("Qual o valor em $ a ser convertido?\n"))  # float para converter em number
        print(f"$ {valor_moeda} valem R$ {(valor_moeda * cotacao):.2f}.\n")



