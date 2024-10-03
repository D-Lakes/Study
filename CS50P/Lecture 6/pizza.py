from tabulate import tabulate as t
import sys
import csv
from pathlib import Path

def error_check():
    match len(sys.argv):
        case 1:
            sys.exit("Please specify a file")
        case 2:
            if not sys.argv[1].endswith(".csv"):
                sys.exit("Only CSV files allowed")
            f = Path(sys.argv[1])
            if not f.exists():
                sys.exit("File does not exist")
        case _:
            sys.exit("Only one command line argument allowed")

def main():
    error_check()
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(t(reader,headers="firstrow", tablefmt='grid'))
        
if __name__ == "__main__":
    main()
