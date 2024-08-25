import argparse
import subprocess


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=". git-stack")
    subparsers = parser.add_subparsers(dest="sub_command", required=True)
    parser_checkout = subparsers.add_parser(
        "checkout",
        help="Add the current branch to the navigation stack and checkout the specified branch",
    )
    parser_checkout.add_argument("branch", help="The branch to checkout")
    subparsers.add_parser(
        "backtrack", help="Pop last branch from the navigation stack and check it out"
    )
    subparsers.add_parser("trace", help="Show the navigation stack")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    repo_dir = subprocess.run(
        "git rev-parse --show-toplevel",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    stack_fpath = f"{repo_dir}/.git-stack-trace.txt"
    if args.sub_command == "checkout":
        proc = subprocess.run(
            "git branch | awk -f $GIT_STACK_DIR/src/get_current_branch.awk",
            shell=True,
            capture_output=True,
            text=True,
        )
        current_branch = proc.stdout.strip()
        with open(stack_fpath, "a") as f:
            f.write(current_branch)
            f.write("\n")
        print(f"git checkout {args.branch}")
    elif args.sub_command == "backtrack":
        with open(stack_fpath, "r") as f:
            branches = f.readlines()
        last_branch = branches.pop()
        with open(stack_fpath, "w") as f:
            f.writelines(branches)
        print(f"git checkout {last_branch}")
    elif args.sub_command == "trace":
        print(f"cat {stack_fpath}")
    else:
        raise ValueError(f"Unknown sub-command: {args.sub_command}")


if __name__ == "__main__":
    main()
