nome="Sandro"
DiaVencimento=10
MesVencimento="Junho"
ValorFatura=150.80

# Python tem diversas possibilidades de formatação de string que permitem que você crie seu texto de saída de forma bem mais legível.

###### Uma delas é o método ".format" de strings:
print("Olá {nome},\n A sua fatura com vencimento em {vencimento} de {mesvencimento} no valor de R${valor:0.02f} está fechada.".format(nome=nome, vencimento=DiaVencimento,  mesvencimento=MesVencimento, valor=float(ValorFatura)))

print()
# E na versão 3.6 em diante você pode até usar strings com o prefixo f" " que permitem a formatação direta a partir das variáveis, sem precisar chamar o método format.

###### Ou seja, fica só assim:
print(f"Olá, {nome},\nA sua fatura com vencimento em {DiaVencimento} de {MesVencimento} no valor de R$ {ValorFatura} está fechada.")
