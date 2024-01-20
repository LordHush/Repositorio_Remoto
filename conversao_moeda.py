def conversao_moeda(moeda,valor_inicial,valor_final):
    valores={
    ("dolar","real"):4.90,
    ("real","dolar"):0.20
    }
    
    if (valor_inicial,valor_final) not in valores.keys():
        return "moeda não existes"


    valor_conversao = valores[(moeda_inicial, moeda_final,)]
    resultado = moeda * valor_conversao  

    return resultado
valor_inicial=float(input("digite valorrr: "))
moeda_inicial=input("a digite a moeda que você tem(dolar,real): ")
moeda_final=input("digite a moeda que você quer converter(dolar,real): ")

resultado=conversao_moeda(valor_inicial,moeda_inicial,moeda_final)
if type(resultado) == float:
    print(f"{valor_inicial:.2f} {moeda_inicial} é igual a {resultado:.2f} {moeda_final}")
else:
    print(resultado)

