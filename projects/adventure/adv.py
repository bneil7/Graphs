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
# map_file = "maps/test_line.txt"
# - shortest is 2
# map_file = "maps/test_cross.txt"
# - shortest is 14
# map_file = "maps/test_loop.txt"
# - shortest is 14
# map_file = "maps/test_loop_fork.txt"
# - shortest is 24
map_file = "maps/main_maze.txt"
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

# add current path if dead end
dead_end_path = []

# function to gather directions in an unexplored exit


def unexplored_exit_directions():
    for direction in traversal_graph[player.current_room.id]:
        print(direction, "<-- DIRECTION")
        if traversal_graph[player.current_room.id][direction] == "?":
            return direction


# step counter
steps = 0

# traverse the entire length of the graph
while len(traversal_graph) < len(room_graph):

    # show exits in current room
    exits = player.current_room.get_exits()

    # add current room and exits to traversal graph
    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
        # loop thru cardinal directions in exits and add "?" to indicate they're unexplored
        for direction in exits:
            traversal_graph[player.current_room.id][direction] = "?"

    # if coming from prev room, update current and prev room with direction opposites
    if prev_room is not None:
        traversal_graph[prev_room][prev_direction] = player.current_room.id
        traversal_graph[player.current_room.id][opp_direction[prev_direction]] = prev_room

    # if all rooms visited, break
    if len(traversal_graph) == len(room_graph):
        break

    # get first unexplored room
    direction = unexplored_exit_directions()

    if direction:
        traversal_path.append(direction)
        dead_end_path.append(opp_direction[direction])
        prev_room = player.current_room.id
        prev_direction = direction
        player.travel(direction)
        traversal_graph[prev_room][direction] = player.current_room.id
        # increment step counter
        steps += 1
    # else, if no "?" in current room exits, turn around and traverse until "?" is found in new room
    else:
        while direction is None:
            if len(dead_end_path) == 0:
                break
            # get last direction in path
            old_direction = dead_end_path.pop()
            traversal_path.append(old_direction)
            player.travel(old_direction)
            print(direction, "<< SHOULD BE OLD DIRECTION")
            direction = unexplored_exit_directions()
            # increment step counter
            steps += 1
        if len(dead_end_path) == 0:
            dead_end_path = []
            # then reset previous trackers
        prev_room = None
        prev_direction = None


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
