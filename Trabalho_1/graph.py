class node:
      ''' Estrutura do Nó de um Grafo '''
      def __init__(self, capacidade_a: int, capacidade_b: int):
            self.capacidade_a = capacidade_a
            self.capacidade_b = capacidade_b
            self.capacidade_a_max = 5
            self.capacidade_b_max = 3
            self.pai = None
            self.filhos = []
            self.h = 0
            #self.peso_aresta = 0
                       
      def __str__(self):
            return "["+str(self.capacidade_a) + " " + str(self.capacidade_b)+"]"

      def add_filho(self, filho):
            self.filhos.append(filho)
            filho.pai = self

      def set_altura(self, h):
            self.h = h
      
      def get_altura(self):
            return self.h

class graph:
      ''' Estrutura do Grafo '''
      def __init__(self, tipo: str, capacidade_a: int = 0, capacidade_b: int = 0):
            self.tipo = tipo
            self.raiz = node(capacidade_a, capacidade_b)
            
      def __str__(self):
            return "Não programada ainda"
      
      def add_node(self, node_filho: node, node_pai: node):
            if(not self.verifica_se_exixte_no_caminho(node_filho, node_pai)):
                  node_pai.add_filho(node_filho)

      def verifica_se_exixte_no_caminho(self, node_filho: node, node_pai: node) -> bool:
            aux = node_pai
            while(aux != None):
                  if(aux.capacidade_a == node_filho.capacidade_a and aux.capacidade_b == node_filho.capacidade_b):
                        return True
                  aux = aux.pai
            return False

      
            