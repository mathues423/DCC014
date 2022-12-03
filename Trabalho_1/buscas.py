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
            self.action = self.__regras_to_action()
            self.objetivo_jarro_a = objetivo_jarro_a
            self.objetivo_jarro_b = objetivo_jarro_b
            self.graph = None
      
      def __encher_a(self, node_pai: graph.node) -> graph.node:
            '''Encher o jarro A'''
            node = graph.node(5, node_pai.capacidade_b)
            return node

      def __encher_b(self, node_pai: graph.node) -> graph.node:
            '''Encher o jarro B'''
            node = graph.node(node_pai.capacidade_a, 3)
            return node

      def __passar_a_para_b(self, node_pai: graph.node) -> graph.node:
            '''Passar a água do jarro A para o jarro B'''
            if(node_pai.capacidade_a + node_pai.capacidade_b > 3):
                  node = graph.node(node_pai.capacidade_a - (3 - node_pai.capacidade_b), 3)
            else:
                  node = graph.node(0, node_pai.capacidade_a + node_pai.capacidade_b)
            return node
      
      def __passar_b_para_a(self, node_pai: graph.node) -> graph.node:
            '''Passar a água do jarro B para o jarro A'''
            if(node_pai.capacidade_a + node_pai.capacidade_b > 5):
                  node = graph.node(5, node_pai.capacidade_b - (5 - node_pai.capacidade_a))
            else:
                  node = graph.node(node_pai.capacidade_a + node_pai.capacidade_b, 0)
            return node

      def __esvaziar_a(self, node_pai: graph.node) -> graph.node:
            '''Esvaziar o jarro A'''
            node = graph.node(0, node_pai.capacidade_b)
            return node

      def __esvasiar_b(self, node_pai: graph.node) -> graph.node:
            '''Esvaziar o jarro B'''
            node = graph.node(node_pai.capacidade_a, 0)
            return node

      def __regras_to_action(self) -> list:
            retorno = []
            for i in range(len(self.regras)):
                  if(self.regras[i] == ['E','A']):
                        retorno.append(self.__encher_a)
                  elif(self.regras[i] == ['E','B']):
                        retorno.append(self.__encher_b)
                  elif(self.regras[i] == ['A','B']):
                        retorno.append(self.__passar_a_para_b)
                  elif(self.regras[i] == ['B','A']):
                        retorno.append(self.__passar_b_para_a)
                  elif(self.regras[i] == ['V','A']):
                        retorno.append(self.__esvaziar_a)
                  elif(self.regras[i] == ['V','B']):
                        retorno.append(self.__esvasiar_b)
                  else:
                        raise AttributeError('Regra inválida')
            return retorno

      def regras_to_string(self) -> str:
            retorno = ''
            for i in range(len(self.regras)):
                  retorno += 'Regra nº '
                  if(self.regras[i] == ['E','A']):
                        retorno += str(i+1)+' Encher o jarro A\n'
                  elif(self.regras[i] == ['E','B']):
                        retorno += str(i+1)+' Encher o jarro B\n'
                  elif(self.regras[i] == ['A','B']):
                        retorno += str(i+1)+' Passar a água do jarro A para o jarro B\n'
                  elif(self.regras[i] == ['B','A']):
                        retorno += str(i+1)+' Passar a água do jarro B para o jarro A\n'
                  elif(self.regras[i] == ['V','A']):
                        retorno += str(i+1)+' Esvaziar o jarro A\n'
                  elif(self.regras[i] == ['V','B']):
                        retorno += str(i+1)+' Esvaziar o jarro B\n'
            return retorno

      def __verificacao_regras(self, node_pai: graph.node) -> bool:
            '''Verifica se a regra aplicada gera um estado valido para ser colocado no grafo'''
            for i in range(len(self.regras)):
                  node = self.action[i](node_pai)
                  if(not self.graph.verifica_se_exixte_no_caminho(node, node_pai) and not self.__igual_visinhanca(node, node_pai)):
                        return True
            return False

      def __add_node_to_graph(self, node_pai: graph.node) -> graph.node:
            if(self.__verificacao_regras(node_pai)):
                  for i in range(len(self.regras)):
                        node = self.action[i](node_pai)
                        if(not self.graph.verifica_se_exixte_no_caminho(node, node_pai) and not self.__igual_visinhanca(node, node_pai)):
                              return node

      def __igual_visinhanca(self, node: graph.node, node_pai: graph.node) -> bool:
            if(node_pai.filhos == []):
                  return False
            else:
                  for auxiliar in range(len(node_pai.filhos)):
                        if(node_pai.filhos[auxiliar].capacidade_b == node.capacidade_b and node_pai.filhos[auxiliar].capacidade_a == node.capacidade_a and node_pai.filhos[auxiliar] != node):
                              return True
                  return False

      def __saida_srt__(self, graph :graph.graph, iteracoes: str = None) -> str:
            retorno_str = '\n'
            retorno_str += 'Busca('+graph.tipo+') com a sequinte ordem de regras:\n'
            retorno_str += self.regras_to_string()
            retorno_str += '-'*50 + '\n'
            if(iteracoes != None):
                  retorno_str += iteracoes
            return retorno_str

      def busca_em_profundidade(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, to_string:bool = False) -> graph.graph:
            '''Busca em profundidade'''
            self.graph = None
            self.graph = graph.graph("profundidade",capacidade_inicial_a, capacidade_inicial_b)


      def busca_em_largura(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, to_string:bool = False) -> graph.graph:
            '''Busca em largura'''
            self.graph = None
            self.graph = graph.graph("largura",capacidade_inicial_a, capacidade_inicial_b)

            lista_abertos = [self.graph.raiz]
            lista_canditados_fila = [self.graph.raiz]
            lista_fechados = []
            variavel_controle = self.graph.raiz
            contador_iteracao = 1
            retorno_str = ''

            while(variavel_controle.capacidade_a != self.objetivo_jarro_a):
                  variavel_controle = lista_canditados_fila[0]

                  ### Str de interação
                  retorno_str += 'Iteração nº '+str(contador_iteracao) + '\n'
                  retorno_str += 'Lista de abertos:' 
                  for i in range(len(lista_abertos)):
                        retorno_str += ('{} '.format(lista_abertos[i]))
                  retorno_str += '\nLista de fechados: '
                  for i in range(len(lista_fechados)):
                        retorno_str += ('{} '.format(lista_fechados[i]))
                  retorno_str += '\nEstado atual: {}'.format(lista_canditados_fila[0])
                  retorno_str += '\n'
                  retorno_str += '-'*50 + '\n'

                  contador_peso_no = contador_iteracao
                 
                  while(self.__verificacao_regras(variavel_controle)):
                        node = self.__add_node_to_graph(variavel_controle)
                        node.set_peso(contador_peso_no + contador_iteracao)
                        variavel_controle.add_filho(node)
                        lista_abertos.append(node)
                        lista_canditados_fila.append(node)
                        contador_peso_no += 1

                  aux = lista_abertos.pop(0)
                  lista_fechados.append(aux)
                  lista_canditados_fila.remove(aux)
                              
                  lista_canditados_fila.sort(key=lambda x: x.peso)
                  contador_iteracao += 1
                  
            if(to_string):
                  print(self.__saida_srt__(self.graph, retorno_str))

            return self.graph

      def busca_em_backtracking(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, to_string:bool = False) -> graph.graph:
            '''Busca em backtracking'''
            self.graph = None
            self.graph = graph.graph("backtracking",capacidade_inicial_a, capacidade_inicial_b)

            lista_abertos = [self.graph.raiz]
            lista_fechados = []
            variavel_controle = self.graph.raiz
            contador_iteracao = 1
            retorno_str = ''

            while(variavel_controle.capacidade_a != self.objetivo_jarro_a):
                  variavel_controle = lista_abertos[-1]

                  ### Str de interação
                  retorno_str += 'Iteração nº '+str(contador_iteracao) + '\n'
                  retorno_str += 'Lista de abertos:' 
                  for i in range(len(lista_abertos)):
                        retorno_str += ('{} '.format(lista_abertos[i]))
                  retorno_str += '\nLista de fechados: '
                  for i in range(len(lista_fechados)):
                        retorno_str += ('{} '.format(lista_fechados[i]))
                  retorno_str += '\nEstado atual: {}'.format(lista_abertos[-1])
                  retorno_str += '\n'
                  retorno_str += '-'*50 + '\n'

                  if(self.__verificacao_regras(variavel_controle)):
                        node = self.__add_node_to_graph(variavel_controle)
                        variavel_controle.add_filho(node)
                        lista_abertos.append(node)
                  else:
                        lista_fechados.append(lista_abertos.pop(-1))

                  contador_iteracao += 1

            if(to_string):
                  print(self.__saida_srt__(self.graph, retorno_str))

            return self.graph