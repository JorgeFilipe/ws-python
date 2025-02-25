#
# Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do
# ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.
# 
#
import datetime

anoAtual=datetime.date.today()
diaDoMes = int(input("Informe o dia do mês atual: "))
mesAtual = int(input("Informe o mês atual: "))
diasPassados = (mesAtual*30)-(30-diaDoMes)

print(f"Desde o início do ano até a data de {diaDoMes}/{mesAtual}/{anoAtual.year}")
print(f"se passaram: {diasPassados} dias")
