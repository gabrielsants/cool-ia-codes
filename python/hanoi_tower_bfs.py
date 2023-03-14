import copy, os, time, sys

nodes_explored = 0

def list_pool(pools):
    pool_list = []
    for pool in pools:
        temp = []
        for disk in pool:
            temp.append(disk.disk_ind)
        pool_list.append(temp)
        
    return pool_list

def moving(p_s, p_f, pools):
    global nodes_explored
    new_pools = copy.deepcopy(pools)
    valid = False
    if len(new_pools[p_s]) > 0:
        if len(new_pools[p_f]) == 0:
            new_pools[p_f].append(new_pools[p_s][-1])
            new_pools[p_s] = new_pools[p_s][:-1]
            valid = True
        else:
            if new_pools[p_s][-1] < new_pools[p_f][-1]:
                new_pools[p_f].append(new_pools[p_s][-1])
                new_pools[p_s] = new_pools[p_s][:-1]
                valid = True
    if valid:
        nodes_explored += 1
    return new_pools, valid

def BFS(pool_stat, N, canDraw):
    global nodes_explored
    nodes_explored = 0
    searching = [(pool_stat, [])]
    searched = [pool_stat]
    
    while True:
        pool_stat, hist = searching[0]
        if len(pool_stat[2]) == N or len(pool_stat[1]) == N:
            break
        searching = searching[1:]
        for p_s in range(3):
            for p_f in range(3):
                if p_s != p_f:
                    new_pools, valid = moving(p_s, p_f, pool_stat)
                    if valid:
                        if new_pools not in searched:
                            searching.append((new_pools, hist+[(p_s, p_f)]))
                            searched.append(new_pools)
        if canDraw:
            draw(searched)                    
    return hist 

def draw(searched):
    for pool in searched[-1]:
        print(pool)
    print("#########################################")
    
def wellcome():
    print("Welcome! This is a program to solve Hanoi Tower problem using BFS.")
    print("Enter a value of disks between 3 and 5\n$ > ", end="")
    N = int(input())
    while True:
        if(N < 3 or N > 5):
            clear_screen()
            print("Enter a value of disks between 3 and 5\n$ > ",end="")
            N = int(input())
        else:
            break;
    return N

def clear_screen():
    if(os.name == "posix"):
        os.system('clear')
    else:
        os.system('cls')

def manualInit():
    pools = []
    pools.append([])
    pools.append([])
    pools.append([])
    N = wellcome()
    for i in range(N):
        pools[0].append(N-i)
    BFS(pools, N, True)

def autoInit(N):
    start_time = time.time()
    pools = []
    pools.append([])
    pools.append([])
    pools.append([])
    for i in range(N):
        pools[0].append(N-i)
    BFS(pools, N, False)
    end_time = time.time()
    print('-----------------------------------------------------------')
    print("| ! Runtime:", end_time - start_time, "seconds.")
    print(f"| ! {nodes_explored} nodes explored")
    print('-----------------------------------------------------------')

if __name__ == "__main__":
    clear_screen()
    if(len(sys.argv) > 1):
        autoInit(int(sys.argv[1]))
    else:
        manualInit()
        print('-----------------------------------------------------------')
        print(f"| ! {nodes_explored} nodes explored")
        print('-----------------------------------------------------------')
