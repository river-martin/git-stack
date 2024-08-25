# The `git branch` command denotes the current branch with an asterisk
/^\*/ {
  # The second field is the branch name
  print $2
}