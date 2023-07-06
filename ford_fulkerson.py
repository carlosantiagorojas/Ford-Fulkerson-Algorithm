import csv
import sys
import numpy as np

def main():
    if len(sys.argv[1:]) == 3:
        if verify_input(sys.argv[1], sys.argv[2], sys.argv[3]):
            
            graph = Graph(read_csv(sys.argv[1]))
            result = graph.ford_fulkerson(int(sys.argv[2]), int(sys.argv[3]))
            
            if result == 0:
                print("Can't be found the maximum flow")
            else:
                print(f"The maximum flow is: {result}")

    elif len(sys.argv[1:]) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


class Graph:
    """
    A class to represent a graph.

    Attributes:
        graph: A 2D list representing the graph
        resGraph: A 2D list representing the residual graph of flow

    Methods:
        __init__(self, graph):
            Initialize the graph
        BFS(self, source, sink, vertices):
            Do the Breadth First Search in the graph
        ford_fulkerson(self, source, sink):
            Finds the maximum flow in the graph
    """
    def __init__(self, graph):
        self.graph = graph
        # Create another array of zeros with the shape and type of the graph
        self.resGraph = np.zeros_like(self.graph)

    # Function to display the graph
    def print_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end="\t")
            print()

    # Function to apply BFS
    def BFS(self, source, sink, vertices):
        # Visited nodes array
        visited = [False] * len(self.graph)
        queue = []
        # The start vertex is placed at the beginning of the queue and is placed as visited
        queue.append(source)
        visited[source] = True

        # While the queue is not empty
        while queue:
            #print(queue)
            #print(visited)
            
            # Read the current vertex
            vertex = queue.pop(0)
            # print(f"[{vertex}]", end=" ")

            # If the destination vertex is reached
            if vertex == sink:
                return True
            
            #print(self.graph[vertex])
            # Go through the edges of the current vertex
            for ind, val in enumerate(self.graph[vertex]):
                # If adjacent vertices are unvisited and have capacity
                if visited[ind] == False and val > 0:
                    # Add the vertex to the queue and mark it as visited
                    queue.append(ind)
                    visited[ind] = True
                    # The current vertex is placed as its predecessor
                    vertices[ind] = vertex

        return False

    def ford_fulkerson(self, source, sink):
        max_flow = 0
        vertices = [-1] * len(self.graph)

        # As long as there are paths from the start source to the destination sink
        while self.BFS(source, sink, vertices):

            # print(vertices)
            # Set a variable to save the track of the current flow
            # Save the index of the sink
            curr_flow = float('inf')
            vertex_ind = sink

            # Traversing the path from the destination vertex to the source vertex
            while vertex_ind != source:
                # print(vertex_ind)
                
                # The graph is traversed according to the path and it is determined which is the maximum flow
                curr_flow = min(curr_flow, self.graph[vertices[vertex_ind]][vertex_ind])
                #print(self.graph[vertices[vertex_ind]][vertex_ind])
                
                # Look at the predecessor vertex until founds the source
                vertex_ind = vertices[vertex_ind]

            # Do the same but now set the values of the residual graph with the maximum flow found previously
            res_ind = sink
            while res_ind != source:
                # The value of the maximum flow previously found is placed in the residual graph
                self.resGraph[vertices[res_ind]][res_ind] = curr_flow
                
                res_ind = vertices[res_ind]

            print("\nResidual graph:")
            self.print_matrix(self.resGraph)
            print("\nMain graph:")

            # The graph is subtracted with the residual graph that has the maximum flow in the edges of the flow
            self.graph = np.subtract(self.graph, self.resGraph)
            self.print_matrix(self.graph)

            # Set the residual matrix to 0
            self.resGraph = np.zeros_like(self.graph)

            # The longest flow of the path is added to the total to find the maximum flow
            max_flow += curr_flow

        return max_flow


def verify_input(file_name, source, sink):
    """
    Verify that the input is a csv file and the source and sink are integers
    
    Raises:
        ValuerError: If the source or the sink is a string
    """
    if file_name.endswith(".csv"):
        try:
            int(source)
            int(sink)

            return True
        except ValueError:
            sys.exit("The source and sink has to be a number")
    else:
        sys.exit("Not a csv file")


def read_csv(filename):
    """
    Reads a CSV file and returns a graph represented as a 2D list.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            
            graph = []
            for row in reader:
                node_relations = []
                for element in row:
                    # read each element of the row and converted the string to integer
                    node_relations.append(int(element))
                # add the relations of a node as a list to the graph
                graph.append(node_relations)
            
        #print(graph)
        return graph
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == '__main__':
    main()
