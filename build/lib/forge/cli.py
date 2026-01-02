import argparse

def main():
    parser = argparse.ArgumentParser(prog="forge", description="Forge CLI Tool")
    parser.add_argument('--version', action='version', version='forge 0.0.1')
    parser.add_argument("command", help="Command to run", choices=["init", "build", "deploy"])
    parser.add_argument("operation", help="Mathematical Operation to perform", choices=["add","subtract","multiply","divide"])
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    
    args = parser.parse_args()

    if args.command == "init":
        print("Initializing project...")
    elif args.command == "build":
        print("Building project...")
    elif args.command == "deploy":
        print("Deploying project...")

    if args.operation == "add":
        print(args.x + args.y)
    elif args.operation == "subtract":
        print(args.x - args.y)
    elif args.operation == "multiply":
        print(args.x * args.y)
    elif args.operation == "divide":
        if args.y != 0:
            print(args.x / args.y)
        else:
            print("Division by zero not allowed!")    