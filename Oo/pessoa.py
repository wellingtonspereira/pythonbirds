class  Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = None

    def cumprimento(self):
        return f'Olá {id(self)}'
    if __name__ == ' __main__ ':
               p = pessoa('Luciano')
               print (pessoa.cumprimento(p))
               print (id(p))
               print (p.cumprimentar())
               print (p.nome)
               p.nome = 'Renzo'
               print (p.nome)
               print (p.idade)