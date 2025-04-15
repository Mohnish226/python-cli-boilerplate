# Python CLI Boilerplate

A lightweight, easy-to-use boilerplate for creating command-line tools in Python.

## Features
- Clean, modular structure for building CLI applications
- Command registration system using argparse
- Simple to extend with new commands
- Python 3.13 compatibility

## Installation

### Requirements

- Python 3.13 or higher

### Steps

Clone this repository:
```
git clone https://github.com/Mohnish226/python-cli-boilerplate.git

cd python-cli-boilerplate
```

Install the package in development mode:
```
pip install -e .
# or
uv pip install -e .
```

## Usage

### Basic Commands

Once installed, you can run the CLI tool:

```
cli-tool --help
# or 
uv run cli-tool --help
```

This will display the help message with available commands.

Example command:
```
cli-tool hello --name "John Doe"
# or
uv run cli-tool hello --name "John Doe"
```

The above command will output: `Hello, John Doe!`

### Adding New Commands

To add a new command, create a new Python file in the `src/cli/commands` directory. 

For example: `src/cli/commands/your_command.py`

```python
def register_subcommand(subparsers):
    parser = subparsers.add_parser("command-name", help="Command description")
    parser.add_argument("--option", help="Description of option")
    parser.set_defaults(func=your_function)

def your_function(args):
    # Implement your command logic here
    print(f"Command executed with option: {args.option}")
```

Then, import and register the command in `src/cli/main.py`:

```python
from cli.commands import example, your_command

def register_commands(subparsers):
    """
    Register all commands with their respective subparsers.
    """
    example.register_subcommand(subparsers)
    your_command.register_subcommand(subparsers)
```

## Customization
This boilerplate is designed to be customized for your specific needs:

Edit [`pyproject.toml`](pyproject.toml) to change the package name, version, and dependencies
Modify the command prompt in [`src/cli/main.py`](src/cli/main.py) to change the command-line interface
Add new commands to the commands directory
Extend with additional functionality as needed