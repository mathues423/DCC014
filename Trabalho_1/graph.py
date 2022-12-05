"""

"""

class node:
      '''
      Estrutura do Nó de um Grafo 

            - Inicialização do Nó
                  - __init__(capacidade_a: int = 0, capacidade_b: int = 0)
                  - capacidade_a: capacidade do jarro A
                  - capacidade_b: capacidade do jarro B
            ------------------------------------------------------------
            - Métodos
                  - add_filho(filho: node)
                  - get_altura(): int
            ------------------------------------------------------------
            - Atributos
                  - pai: Nó que antecede o nó atual
                  - filhos: Lista de nós que são filhos do nó atual
                  - h: Altura do nó em relação a raiz
            
      '''
      def __init__(self, capacidade_a: int, capacidade_b: int):
            self.capacidade_a = capacidade_a
            self.capacidade_b = capacidade_b
            self.capacidade_a_max = 5
            self.capacidade_b_max = 3
            self.pai = None
            self.filhos = []
            self.h = 0
            self.peso_aresta = 0
                       
      def __str__(self):
            return "["+str(self.capacidade_a) + " " + str(self.capacidade_b)+"]"

      def add_filho(self, filho: 'node'):
            filho.__set_altura__(self.h+1)
            self.filhos.append(filho)
            filho.pai = self

      def __set_altura__(self, h: int):
            self.h = h
      
      def get_altura(self) -> int:
            return self.h
      
      def get_peso_aresta(self) -> int:
            return self.peso_aresta
class graph:
      '''
      Estrutura do Grafo 

            - Inicialização do grafo
                  - __init__(tipo: str, capacidade_a: int = 0, capacidade_b: int = 0)
                        - tipo: tipo da busca no grafo ex: Largura, Profundidade, Backtracking ....
                        - capacidade_a: capacidade inicial do jarro A
                        - capacidade_b: capacidade inicial do jarro B
            ------------------------
            - Metodos
                  - add_node(node_filho: node, node_pai: node)
                        - node_filho: nó filho a ser adicionado
                        - node_pai: nó pai que já existe no grafo
                  ------------------------
            ---------------
            - Atributos
                  - raiz: nó raiz do grafo
                        - Maior explicação do node em 'node.__doc__()'
                  
      '''
      def __init__(self, tipo: str, capacidade_a: int = 0, capacidade_b: int = 0):
            self.tipo = tipo
            self.raiz = node(capacidade_a, capacidade_b)
            
      def __str__(self):
            retorno = ''
            node_aux = self.raiz
            candidatos = [node_aux]

            while(candidatos != []):
                  node_aux = candidatos[0]
                  retorno += ' Pai: ' + str(node_aux.pai) + 'Node: '+ str(node_aux)
                  if(node_aux.get_peso_aresta() != 0):
                        retorno += ' Peso: ' + str(node_aux.get_peso_aresta())
                        #Condição caso tenha peso nas arestas
                  retorno += ' |h: ' + str(node_aux.get_altura()) + '\n'
                  candidatos.remove(node_aux)
                  candidatos += node_aux.filhos
            return retorno
      
      def add_node(self, node_filho: node, node_pai: node):
            if(not self.__verifica_se_exixte_no_caminho__(node_filho, node_pai)):
                  node_filho.__set_altura__(node_pai.get_altura() + 1)
                  node_pai.add_filho(node_filho)

      def __verifica_se_exixte_no_caminho__(self, node_filho: node, node_pai: node) -> bool:
            aux = node_pai
            while(aux != None):
                  if(aux.capacidade_a == node_filho.capacidade_a and aux.capacidade_b == node_filho.capacidade_b):
                        return True
                  aux = aux.pai
            return False     