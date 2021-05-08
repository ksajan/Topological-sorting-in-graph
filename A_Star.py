class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        """
        Returns neighbor of given v node
        """
        return self.adjac_lis[v]

    # This is heuristic function 
    def h(self, n):
        """
        Heuristic function
        Inpup : index (int)
        Output : heuristic cost ( estimated eucledian cost )
        """
        H = {
            'a': 10,
            'b': 7,
            'c': 8,
            'd': 3,
            'e': 2,
            'z': 0
        }
        return H[n]

    def a_star_algorithm(self, start, stop):
        """
        A star algorithm
        Input: start node, Goal node
        Output: Path to the goal node from start node

        Description: 
        We have two list open_list and closed_list. Open list consist nodes 
        which have been visited but neighbours are not visited whereas Closed list 
        contains node which are visited as well as its neighbors are also visited.

        We start with starting node in open list and closed list as empty list.
        """
        open_lst = set([start])
        closed_lst = set([])
        poo = {}
        poo[start] = 0
        par = {}
        par[start] = start
        while len(open_lst) > 0:
            n = None
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v;
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop:
                reconst_path = []
                cost = 0
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
                reconst_path.append(start)
                reconst_path.reverse()
                return reconst_path, poo[stop]
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight # f(n) = g(n) + h(n) 
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
            open_lst.remove(n)
            closed_lst.add(n)
        print('Path does not exist!')
        return None

if __name__ == "__main__":
    adjac_lis = {
        'a': [('b', 4), ('c', 2)],
        'b': [('a', 4), ('d', 5), ('c', 1)],
        'c': [('a', 2), ('d', 8), ('b', 1), ('e', 10)],
        'd': [('b', 5), ('c', 8), ('e', 2), ('z', 6)],
        'e': [('c', 10), ('d', 2), ('z', 5)],
        'z': [('d', 6), ('e', 5)]
    }

    graph = Graph(adjac_lis)
    start, goal = map(str, input().split())
    path, cost = graph.a_star_algorithm(start, goal)
    if path:
        print('Path found from node {} to node {}'.format(start, goal))
        print('Path: {} with cost {}'.format(path, cost))