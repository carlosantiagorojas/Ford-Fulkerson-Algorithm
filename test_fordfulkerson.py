from ford_fulkerson import Graph, read_csv

def test_example():
    graph = Graph(read_csv("example.csv"))
    assert graph.ford_fulkerson(0, 5) == 195

def test_example2():
    graph = Graph(read_csv("example2.csv"))
    assert graph.ford_fulkerson(0, 8) == 6

def test_example3():
    graph = Graph(read_csv("example3.csv"))
    assert graph.ford_fulkerson(0, 31) == 27
