# Git Stack

Git Stack is intended to be a command line utility that saves the user's branch navigation history. It should allow the user to backtrack by popping a branch name off the navigation stack. Additionally, Git Stack should set the environment variable `prev` before each branch change, so that after a backtrack step, the user can merge the previous branch into the current branch with the command `git merge $prev`. Lastly, the user should be able to view their navigation history.

## Example usage

**Path tracing**: The command below adds the current branch to the navigation stack, sets `prev` to the current branch, then checks out out branch `bname`.

```Bash
git-stack checkout bname
```

**Backtracking**: The command below sets `prev`, pops a branch name from the stack, and then checks out the popped branch.

```Bash
git-stack backtrack
```

**Referencing the previous branch**: The previous branch is stored in the environment variable `prev`. It is convenient to use when merging and rebasing, as is shown in the examples below.

```Bash
# Merge the branch that was visited most recently into the current branch
git merge $prev
```

```Bash
# Rebase the previous branch onto the current branch
git rebase $prev
```

**Viewing the stack trace (i.e. navigation history)**: Various options can be provided. Run `git-stack --help` to view them all.

```Bash
# Print the branch navigation stack
git-stack trace
```
