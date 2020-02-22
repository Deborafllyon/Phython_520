#argumentos nomeados

class Usuario:

    id = 1
    nome = 'Lucas Ricciardi de Sales'
    idade = 26

    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

usuario = Usuario(id=11, nome="lucas", idade=26)
usuario_2 = Usuario(id=2, nome='cory', idade=0)

print(usuario.id)
print(usuario.nome)
print(usuario.idade)