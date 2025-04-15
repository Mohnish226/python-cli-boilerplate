import argparse

from cli.commands import example


def register_commands(subparsers):
    """
    Register all commands with their respective subparsers.
    """
    example.register_subcommand(subparsers)


def main():
    parser = argparse.ArgumentParser(
        prog="cli-tool", description="A blank Python CLI tool template"
    )

    # Create and register subparsers
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    register_commands(subparsers)

    # Parse arguments
    args = parser.parse_args()

    # Execute the function associated with the command if it exists
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
