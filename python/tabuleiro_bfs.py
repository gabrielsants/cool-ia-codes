from collections import deque
import random
import os

def is_goal(state):
    return state == [None, 'A', 'A', 'V', 'V'] or \
               state == ['A', None, 'A', 'V', 'V'] or \
               state == ['A', 'A', None, 'V', 'V'] or \
               state == ['A', 'A', 'V', None, 'V'] or \
               state == ['A', 'A', 'V', 'V', None]

def get_path(node):
    # Retorna a lista de estados percorridos até o estado atual
    path = [node['state']]
    while node['parent'] is not None:
        node = node['parent']
        path.append(node['state'])
    return path[::-1]

def get_successors(state):
    # Retorna a lista de estados sucessores do estado atual
    successors = []
    empty_index = state.index(None)
    for i, block in enumerate(state):
        if i != empty_index:
            new_state = state.copy()
            new_state[empty_index] = block
            new_state[i] = None
            successors.append(new_state)
    return successors

def bfs(initial_state):
    # Define o estado inicial como um dicionário com os atributos 'state' e 'parent'
    initial_node = {'state': initial_state, 'parent': None}

    # Cria a fila de estados a serem explorados
    frontier = deque([initial_node])

    # Cria um conjunto para armazenar os estados já visitados
    explored = set()

    # Enquanto houver estados na fila de fronteira
    while frontier:
        # Remove o primeiro estado da fila de fronteira
        node = frontier.popleft()
        state = node['state']

        # Se o estado atual for o objetivo, retorna o caminho percorrido até o objetivo
        if is_goal(state):
            return get_path(node)

        # Adiciona o estado atual ao conjunto de estados já visitados
        explored.add(tuple(state))

        # Gera os estados sucessores do estado atual
        for successor_state in get_successors(state):
            # Se o estado sucessor ainda não foi visitado, adiciona-o à fila de fronteira
            if tuple(successor_state) not in explored:
                successor_node = {'state': successor_state, 'parent': node}
                frontier.append(successor_node)

    # Se a fila de fronteira estiver vazia e o objetivo não tiver sido encontrado, retorna None
    return None

def random_input():
    vetor = ['V', 'V', 'A', 'A',None]
    random.shuffle(vetor)
    return vetor

if __name__ == "__main__":
    # Define a entrada como estado inicial -- podes adicionar uma entrada com input randomico
    if(os.name == "posix"):
        os.system('clear')
    else:
        os.ystem('cls')
    initial_state = random_input()
    print(f"Estado inicial\n{initial_state}\n")
    # Executa o algoritmo BFS
    result = bfs(initial_state)
    
    # Verifica se o objetivo foi encontrado e imprime o caminho percorrido se for o caso
    if result:
        print('Caminho até a solução:')
        for state in result:
            print(state)
        print(result[-1])
    else:
        print('Não foi possível encontrar uma solução.')