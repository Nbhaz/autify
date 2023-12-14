import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Fetch web pages and save them to disk for later retrieval and browsing.')
    parser.add_argument('urls', nargs='+', help='URLs to fetch')
    parser.add_argument('--metadata', action='store_true', help='Include metadata and create a local mirror')
    args = parser.parse_args()
    print(args.urls)
    print(args.metadata)


if __name__ == "__main__":
    main()
