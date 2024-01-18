from ford_fulkerson import Graph
import csv
import sys


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

        # print(graph)
        return graph
    except FileNotFoundError:
        sys.exit("File does not exist")
        

if __name__ == '__main__':
    main()