import time, sys

def hanoi_dfs(n, source, target, aux, moves):
    if n == 1:
        moves += 1
        print("Move disk 1 from source", source, "to target", target)
        return moves
    moves = hanoi_dfs(n-1, source, aux, target, moves)
    moves += 1
    print("Move disk", n, "from source", source, "to target", target)
    moves = hanoi_dfs(n-1, aux, target, source, moves)
    return moves

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        disks = int(sys.argv[1])
    else:
        disks = 5

    moves = 0
    start_time = time.time()
    # executa a função com as hastes de origem, destino e auxiliar
    moves = hanoi_dfs(disks, 'A', 'C', 'B', moves)
    print('-----------------------------------------------------------')
    print("| ! Runtime:", time.time() - start_time, "seconds.")
    print(f"| ! Number of moves: {moves}.")
    print('-----------------------------------------------------------')
