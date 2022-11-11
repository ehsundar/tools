import argparse


def main():
    parser = argparse.ArgumentParser("autounderscore")
    parser.add_argument("filepath", type=str)
    args = parser.parse_args()

    with open(args.filepath, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        ln = lines[i]
        if ln.strip().startswith("def "):
            stop = len(ln)
            if "(" in ln:
                stop = ln.find("(")

            start = ln.find("def ") + 4

            ln = ln[:start] + ln[start:stop].replace(" ", "_") + ln[stop:]
            lines[i] = ln

    new_contents = "".join(lines)
    with open(args.filepath, "w") as file:
        file.write(new_contents)


if __name__ == '__main__':
    main()
