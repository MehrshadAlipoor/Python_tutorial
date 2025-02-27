# Session5: Git and GitHub
# Date: 25/02/2025

# ================================================================================================
# Branching in Git
# what is branching?
    # Branching is a feature in git that allows you to create a copy of the code and work on it separately.
    # It is useful when you want to work on a new feature or fix a bug without affecting the main code.
    # Each branch has its own copy of the code and changes made to one branch do not affect other branches.
    # You can create, switch, merge, and delete branches in git.
    # Branching allows you to work on multiple features simultaneously and merge them later.

# process of branching:
    # code -> 
    # git branch -> new branch -> git checkout -> switch to new branch -> 
    # code -> git commit -> save changes to new branch -> 
    # git checkout -> switch to main branch -> git merge -> 
    # merge changes from new branch to main branch

# types of branches:
    # master branch = main branch
    # feature branch = branch for new features
    # bugfix branch = branch for fixing bugs
    # release branch = branch for releasing the code
    # hotfix branch = branch for fixing critical bugs

# git commands for branching:
    # git branch = list all branches
    # git branch <branch_name> = create a new branch
    # git checkout <branch_name> = switch to a branch
    # git checkout -b <branch_name> = create and switch to a new branch
    # git merge <branch_name> = merge changes from a branch
    # git branch -d <branch_name> = delete a branch (if changes are merged)
    # git branch -D <branch_name> = force delete a branch (if changes are not merged)

# branching strategies:
    # feature branching = create a new branch for each feature
    # git flow = a branching model for git
    # trunk-based development = main branch is always stable
    # release branching = create a branch for each release
    # environment branching = create a branch for each environment (dev, test, prod)

#================================================================================================
# Exercise: Branching in Git
# create a new branch called "feature-login" and switch to it

# git branch feature-login
# git checkout feature-login
