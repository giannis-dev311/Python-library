pesos = int(input('what do you have left in pesos? '))
soles = int(input('what do you have left in soles? '))
reais = int(input('what do you have left in reais? '))

total = pesos*0.054 + soles *0.29 + reais*0.18
print('your total in USD is',total)