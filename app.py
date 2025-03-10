from flask import Flask, request, render_template
import sqlite3
import heapq  # For priority queue (used in Dijkstra's Algorithm)

app = Flask(__name__)

# Connect to SQLite Database
def get_db_connection():
    conn = sqlite3.connect('locations.db')
    conn.row_factory = sqlite3.Row
    return conn

# Dijkstra's Algorithm to find shortest path
def dijkstra(start, end):
    # Initialize the graph
    conn = get_db_connection()
    edges = conn.execute('SELECT start_node, end_node, distance FROM distances').fetchall()
    conn.close()

    graph = {}
    for edge in edges:
        if edge['start_node'] not in graph:
            graph[edge['start_node']] = []
        graph[edge['start_node']].append((edge['end_node'], edge['distance']))
        if edge['end_node'] not in graph:
            graph[edge['end_node']] = []
        graph[edge['end_node']].append((edge['start_node'], edge['distance']))

    # Priority Queue for Dijkstra (min-heap)
    pq = [(0, start)]  # (distance, node)
    distances = {start: 0}
    previous_nodes = {start: None}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            # Build the path from end to start
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return distances[end], path

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return float("inf"), []  # No path found

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to calculate the distance using Dijkstra
@app.route('/get_distance', methods=['POST'])
def get_distance():
    source = request.form['source']
    destination = request.form['destination']

    # Use Dijkstra's algorithm to find the shortest path
    distance, path = dijkstra(source, destination)
    
    if distance == float("inf"):
        return render_template('result.html', message=f"No path found between {source} and {destination}.", path=None)
    
    return render_template('result.html', 
                           message=f"The shortest distance between {source} and {destination} is {distance} units.", 
                           path=" → ".join(path))

if __name__ == '__main__':
    app.run(debug=True)
