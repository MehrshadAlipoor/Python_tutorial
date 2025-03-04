# Session6: Git and Github
# Date: 04/03/2025

# ================================================================================================
# conflict resolution in git

# what is a conflict in git?
    # A conflict in git occurs when two branches have changes in the same line of code.
    # Git is unable to automatically merge the changes and requires manual intervention.
    # Conflicts can occur during the merge, rebase, or pull operations in git.
    # Conflicts are marked in the code with special markers that indicate the conflicting changes.

# how to resolve a conflict in git?
    # To resolve a conflict in git, you need to follow these steps:
        # 1. Identify the conflicting files and lines of code.
        # 2. Open the conflicting files in a text editor.
        # 3. Search for the conflict markers (<<<<<<<, =======, >>>>>>>).
        # 4. Choose one of the conflicting changes or combine them.
        # 5. Save the changes and remove the conflict markers.
        # 6. Add the resolved files to the staging area.
        # 7. Commit the changes to complete the conflict resolution.
        # 8. Push the changes to the remote repository to share the resolved conflict.

# conflict resolution strategies in git
    # There are several strategies for resolving conflicts in git:
        # 1. Accept current change: Choose the changes from the current branch.
        # 2. Accept incoming change: Choose the changes from the incoming branch.
        # 3. Accept both changes: Combine the changes from both branches.
        # 4. Accept all changes: Accept all changes from both branches.
        # 5. Manual resolution: Manually edit the code to resolve the conflict.

# conflict resolution tools in git
    # Git provides several tools to help you resolve conflicts:
        # 1. git mergetool: A tool that helps you resolve conflicts interactively.
        # 2. git diff: A command that shows the differences between conflicting files.
        # 3. git status: A command that shows the status of the conflict resolution.
        # 4. git checkout: A command that allows you to switch between conflicting changes.

# ================================================================================================
# Forking in Git

# what is forking in git?
    # Forking is a process in git that allows you to create a copy of a repository on github.
    # It is useful when you want to contribute to a project without directly modifying the original code.
    # When you fork a repository, you create a new copy of the code that you can modify and push changes to.
    # Forking creates a separate repository on your github account that is independent of the original repository.

# how to fork a repository on github?
    # To fork a repository on github, follow these steps:
    # 1. Go to the github repository you want to fork.
    # 2. Click on the "Fork" button in the top right corner of the page.
    # 3. Select your github account as the destination for the fork.
    # 4. Wait for github to create the forked repository on your account.
    # 5. Clone the forked repository to your local machine using the git clone command.

# pull request in git:
    # A pull request is a request to merge changes from a forked repository to the original repository.
    # It allows you to propose changes to the original code and collaborate with other developers.
    # When you create a pull request, the changes are reviewed by the repository owner before they are merged.
    # Pull requests are a common way to contribute to open source projects on github.

# ================================================================================================
# Git blame

# what is git blame?
    # Git blame is a command that shows the author and revision history of a file.
    # It allows you to see who made changes to a file and when the changes were made.
    # Git blame is useful for tracking down the origin of a bug or understanding the history of a file.
    # It shows the commit hash, author name, date, and line number for each line of code.

# ================================================================================================
# Git tags

# what are git tags?
    # Git tags are markers that point to specific commits in the git history.
    # They are used to mark important milestones, releases, or versions of the code.
    # Tags are immutable and do not change once they are created.
    # Tags can be annotated or lightweight, depending on the amount of information you want to store.
    # Annotated tags store additional information such as tagger name, email, date, and message.

# ================================================================================================

# Python Learning

# Exercise: creat a weight converter program that asks the user to enter a weight in kg or lbs and converts it to the other unit.
# 1 kg = 2.20462 lbs
# 1 lb = 0.453592 kg

weight = float(input("Input your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted_weight = weight * 0.453592
    print(f"Your weight in kg is: {converted_weight}")

elif unit.upper() == "K":
    converted_weight = weight * 2.20462
    print(f"Your weight in lbs is: {converted_weight}")

else:
    print("Invalid unit. Please enter 'L' for lbs or 'K' for kg.")

# ================================================================================================
# Height converter program

# 1 ft = 0.3048 m
# 1 m = 3.28084 ft

height = float(input("Input your height: "))
unit = input("Enter height unit (F)eet or (M)eters: ")

if unit.strip().upper() == "F":
    converted_height = height * 0.3048
    print(f"Your height in meters is: {converted_height}")

elif unit.strip().upper() == "M":
    converted_height = height * 3.28084
    print(f"Your height in feet is: {converted_height}")

else:
    print("Invalid unit. Please enter 'F' for feet or 'M' for meters.")

# ================================================================================================
# Building a car game

# Exercise: Build a car game that simulates the basic functions of a car.
# The car can start, stop, accelerate, and exit the game.

command = ""
is_started = False  # car is not started initially

while True:
    command = input("> ").lower()

    if command == "start":
        if not is_started:
            print("Car is already started.")
        else:
            is_started = True
            print("Car started...Ready to go!")

    elif command == "stop":
        if not is_started:
            print("Car is already stopped.")
        else:
            is_started = False
            print("Car stopped.")

    elif command == "accelerate":
        if is_started:
            print("Car is accelerating...")
        else:
            print("Car needs to be started first.")

    elif command == "exit":
        print("Exiting the car game...")
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
accelerate - to accelerate the car
exit - to exit the game
              """)

    else:
        print("Invalid command. Please enter 'start', 'stop', 'accelerate', or 'exit'.")
        