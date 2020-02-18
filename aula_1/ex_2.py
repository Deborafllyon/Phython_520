# Tipos primitivos

texto = 'Debora llyon'
inteiro = 27
decimais = 1.80
booleano = True # False
complexo = complex(2, 3)

#Ex 2 
#solicitar ao usuario as informacoess:
#nome
#idade 
#email
# e armazenar oas valores em variaveis 
# (escolham bem os nomes )

nome = input ("Escreva seu nome:  ")
idade  = input('Digite sua idade')    
email = input ('Digite seu email')

print (nome)
print (idade)
print (email)

if int (idade) < 18:
    print('Ola)
    else:('Bloqueado')