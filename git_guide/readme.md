# Complete Git & GitHub Guide - Comprehensive Notes

## Table of Contents
1. [Git Basics & Concepts](#1-git-basics--concepts)
2. [Initial Setup & Configuration](#2-initial-setup--configuration)
3. [Repository Creation & Management](#3-repository-creation--management)
4. [Daily Workflow](#4-daily-workflow)
5. [Collaboration with Others](#5-collaboration-with-others)
6. [Branching & Merging](#6-branching--merging)
7. [GitHub Integration](#7-github-integration)
8. [Troubleshooting & Common Issues](#8-troubleshooting--common-issues)
9. [Best Practices](#9-best-practices)

---

## 1. Git Basics & Concepts

### What is Git?
- **Version Control System**: Tracks changes to files over time
- **Distributed**: Every developer has full copy of repository history
- **Free & Open Source**: Created by Linus Torvalds for Linux development

### Key Terminology:
- **Repository (Repo)**: Project folder with version tracking
- **Commit**: Snapshot of changes at a specific time
- **Branch**: Independent line of development
- **Clone**: Copy a repository from remote to local
- **Push**: Send local commits to remote repository
- **Pull**: Fetch and merge changes from remote
- **Merge**: Combine different branches of development

### Why Use Git?
- Track history of changes
- Collaborate with multiple developers
- Experiment safely with branches
- Revert to previous versions if needed
- Maintain different versions (production, development)

---

## 2. Initial Setup & Configuration

### 1. Install Git
**Windows**: Download from git-scm.com  
**Mac**: `brew install git` or Xcode Command Line Tools  
**Linux**: `sudo apt install git` (Ubuntu/Debian)

### 2. Basic Configuration (FIRST TIME ONLY)
```bash
# Set your identity (visible in commits)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Set preferred text editor
git config --global core.editor "code --wait"  # VS Code

# Verify configuration
git config --global --list
```

### 3. Common Configuration Options
```bash
# Color output for better readability
git config --global color.ui auto

# Create aliases for common commands
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Line ending settings (important for cross-platform)
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # Mac/Linux
```

---

## 3. Repository Creation & Management

### Creating a New Repository

#### Method 1: Initialize New Project
```bash
# Navigate to project directory
cd /path/to/your/project

# Initialize Git repository
git init

# Check status
git status
```

#### Method 2: Clone Existing Repository
```bash
# Clone from GitHub/GitLab etc.
git clone https://github.com/username/repository-name.git
git clone https://github.com/username/repository-name.git new-folder-name
```

### Essential Files for New Repository

#### .gitignore File (CRITICAL)
Create this file BEFORE first commit to avoid tracking unwanted files:

```bash
# Create .gitignore
cat > .gitignore << EOF
# Python specific
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
.env

# IDE and editor files
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
Thumbs.db

# Database files
*.sqlite
*.db
instance/

# Logs
*.log

# Testing
.pytest_cache/
.mypy_cache/
.coverage

# Distribution files
dist/
build/
*.egg-info/

# Temporary files
*.tmp
*.temp
EOF
```

#### README.md File
```markdown
# Project Title

Brief description of your project.

## Features
- Feature 1
- Feature 2

## Installation
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Usage
\`\`\`bash
python main.py
\`\`\`

## License
Your license information
```

#### requirements.txt (Python Projects)
```text
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
```

---

## 4. Daily Workflow

### Basic Command Sequence

#### 1. Check Status
```bash
git status
```

#### 2. Add Changes to Staging
```bash
# Add specific file
git add filename.py

# Add all changes in current directory
git add .

# Add all changes in entire project
git add -A

# Add files interactively
git add -p
```

#### 3. Commit Changes
```bash
# Basic commit
git commit -m "Descriptive commit message"

# Commit with detailed message
git commit -m "Title" -m "Detailed description of changes"

# Add and commit in one step (only for modified files)
git commit -am "Commit message"
```

### Writing Good Commit Messages
```
Format: <type>: <subject>

Examples:
feat: add user authentication system
fix: resolve memory leak in image processing
docs: update API documentation
style: reformat code according to PEP8
refactor: simplify database connection logic
test: add unit tests for user model
```

### 4. View History
```bash
# Basic log
git log

# One-line format
git log --oneline

# With graph
git log --oneline --graph --all

# Show changes in files
git log --stat

# Filter by author
git log --author="username"
```

---

## 5. Collaboration with Others

### 🆕 NEW SECTION: Working with Teammates' Changes

#### Scenario: Your friend committed changes, how to update your files?

### Method 1: Simple Pull (Most Common)
```bash
# Fetch and merge changes from remote
git pull origin main

# Or shorter (if you've set upstream)
git pull
```

### Method 2: Safe Approach (Recommended for Beginners)
```bash
# 1. Save your current changes (if any)
git stash

# 2. Download latest changes
git fetch origin

# 3. Update your local branch
git pull origin main

# 4. Restore your changes
git stash pop
```

### Method 3: Step-by-Step (More Control)
```bash
# 1. Check what others have pushed
git fetch origin

# 2. See the difference between your branch and remote
git log HEAD..origin/main --oneline

# 3. Merge the changes
git merge origin/main

# Alternative: Rebase instead of merge (cleaner history)
git rebase origin/main
```

### What Happens When You Pull?
1. **Git fetches** all new commits from the remote repository
2. **Git merges** those changes into your current branch
3. **Your files are updated** automatically with your friend's changes

### Handling Different Scenarios:

#### Scenario 1: You have no local changes
```bash
# Simple pull works perfectly
git pull origin main
```

#### Scenario 2: You have uncommitted changes
```bash
# Stash your changes first
git stash
git pull origin main
git stash pop

# If there are conflicts after stash pop, resolve them manually
```

#### Scenario 3: You have committed changes that conflict with friend's changes
```bash
# Pull will create a merge conflict
git pull origin main

# You'll see something like:
# CONFLICT (content): Merge conflict in filename.py
# Automatic merge failed; fix conflicts and then commit the result.

# Edit the conflicted files, look for:
<<<<<<< HEAD
Your changes
=======
Friend's changes
>>>>>>> commit-hash

# Keep what you want, remove conflict markers, then:
git add .
git commit -m "Merge friend's changes"
```

### Best Practices for Team Collaboration:

#### 1. Always Pull Before Starting Work
```bash
# Good habit: pull latest changes before making new changes
git pull origin main
```

#### 2. Pull Before Pushing
```bash
# Never push without pulling first!
git pull origin main
git push origin main
```

#### 3. Communicate with Your Team
- Let teammates know when you're working on sensitive files
- Use descriptive commit messages
- Coordinate on major changes

#### 4. Use Feature Branches for Big Changes
```bash
# Instead of working directly on main
git checkout -b feature/new-feature
# ... make changes ...
git pull origin main  # Update your feature branch with latest main
git checkout main
git pull origin main  # Update main
git merge feature/new-feature
```

### Checking What Your Friend Changed:
```bash
# See latest commits
git log --oneline -5

# See what files were changed in last commit
git show --name-only HEAD

# See actual changes in a file
git diff HEAD~1 HEAD filename.py

# See who changed what and when
git blame filename.py
```

### Resolving Merge Conflicts Like a Pro:

#### Step 1: Identify Conflicts
```bash
git status
# Shows: both modified: filename.py
```

#### Step 2: Open the File and Resolve
```python
# In your code editor, you'll see:
def some_function():
<<<<<<< HEAD
    # Your version
    return "your code"
=======
    # Friend's version  
    return "friend's code"
>>>>>>> commit-hash

# Decide which to keep, or combine:
def some_function():
    # Combined version
    return "improved code"
```

#### Step 3: Mark as Resolved
```bash
git add filename.py
git commit -m "Resolve merge conflict with friend's changes"
```

### Quick Collaboration Cheat Sheet:
```bash
# Daily team workflow:
git pull origin main          # Get latest changes
# ... work on your tasks ...
git add .                    # Stage changes
git commit -m "Description"  # Commit changes  
git pull origin main         # Get any new changes
git push origin main         # Share your changes
```

---

## 6. Branching & Merging

### Branch Management

#### Create and Switch Branches
```bash
# List all branches
git branch

# Create new branch
git branch feature-new-auth

# Switch to branch
git checkout feature-new-auth

# Create and switch in one command
git checkout -b feature-new-auth

# Switch back to main
git checkout main
```

#### Merge Branches
```bash
# Ensure you're on target branch (usually main)
git checkout main

# Merge feature branch
git merge feature-new-auth

# Delete branch after merge
git branch -d feature-new-auth
```

#### Resolve Merge Conflicts
1. **Identify conflicts**: `git status` shows conflicted files
2. **Edit files**: Look for `<<<<<<<`, `=======`, `>>>>>>>` markers
3. **Resolve**: Choose which changes to keep
4. **Mark as resolved**: `git add filename.py`
5. **Complete merge**: `git commit`

### Stashing Changes
```bash
# Save uncommitted changes temporarily
git stash

# View stashed changes
git stash list

# Apply last stashed changes
git stash pop

# Apply specific stash
git stash apply stash@{1}

# Clear all stashes
git stash clear
```

---

## 7. GitHub Integration

### Connecting Local Repository to GitHub

#### 1. Create Repository on GitHub
- Go to GitHub.com → Click "+" → "New repository"
- Name: your-repo-name
- Description: Brief description
- **DO NOT** initialize with README, .gitignore, or license
- Choose Public/Private
- Click "Create repository"

#### 2. Connect Local Repository
```bash
# Add remote origin
git remote add origin https://github.com/username/repo-name.git

# Verify remote
git remote -v

# Rename branch to main (if needed)
git branch -M main

# First push
git push -u origin main
```

### Authentication Methods

#### HTTPS (Simpler)
```bash
# Will prompt for username/password or token
git push origin main

# Cache credentials (Windows)
git config --global credential.helper wincred

# Cache credentials (Mac)
git config --global credential.helper osxkeychain

# Cache credentials (Linux)
git config --global credential.helper cache
```

#### SSH (More Secure)
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add key to SSH agent
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key

# Use SSH URL instead of HTTPS
git remote set-url origin git@github.com:username/repo-name.git
```

### Common Remote Operations

#### Push Changes
```bash
# Push to remote
git push

# Push specific branch
git push origin branch-name

# Force push (use with caution)
git push --force-with-lease
```

#### Pull Changes
```bash
# Fetch and merge
git pull

# Fetch only
git fetch

# Pull specific branch
git pull origin branch-name
```

#### Working with Remote Branches
```bash
# List remote branches
git branch -r

# Create local branch tracking remote
git checkout -b feature-branch origin/feature-branch

# Delete remote branch
git push origin --delete branch-name
```

---

## 8. Troubleshooting & Common Issues

### Common Problems & Solutions

#### 1. Committed Wrong Files
```bash
# Remove file from last commit (keeps changes)
git reset --soft HEAD~1

# Then re-commit properly
git add correct-files.py
git commit -m "Proper commit message"

# Remove file from staging (keeps file changes)
git reset HEAD filename.py

# Completely remove file from history (dangerous)
git filter-branch --tree-filter 'rm -f sensitive-file.txt' HEAD
```

#### 2. Wrong Commit Message
```bash
# Change last commit message
git commit --amend -m "New commit message"

# For older commits (interactive rebase)
git rebase -i HEAD~3  # Change last 3 commits
```

#### 3. Need to Revert Changes
```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo last commit and discard changes
git reset --hard HEAD~1

# Revert specific commit (creates new commit)
git revert commit-hash

# Discard uncommitted changes in file
git checkout -- filename.py

# Discard all uncommitted changes
git reset --hard
```

#### 4. Authentication Issues
```bash
# If getting 403 errors, use personal access token
# GitHub: Settings → Developer settings → Personal access tokens

# Update remote URL with token
git remote set-url origin https://token@github.com/username/repo.git
```

### Recovery Commands

#### View History and Changes
```bash
# See what will be pushed
git log --oneline origin/main..main

# See differences
git diff

# See staged differences
git diff --staged

# See branch differences
git diff main..feature-branch
```

#### Find Lost Commits
```bash
# View reflog (history of all actions)
git reflog

# Recover lost commit from reflog
git checkout commit-hash
git checkout -b recovered-branch
```

---

## 9. Best Practices

### Repository Structure
```
project-root/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
└── docs/
    └── documentation.md
```

### Commit Strategy
1. **Commit often**: Small, logical changesets
2. **Test before commit**: Don't commit broken code
3. **Write meaningful messages**: Explain WHY, not just what
4. **One feature per commit**: Keep commits focused

### Branching Strategy
- `main`: Production-ready code only
- `develop`: Integration branch for features
- `feature/`: New features (from develop, back to develop)
- `hotfix/`: Critical production fixes (from main, to main and develop)

### .gitignore Best Practices
- Ignore OS-specific files
- Ignore IDE/editor files
- Ignore dependencies and build artifacts
- Ignore sensitive data (API keys, passwords)
- Include comments for different sections

### Collaboration Etiquette
1. **Pull before push**: Always pull latest changes before pushing
2. **Review code**: Use pull requests for team projects
3. **Communicate**: Discuss major changes with team
4. **Backup**: Regular pushes to remote repository

### Advanced Tips

#### Tagging Releases
```bash
# Create annotated tag
git tag -a v1.0.0 -m "Version 1.0.0 release"

# Push tags to remote
git push --tags
```

#### Git Hooks (Automation)
Create scripts in `.git/hooks/` for automation:
- `pre-commit`: Run tests before commit
- `pre-push`: Run integration tests before push
- `post-merge`: Install dependencies after merge

#### Partial Staging
```bash
# Stage specific parts of a file
git add -p filename.py

# Create patch files for sharing changes
git format-patch origin/main
```

---

## Quick Reference Cheat Sheet

### Essential Commands
```bash
git init                        # Initialize new repo
git clone <url>                 # Clone existing repo
git status                      # Check status
git add <file>                  # Add file to staging
git commit -m "message"         # Commit changes
git push                        # Push to remote
git pull                        # Pull from remote
git log                         # View history
git branch                      # List branches
git checkout <branch>           # Switch branch
git merge <branch>              # Merge branch
```

### Team Collaboration Workflow
```bash
# Daily team routine
git pull origin main           # Get friend's changes first!
git status                     # Check what you have
# ... make your changes ...
git add .                      # Stage changes
git commit -m "Meaningful message"
git pull origin main           # Get any new changes
git push origin main           # Share your changes

# When conflicts happen:
git pull origin main           # This may create conflicts
# ... resolve conflicts in files ...
git add .                      # Mark conflicts as resolved
git commit -m "Merge conflicts"
git push origin main
```

### Common Team Scenarios Solved:

**Q: My friend added new files, how do I get them?**
```bash
git pull origin main
```

**Q: I'm getting "divergent branches" error?**
```bash
git pull --rebase origin main
```

**Q: How to see what my friend changed?**
```bash
git log --oneline -5           # Last 5 commits
git show HEAD                  # Latest commit details
```

**Q: I messed up my local files after pull?**
```bash
git reset --hard HEAD~1        # Go back before pull
```

