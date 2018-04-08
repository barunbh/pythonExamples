import sys
import getopt


def usage(str):
    print("\nThis is the usage function\n for ", str)
    print('Usage: '+sys.argv[0]+' -i <file1> [option]')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:v:h:r", ["output=", "verbose="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for o, a in opts:
        if o == "-v":
            verbose()
        elif o in "-h":
            helps(sys.argv[2])
            sys.exit()
        elif o in ("-o", "--output"):
            output()
        elif o in "-r":
            restart()
        else:
            assert False, "unhandled option"


def output():
    print("Output is :", sys.argv[2])


def verbose():
    print("Printing verbose for ", sys.argv[2])


def restart():
    print("Restarting system")


def helps(str):
    print("help for ", str, "is", usage(str))


if __name__ == "__main__":
    main()

