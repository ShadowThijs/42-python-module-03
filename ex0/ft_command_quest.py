import sys


def main():
    print("=== Command Quest ===")
    args = sys.argv
    total = len(args)

    if total == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print(f"Total arguments: {total}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {total - 1}")
        index = 1
        for arg in args[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

        print(f"Total arguments: {total}")


main()
