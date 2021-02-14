import pandas as pd
# from Graph import Graph
from SmrtVertex import Vertex
from SmrtGraph import Graph


def readCSV(filename, src):
    df = pd.read_csv(filename)
    graph = Graph(directed=True)
    prevstation = -1
    for index, row in df.iterrows():
        currstation = Vertex(row['Station Name'], row['Station Code'])
        if prevstation != -1 and prevstation.code[0:1] == currstation.code[0:1]:
            graph.add(prevstation, currstation)
        if prevstation != -1:
            print("Is Previous Station:" + str(prevstation) + " connected to current station:" + str(currstation) + " "+str(
                graph.is_connected(prevstation, currstation)))
        prevstation = currstation
    print("Finding shortest path from " + str(src))
    graph.dijkstra(src)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    source = input("enter source station name:")
    readCSV('datasource/StationMap.csv', Vertex(source, -1))
