function ensure_branch_stack_exists() {
  repo_root=$(git rev-parse --show-toplevel)
  if [ ! -f $repo_root/.git-stack-trace.txt ]; then
    touch $repo_root/.git-stack-trace.txt
  fi
}

ensure_branch_stack_exists

# `git_stack.py` parses the arguments and returns a command string to be sourced.
args="$@"

provided_help=0
for arg in $args; do
  if [ "$arg" == "-h" ]; then
    python3 $GIT_STACK_DIR/src/git_stack.py $args
    provided_help=1
  fi
done

# It is convenient to know the previous branch name when backtracking.
function export_prev_branch() {
  current=$(git branch | awk -f $GIT_STACK_DIR/src/get_current_branch.awk)
  export prev=$current
  # Since this script is sourced, we should clear the variable after it is used.
  current=
}

cmd_str=$(python3 $GIT_STACK_DIR/src/git_stack.py "$@")
if [ $? -eq 0 ] && [ !$provided_help ]; then
  export_prev_branch
  eval $cmd_str
fi
