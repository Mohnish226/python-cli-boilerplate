def register_subcommand(subparsers):
    parser = subparsers.add_parser("hello", help="Print a greeting")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.set_defaults(func=greet)


def greet(args):
    print(f"Hello, {args.name}!")
