''' Descrição do problema: 
Você tem 2 jarros sem nenhuma marcação, com as respectivas capacidades: 1º 5 litros e o 2º 3 litros
. O propósito do problema é que ocorra uma situação final de que o jarro de maior capacidade 
fique com exatamente 1 litro.
. Você pode executar as seguintes ações:
      • Enxer totalmente um jarro com a água do poço;
      • Esvaziar totalmente um jarro jogando a água na grama;
      • Passar a água de um jarro para o outro.
      • Os jarros começam vazios.
Um ponto a observar é que a movimentação exige o cuidado de não ultrapassar a capacidade dos respectivos jarros.

buscas: backtracking, em largura e em profundidade
'''
import graph

class busca:
      '''Para a inicialisação das buscas é necessário que seja passado o conjunto de regras que serão utilizadas.\n
      -Exemplo:\n
            regras = [regra1, regra2, regra3, regra4, regra5, regra6]\n
            tendo que cada regra é uma lista de 2 elementos onde:\n
            ['E','A'] quer dizer que é para encher a água do jarro A\n
            ['E','B'] quer dizer que é para encher a água do jarro B\n
            ['A','B'] quer dizer que é para passar a água do jarro A para o jarro B\n
            ['B','A'] quer dizer que é para passar a água do jarro B para o jarro A\n
            ['V','A'] quer dizer que é para esvasiar a água do jarro A\n
            ['V','B'] quer dizer que é para esvasiar a água do jarro B\n
       '''
      def __init__(self, regras: list, objetivo_jarro_a:int=None, objetivo_jarro_b:int=None):
            if(len(regras) != 6):
                  raise AttributeError('O número de regras deve ser 6')
            self.regras = regras
            self.action = self.regras_to_action()
            self.objetivo_jarro_a = objetivo_jarro_a
            self.objetivo_jarro_b = objetivo_jarro_b
      
      def encher_a(self, node_pai: graph.node):
            '''Encher o jarro A'''
            node = graph.node(5, node_pai.capacidade_b)
            return node

      def encher_b(self, node_pai: graph.node):
            '''Encher o jarro B'''
            node = graph.node(node_pai.capacidade_a, 3)
            return node

      def passar_a_para_b(self, node_pai: graph.node):
            '''Passar a água do jarro A para o jarro B'''
            if(node_pai.capacidade_a + node_pai.capacidade_b > 3):
                  node = graph.node(node_pai.capacidade_a - (3 - node_pai.capacidade_b), 3)
            else:
                  node = graph.node(0, node_pai.capacidade_a + node_pai.capacidade_b)
            return node
      
      def passar_b_para_a(self, node_pai: graph.node):
            '''Passar a água do jarro B para o jarro A'''
            if(node_pai.capacidade_a + node_pai.capacidade_b > 5):
                  node = graph.node(5, node_pai.capacidade_b - (5 - node_pai.capacidade_a))
            else:
                  node = graph.node(node_pai.capacidade_a + node_pai.capacidade_b, 0)
            return node

      def esvaziar_a(self, node_pai: graph.node):
            '''Esvaziar o jarro A'''
            node = graph.node(0, node_pai.capacidade_b)
            return node

      def esvasiar_b(self, node_pai: graph.node):
            '''Esvaziar o jarro B'''
            node = graph.node(node_pai.capacidade_a, 0)
            return node

      def regras_to_action(self):
            retorno = []
            for i in range(len(self.regras)):
                  if(self.regras[i] == ['E','A']):
                        retorno.append(self.encher_a)
                  elif(self.regras[i] == ['E','B']):
                        retorno.append(self.encher_b)
                  elif(self.regras[i] == ['A','B']):
                        retorno.append(self.passar_a_para_b)
                  elif(self.regras[i] == ['B','A']):
                        retorno.append(self.passar_b_para_a)
                  elif(self.regras[i] == ['V','A']):
                        retorno.append(self.esvaziar_a)
                  elif(self.regras[i] == ['V','B']):
                        retorno.append(self.esvasiar_b)
                  else:
                        raise AttributeError('Regra inválida')
            return retorno

      def verificacao_regras(self, node_pai: graph.node, graph: graph.graph):
            '''Verifica se a regra aplicada gera um estado valido para ser colocado no grafo'''
            for i in range(len(self.regras)):
                  node = self.regras[i](node_pai)
                  if(not graph.verifica_se_exixte_no_caminho(node, node_pai)):
                        return True
            return False

      def busca_em_profundidade(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, to_string:bool = False):
            '''Busca em profundidade'''
            self.graph = graph.graph("profundidade",capacidade_inicial_a, capacidade_inicial_b)
      
      def busca_em_largura(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, to_string:bool = False):
            '''Busca em largura'''
            self.graph = graph.graph("largura",capacidade_inicial_a, capacidade_inicial_b)

      def busca_em_backtracking(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, to_string:bool = False):
            '''Busca em backtracking'''
            self.graph = graph.graph("backtracking",capacidade_inicial_a, capacidade_inicial_b)