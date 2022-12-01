import buscas
from buscas import busca
if __name__ == '__main__':
      regras = [['E','A'],['V','B'],['B','A'],['V','A'],['A','B'],['E','B']]
      regras.sort()
      main = busca(regras,1)
      raiz = main.busca_em_backtracking().raiz
      while(raiz.filhos != []):
            for i in raiz.filhos:
                  print(i.__str__())
            raiz = i.filhos[0]
            
      #main.
      # graph_backtracking = buscas
      # graph_largura = 
      # graph_profundidade = 
