import buscas
import random
from buscas import busca
if __name__ == '__main__':
      regras = [['V','B'],['B','A'],['E','B'],['V','A'],['E','A'],['A','B']]
      random.shuffle(regras)
      main = busca(regras,1)
      main.busca_em_backtracking(verbose=True)
      main.busca_em_largura(verbose=True)
      main.busca_em_profundidade(verbose=True)      

      #Adição do print dos grafos para visualização (faltando)