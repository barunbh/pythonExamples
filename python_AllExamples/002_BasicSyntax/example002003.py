import getopt, sys


def usage():
    print("\nThis is the usage function\n")
    print('Usage: '+sys.argv[0]+' -i <file1> [option]')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hco:v", ["help=", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = 'We love Python'
    verbose = '1.11.2.12'
    for o, a in opts:
        if o == "-v":
            print(verbose)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            print(output)
        elif o in "-c":
            print("clear")
        else:
            assert False, "unhandled option"
    # ...


if __name__ == "__main__":
    main()
