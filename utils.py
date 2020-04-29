from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Lima', idade=45)
    pessoa.save()
    print(pessoa)

# Consulta tabela poessoas
def consulta_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Fábio').first()
    # for p in pessoa:
    #     print(pessoa)
    print(pessoa)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Lima').first()
    pessoa.idade = 40
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fábio').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    # exclui_pessoa()
    consulta_pessoas()
    # altera_pessoa()