"""

"""
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
      def __init__(self, regras: 'list[list[str]]', objetivo_jarro_a:int=None, objetivo_jarro_b:int=None):
            if(len(regras) != 6):
                  raise AttributeError('O número de regras deve ser 6')
            self.regras = regras
            self.action = self.__regras_to_action()
            self.objetivo_jarro_a = objetivo_jarro_a
            self.objetivo_jarro_b = objetivo_jarro_b
            self.graph = graph.graph('Não inicializado')
      
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
            for regra in self.regras:
                  if(regra == ['E','A']):
                        retorno.append(self.__encher_a)
                  elif(regra == ['E','B']):
                        retorno.append(self.__encher_b)
                  elif(regra == ['A','B']):
                        retorno.append(self.__passar_a_para_b)
                  elif(regra == ['B','A']):
                        retorno.append(self.__passar_b_para_a)
                  elif(regra == ['V','A']):
                        retorno.append(self.__esvaziar_a)
                  elif(regra == ['V','B']):
                        retorno.append(self.__esvasiar_b)
                  else:
                        raise AttributeError('Regra inválida')
            return retorno

      def regras_string_passos(self) -> str:
            retorno = ''
            for index, regra in enumerate(self.regras):
                  retorno += 'Regra nº '
                  if(regra == ['E','A']):
                        retorno += str(index+1)+' Encher o jarro A\n'
                  elif(regra == ['E','B']):
                        retorno += str(index+1)+' Encher o jarro B\n'
                  elif(regra == ['A','B']):
                        retorno += str(index+1)+' Passar a água do jarro A para o jarro B\n'
                  elif(regra == ['B','A']):
                        retorno += str(index+1)+' Passar a água do jarro B para o jarro A\n'
                  elif(regra == ['V','A']):
                        retorno += str(index+1)+' Esvaziar o jarro A\n'
                  elif(regra == ['V','B']):
                        retorno += str(index+1)+' Esvaziar o jarro B\n'
            return retorno

      def __verificacao_regras(self, node_pai: graph.node) -> bool:
            '''Verifica se a regra aplicada gera um estado valido para ser colocado no grafo'''
            for regra in self.action:
                  node = regra(node_pai)
                  if(not self.graph.__verifica_se_exixte_no_caminho__(node, node_pai) and not self.__igual_visinhanca(node, node_pai)):
                        return True
            return False

      def __creat_node_to_graph(self, node_pai: graph.node) -> graph.node:
            if(self.__verificacao_regras(node_pai)):
                  for regra in self.action:
                        node = regra(node_pai)
                        if(not self.graph.__verifica_se_exixte_no_caminho__(node, node_pai) and not self.__igual_visinhanca(node, node_pai)):
                              return node

      def __igual_visinhanca(self, node: graph.node, node_pai: graph.node) -> bool:
            if(node_pai.filhos == []):
                  return False
            else:
                  for auxiliar in node_pai.filhos:
                        if(auxiliar.capacidade_b == node.capacidade_b and auxiliar.capacidade_a == node.capacidade_a and auxiliar != node):
                              return True
                  return False

      def __saida_srt__(self, graph :graph.graph, iteracoes: str = None) -> str:
            retorno_str = '\n'
            retorno_str += 'Busca('+graph.tipo+') com a sequinte ordem de regras:\n'
            retorno_str += self.regras_string_passos()
            retorno_str += '-'*50 + '\n'
            if(iteracoes != None):
                  retorno_str += iteracoes
            retorno_str += 'Grafo gerado:\n'
            retorno_str += graph.__str__()
            return retorno_str
      
      def __saida_intermediaria_str__(self, abertos:list, fechados:list, atual:graph.node, n_iteracao: int) -> str:
            retorno = 'Iteração nº '+str(n_iteracao) + '\n'
            retorno += 'Lista de abertos:'
            for node in abertos:
                  retorno += ('{} '.format(node))
            retorno += '\nLista de fechados: '
            for node in fechados:
                  retorno += ('{} '.format(node))
            retorno += '\nEstado atual: ' + str(atual) + '\n'
            retorno += '-'*50 + '\n'
            return retorno

      def __verifica_poda(self, node: graph.node, lista_no_adicionada: 'list[graph.node]') -> bool:
            '''Verifica se o no pode ser adicionado na lista de abertos'''
            for node_aux in lista_no_adicionada:
                  if(node_aux.capacidade_a == node.capacidade_a and node_aux.capacidade_b == node.capacidade_b
                  and node_aux.get_altura() >= node.get_altura()):
                        return True
            return False

      def __poda__(self,node_criado: graph.node, lista_abertos: 'list[graph.node]',lista_fechados: 'list[graph.node]', lista_candidatos: 'list[graph.node]' = None) -> 'list[list[graph.node]]':
            '''Remove os nos que podem ser podados'''
            for index, node in enumerate(lista_abertos):
                  if(node.capacidade_a == node_criado.capacidade_a and node.capacidade_b == node_criado.capacidade_b and node.get_altura() >= node_criado.get_altura()):
                        aux = lista_abertos.pop(index)
                        if(lista_candidatos != None):
                              if(aux in lista_candidatos):
                                    lista_candidatos.remove(aux)
                              
                        lista_fechados.append(aux)
                        break

            if(lista_candidatos != None):
                  return [lista_abertos, lista_fechados, lista_candidatos]
            else:
                  return [lista_abertos, lista_fechados]

      def busca_em_profundidade(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, verbose:bool = False) -> graph.graph:
            '''Busca em profundidade'''
            self.graph = None
            self.graph = graph.graph("profundidade",capacidade_inicial_a, capacidade_inicial_b)

            lista_abertos = [self.graph.raiz]
            lista_canditados_pilha = [self.graph.raiz]
            lista_fechados = []
            variavel_controle = self.graph.raiz
            contador_iteracao = 1
            retorno_str = ''

            while(variavel_controle.capacidade_a != self.objetivo_jarro_a):
                  variavel_controle = lista_canditados_pilha[-1]

                  ### Str de interação
                  retorno_str += self.__saida_intermediaria_str__(lista_abertos, lista_fechados, variavel_controle, contador_iteracao)
                  if(variavel_controle.capacidade_a == self.objetivo_jarro_a):
                        self.graph.add_node_resposta(variavel_controle)
                        break

                  while(self.__verificacao_regras(variavel_controle)):
                        node = self.__creat_node_to_graph(variavel_controle)
                        if(self.__verifica_poda(node, lista_abertos)):
                              lista_canditados_pilha, lista_fechados, lista_abertos = self.__poda__(node, lista_canditados_pilha, lista_fechados, lista_abertos)
                        
                        variavel_controle.add_filho(node)
                        lista_abertos.append(node)
                        lista_canditados_pilha.append(node)
                        
                  lista_canditados_pilha.pop(0)
                  lista_fechados.append(variavel_controle)
                  if variavel_controle in lista_abertos:
                        lista_abertos.remove(variavel_controle)
                  
                  lista_canditados_pilha.sort(key=lambda x: x.get_altura())
                  contador_iteracao += 1
                  
            if(verbose):
                  print(self.__saida_srt__(self.graph, retorno_str))

            return self.graph

      def busca_em_largura(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, verbose:bool = False) -> graph.graph:
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
                  retorno_str += self.__saida_intermediaria_str__(lista_abertos, lista_fechados, variavel_controle, contador_iteracao)
                  if(variavel_controle.capacidade_a == self.objetivo_jarro_a):
                        self.graph.add_node_resposta(variavel_controle)
                        break

                  while(self.__verificacao_regras(variavel_controle)):
                        node = self.__creat_node_to_graph(variavel_controle)
                        if(self.__verifica_poda(node, lista_abertos)):
                              lista_abertos, lista_fechados, lista_canditados_fila = self.__poda__(node, lista_abertos, lista_fechados, lista_canditados_fila)
                        
                        variavel_controle.add_filho(node)
                        lista_abertos.append(node)
                        lista_canditados_fila.append(node)
                          
                  aux = lista_abertos.pop(0)
                  lista_fechados.append(aux)
                  if(aux in lista_canditados_fila):
                        lista_canditados_fila.remove(aux)
                  
                  lista_canditados_fila.sort(key=lambda x: x.get_altura())
                  contador_iteracao += 1
                  
            if(verbose):
                  print(self.__saida_srt__(self.graph, retorno_str))

            return self.graph

      def busca_em_backtracking(self, capacidade_inicial_a:int = 0, capacidade_inicial_b:int = 0, verbose:bool = False) -> graph.graph:
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
                  retorno_str += self.__saida_intermediaria_str__(lista_abertos, lista_fechados, variavel_controle, contador_iteracao)
                  if(variavel_controle.capacidade_a == self.objetivo_jarro_a):
                        self.graph.add_node_resposta(variavel_controle)
                        break
                  
                  if(self.__verificacao_regras(variavel_controle)):
                        node = self.__creat_node_to_graph(variavel_controle)
                        variavel_controle.add_filho(node)
                        lista_abertos.append(node)
                  else:
                        lista_fechados.append(lista_abertos.pop(-1))

                  contador_iteracao += 1

            if(verbose):
                  print(self.__saida_srt__(self.graph, retorno_str))

            return self.graph