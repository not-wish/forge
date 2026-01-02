import argparse

def main():
    parser = argparse.ArgumentParser(prog="forge", description="Forge CLI Tool")
    parser.add_argument('--version', action='version', version='forge 0.0.1')
    parser.add_argument("command", help="Command to run", choices=["init", "build", "deploy"])

    args = parser.parse_args()

    if args.command == "init":
        print("Initializing project...")
    elif args.command == "build":
        print("Building project...")
    elif args.command == "deploy":
        print("Deploying project...")

    
