nome = input ("Escreva seu nome:  ")
idade = input('Digite sua idade')    
email = input ('Digite seu email')

print (nome)
print (idade)
print (email)

user = {

    'nome':input ("Escreva seu nome:  "),
    'idade':input ('Digite sua idade:  '),   
    'email':input ('Digite seu email:  ')
   
}

idade = int (user['idade'])

if idade > 18:
    print('Maior de 18')
else:
    print('Menor de 18')

#Operadores 

#a = 3,1415
#b = 10

#print(a + b )   #soma
#print(a - b)    #subtracao
#print(a*b)      #multiplicacacao
#print(a / b )   #divisao
#print (a % b) 3   #modulo (resto da divisao)
#print (a **b) # exponenciacao


#Operacoes entre booleano

#operacao entre strings
#first name = Debora
#last_name = Llyon

#concentracao 
# print (first_name + '' + last_name)

#interpretacao
#mensagem = 'Ola, {}, Seja bem vindo' . format(
#    fist) name
    
#)
#print (mensagem)