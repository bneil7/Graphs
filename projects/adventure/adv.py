from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)
# stolen from ../graph/util.py


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)
# stolen from ../graph/util.py


# Load world
world = World()

# using BFS and DFT to reach every node (room in this case)

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# - shortest is 2
# map_file = "maps/test_cross.txt"
# - shortest is 14
# map_file = "maps/test_loop.txt"
# - shortest is 14
# map_file = "maps/test_loop_fork.txt"
# - shortest is 24
# map_file = "maps/main_maze.txt"
# largest graph - shortest is 918
# MUST PASS IN LESS THAN 2000 STEPS (should only take a few seconds at most tbh)

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# add N, S, E, W directions for moving between rooms
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}

# initiate variables to hold values of previous rooms and directions
prev_room = None
prev_direction = None

# dict to hold values of each cardinal direction's corresponding opposite
opp_direction = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e"
}

# Commands:
# player.current_room.id,
# player.current_room.get_exits()
# player.travel(direction)

# traverse the entire length of the graph
while len(traversal_graph) < len(room_graph):
    # print(player.current_room.id)
    # print("---")
    # print(traversal_graph, "<-- traversal graph")
    # print("---")
    # print(traversal_path, "<-- traversal path")

    # show exits in current room
    exits = player.current_room.get_exits()

    # if all rooms visited, break
    if len(traversal_graph) == len(room_graph):
        break

    # add current room and exits to traversal graph
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
        # loop thru cardinal directions in exits and add "?"
        for direction in exits:
            traversal_graph[player.current_room.id][direction] = "?"

    # get first unexplored room
    for direction in traversal_graph[player.current_room.id]:
        if traversal_graph[player.current_room.id][direction] == "?":
            traversal_path.append(direction)
            prev_room = player.current_room.id
            player.travel(direction)
            traversal_graph[prev_room][direction] = player.current_room.id
        break


print(traversal_graph, "<-- traversal graph")
print("---")
print(traversal_path, "<-- traversal path")


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
