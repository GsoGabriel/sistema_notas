#Funções do sistema de cadastro de alunos e suas respectivas notas

#função para cadastrar o nome de cada aluno
def cadastro_alunos():
	arquivo = open('cadastro.cvs', 'a')
	cadastrar_mais = 's'
	while cadastrar_mais == 's':
		aluno=input('Digite o nome do aluno que você deseja cadastrar: ')
		arquivo.write(aluno+'\n')
		cadastrar_mais=input('Deseja cadastrar mais alunos? (s/n) ')
	arquivo.close()

#função para cadastrar as notas de cada aluno
def notas_alunos():
	arquivo_notas = open('notas.cvs', 'a')
	arquivo_cadastro = open('cadastro.cvs', 'r')
	nomes_alunos = arquivo_cadastro.read()
	nomes_alunos = nomes_alunos.split('\n')
	for x in nomes_alunos:
		for y in range(1,5):
			nota=int(input('Digite a {}ª nota do aluno {}: '.format(y, x)))
			while nota>10 or nota<0:
				nota=int(input('Nota inválida. Por favor, digite a {}ª nota do aluno {}: '.format(y, x)))
			if y<4:
				arquivo_notas.write(str(nota)+', ')
			else:
				arquivo_notas.write(str(nota)+'\n')
	arquivo_notas = open('notas.cvs', 'r')
	notas_alunos = arquivo_notas.read()
	notas_alunos = notas_alunos.split('\n')
	for z in range(len(nomes_alunos)): 
		print(nomes_alunos[z])
		notas_alunos[z]=notas_alunos[z].split(', ')
		notas=[int(val) for val in notas_alunos[z]]
		print(notas_alunos[z])
		media=lambda nota: sum(nota) / len(nota)
		print(str(media(notas))+'\n')

#comando do programa
a= input('Deseja cadastrar alunos? (s/n)')
if a=='s':
	cadastro_alunos()
	notas_alunos()
else:
	notas_alunos()