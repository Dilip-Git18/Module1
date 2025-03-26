# Dijkstra's Shortest Path Finder

This project is a web application built with Flask, which allows users to calculate the shortest distance between two locations using **Dijkstra's Algorithm**. The application fetches data from an **SQLite** database that contains a graph of locations and their connecting distances. It displays the result and the path from the source location to the destination.

## Features

- **Web Interface**: Simple and intuitive form to enter source and destination locations.
- **Dijkstra's Algorithm**: Efficient algorithm to compute the shortest path between two nodes in a graph.
- **SQLite Database**: Stores the graph of locations and their distances, which is queried for calculating the shortest path.
- **Real-Time Results**: Calculates and displays the shortest distance and the path in real-time.

## Technologies Used

- **Flask**: Python web framework for building the application.
- **SQLite**: Lightweight relational database used to store location data.
- **Dijkstra's Algorithm**: Algorithm to find the shortest path between two nodes in a graph.
- **HTML/CSS**: Frontend design to create the user interface.

## Installation

Follow these steps to run the project locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/dijkstra-shortest-path-finder.git

2. You can open the locations.db or dehradun.db file in a tool like DB Browser for SQLite to view or modify the data.

3. Open a web browser and go to:
   ```bash
   http://127.0.0.1:5000/
