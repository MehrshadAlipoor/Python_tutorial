#Session6: Git and Github
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