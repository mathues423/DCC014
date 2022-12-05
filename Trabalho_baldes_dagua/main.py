import random
from buscas import busca
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def escolha_type_trabalho(busca: busca,escolha_trabalho: int, escolha_busca: int):
      if escolha_trabalho == 1:
            if escolha_busca == 1:
                  busca.busca_em_backtracking(verbose=True)
            elif escolha_busca == 2:
                  busca.busca_em_largura(verbose=True)
            elif escolha_busca == 3:
                  busca.busca_em_profundidade(verbose=True)
      else:
            if escolha_busca == 1:
                  print('não implementado')
                  #busca.busca_ordenada()
            elif escolha_busca == 2:
                  print('não implementado')
                  #busca.busca_gulosa()
            elif escolha_busca == 3:
                  print('não implementado')
                  #busca.busca_A_estrela()

def escolha_trabalho() -> int:
      print('Escolha o trabalho que deseja executar:')
      print('1 - Trabalho 1')
      print('2 - Trabalho 2')
      print('3 - Sair')
      print('4 - Alteração da ordem das regras')
      print('5- Limpar tela:\n', end='')
      escolha = int(input())
      while escolha not in [1, 2, 3, 4, 5]:
            escolha = int(input())
      return int(escolha)

def escolha_busca(escolha_trabalho: int):
      print('Escolha o tipo de busca:')
      if escolha_trabalho == 1:
            print('1 - Backtracking')
            print('2 - Em largura')
            print('3 - Em profundidade:\n', end='')
      else:
            print('1 - Ordenada')
            print('2 - Gulosa')
            print('3 - A*:\n', end='')
      escolha = int(input())
      while escolha not in [1, 2, 3]:
            escolha = int(input())
      return int(escolha)

def escolha_regras() -> 'list[str]':
      regras = [['E','A'],['E','B'],['V','A'],['V','B'],['A','B'],['B','A']]
      escolha = 0
      print('Escolha como queira alterar as regras:')
      print('1 - Randomico')
      print('2 - Escolher a ordem das regras')
      while escolha not in [1, 2]:
            escolha = int(input())
      
      if escolha == 1:
            random.shuffle(regras)
            return regras
      else:
            regras_aux = []
            while(len(regras) != 6):
                  print('Escolha a ordem das regras:')
                  for i in range(len(regras)):
                        print(f'{i+1} - {regras[i]}')
                  try:
                        regras_aux.append(regras.pop(int(input())-1))
                  except IndexError as error:
                        print('##Escolha uma opção válida##')
                        clear()
            return regras_aux

def tela_inicial(busca: busca):
      ''' Descrição do problema: 
      Você tem 2 jarros sem nenhuma marcação, com as respectivas capacidades: 1º 5 litros e o 2º 3 litros.
      O propósito do problema é que ocorra uma situação final de que o jarro de maior capacidade 
      fique com exatamente 1 litro.
      - Você pode executar as seguintes ações:
            - Enxer totalmente um jarro com a água do poço.
            - Esvaziar totalmente um jarro jogando a água na grama.
            - Passar a água de um jarro para o outro.
            - Os jarros começam vazios.

      --------------------------------------------------------
      Um ponto a observar é que a movimentação exige o cuidado de não ultrapassar a capacidade dos respectivos jarros.
      --------------------------------------------------------------

      buscas: backtracking, em largura e em profundidade (Trabalho 1)
      buscas: ordenada, gulosa e A* (Trabalho 2)
      '''
      escolha_t = 0
      while(True):
            escolha_b = 0
            escolha_r = 0
            escolha_t = escolha_trabalho()
            if escolha_t == 3:
                  break
            if escolha_t != 4 and escolha_t != 5:
                  escolha_b = escolha_busca(escolha_t)
                  escolha_type_trabalho(busca, escolha_t, escolha_b)
            elif escolha_t == 4:
                  escolha_r = escolha_regras()
                  busca.regras = escolha_r
            elif escolha_t == 5:
                  clear()
      return 0

if __name__ == '__main__':
      regras = [['E','A'],['E','B'],['V','A'],['V','B'],['A','B'],['B','A']]
      main = busca(regras,1)
      tela_inicial(main)