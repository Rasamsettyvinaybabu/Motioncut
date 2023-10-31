import random

current_location = "start"

world = {
    "start": {
        "description": "You are at the entrance of a dark forest. A path leads further in.",
        "paths": {"in": "forest"},
    },
    "forest": {
        "description": "You are in the dense forest. There are three paths: left, right, and straight ahead.",
        "paths": {"left": "cave", "right": "river", "straight": "clearing"},
    },
    "cave": {
        "description": "You entered a cave. It's dark and damp. You see two tunnels.",
        "paths": {"left": "treasure", "right": "dead_end"},
    },
    "river": {
        "description": "You arrived at a fast-flowing river. You need to cross it to continue.",
        "paths": {"cross": "clearing", "turn back": "forest"},
    },
    "clearing": {
        "description": "You found a beautiful clearing. There's a chest here.",
        "paths": {"open chest": "treasure", "continue": "end"},
    },
    "treasure": {
        "description": "You found a treasure chest filled with gold! You've won the game.",
    },
    "dead_end": {
        "description": "You reached a dead end. Time to turn back.",
        "paths": {"turn back": "cave"},
    },
    "end": {
        "description": "Congratulations! You have completed the adventure!",
    },
}

# Game loop
while current_location != "treasure" and current_location != "end":
    print(world[current_location]["description"])

    paths = world[current_location].get("paths", {})
    if paths:
        print("Paths available:")
        for path, destination in paths.items():
            print(path)

    
    user_choice = input("Enter your choice: ").lower()

    if user_choice in paths:
        current_location = paths[user_choice]
    else:
        print("Invalid choice. Try again.")

if current_location == "treasure":
    print("You found the treasure and won the game!")
else:
    print("Thanks for playing!")
