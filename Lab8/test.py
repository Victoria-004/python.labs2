import unittest
from task import *

class TestEdmondsKarp(unittest.TestCase):
    def test_csv(self):
        graph = {}
        capacity = {}
        filename = 'roads.csv'

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                farms = [x.strip() for x in file.readline().split(',')]
                shops = [x.strip() for x in file.readline().split(',')]

                for line in file:
                    parts = [x.strip() for x in line.split(',')]
                    if len(parts) == 3:
                        u, v, cap = parts[0], parts[1], int(parts[2])
                        if u not in graph:
                            graph[u] = []
                        if v not in graph:
                            graph[v] = []
                        graph[u].append(v)
                        graph[v].append(u)
                        capacity[(u, v)] = cap
                        capacity[(v, u)] = capacity.get((v, u), 0)

            source = 'SOURCE'
            sink = 'SINK'
            graph[source] = []
            graph[sink] = []

            for farm in farms:
                graph[source].append(farm)
                graph[farm].append(source)
                capacity[(source, farm)] = float('inf')
                capacity[(farm, source)] = 0

            for shop in shops:
                graph[shop].append(sink)
                graph[sink].append(shop)
                capacity[(shop, sink)] = float('inf')
                capacity[(sink, shop)] = 0

            result = edmonds_karp(graph, capacity, source, sink)
            self.assertEqual(result, 11)

        except FileNotFoundError:
            self.fail("Test CSV file 'roads.csv' not found.")

if __name__ == '__main__':
    unittest.main()
