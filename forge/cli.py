import argparse
from .hasher import hashContent
from .task import build

def buildHelp(args):
    build(args.taskName)

def hash(args):   
    print(hashContent(args.fileName))

def main():
    parser = argparse.ArgumentParser(prog="forge", description="Forge CLI Tool")
    parser.add_argument('--version', action='version', version='forge v0.0.1')
    sub_parser = parser.add_subparsers(dest="OPTIONS", required=True)


    # Build Command
    com_p = sub_parser.add_parser("build")
    com_p.add_argument("taskName", type=str)
    com_p.set_defaults(func=buildHelp)
    
    # Hash Command -> To check the hash of a file 
    hash_p = sub_parser.add_parser("hash")
    hash_p.add_argument("fileName", type=str)
    hash_p.set_defaults(func=hash)

    args = parser.parse_args()
    args.func(args)