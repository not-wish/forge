import argparse
from .hasher import hashContent
from .task import build

def add(args):
    print(args.x + args.y)

def subtract(args):
    print(args.x - args.y)

def multiply(args):
    print(args.x * args.y)

def divide(args):
    if (args.y != 0):
        print(args.x / args.y)
    else:
        print("Division by Zero: 0")

def buildHelp(args):
    build(args.taskName)

def hash(args):
    
    print(hashContent(args.fileName))

def main():
    parser = argparse.ArgumentParser(prog="forge", description="Forge CLI Tool")
    parser.add_argument('--version', action='version', version='forge v0.0.1')
    sub_parser = parser.add_subparsers(dest="OPTIONS", required=True)

    add_p = sub_parser.add_parser("add")
    add_p.add_argument("x", type=float)
    add_p.add_argument("y", type=float)
    add_p.set_defaults(func=add)
    
    sub_p = sub_parser.add_parser("subtract")
    sub_p.add_argument("x", type=float)
    sub_p.add_argument("y", type=float)
    sub_p.set_defaults(func=subtract)
    
    mul_p = sub_parser.add_parser("multiply")
    mul_p.add_argument("x", type=float)
    mul_p.add_argument("y", type=float)
    mul_p.set_defaults(func=multiply)
    
    div_p = sub_parser.add_parser("divide")
    div_p.add_argument("x", type=float)
    div_p.add_argument("y", type=float)
    div_p.set_defaults(func=divide)

    com_p = sub_parser.add_parser("build")
    com_p.add_argument("taskName", type=str)
    com_p.set_defaults(func=buildHelp)
    
    hash_p = sub_parser.add_parser("hash")
    hash_p.add_argument("fileName", type=str)
    hash_p.set_defaults(func=hash)

    args = parser.parse_args()
    args.func(args)