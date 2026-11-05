#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO Handle Errors/Exceptions
# using an exception handler and the try/except/else block
""" 
    DocString
"""
import re
import sys

# Example of a User function with optional parameter passing
# and default values and annotations.
def search_pattern(pattern:str = r"^.{19}$", file:str = r"f:\labs\words")->None:
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error: {err.args}, file={err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error: {err.args}, file={err.filename}", file=sys.stderr)
        sys.exit(2)
    except OSError as err:
        print(f"OS Error: {err.args}", file=sys.stderr)
        sys.exit(3)
    except Exception as err:
        print(f"Some other Error occurred - investigate", file=sys.stderr)
        sys.exit(4)
    else:
        # Execute if try block succeeds
        reobj = re.compile(pattern) # PRE-Compiles PATTERN ONLY ONCE
        for line in fh_in:
            m = reobj.search(line) # USE precompiled pattern
            if m:
                print(f"Matched {line.rstrip()}")
        fh_in.close()
    finally:
        # Executes if try block fails or succeeds
        print("And now for something completely different..")
    return None

def main():
    search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words")
    return None

# Namespace trick
if __name__ == "__main__":
    main()
    sys.exit(0)