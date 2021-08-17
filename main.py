import argparse
import sys
from pathlib import Path
import time

class DuplicateRemover:

    def __init__(self, source_path: str, no_inputs = False, generate_logs = False, log_path = None, verbose = False):
        # validate
        log_path_set = True if log_path else False
        if not log_path:
            log_path = 'log.txt'
        
        # setup source_path and log_path
        log_path_obj = Path.cwd() / log_path
        log_path_obj = log_path_obj.resolve()
        source_path = Path(source_path).resolve()

        # set properties
        self.source_path = source_path

        ## config properties
        self.no_inputs = no_inputs
        self.generate_logs = generate_logs
        self.log_path = log_path_obj
        self.log_path_set = log_path_set
        self.verbose = verbose

    def welcome(self):
        print()
        print('***********************************')
        print('***      DUPLICATE REMOVER      ***')
        print('***********************************')
        print()
        print(f"RECURSIVE CLEAN ON PATH '{str(self.source_path)}'")

        if not self.no_inputs:
            while True:
                print()
                answer = str.lower(input('Perform recursive clean? (Y/n):'))
                if answer == 'y':
                    break
                elif answer == 'n':
                    print('Exiting...')
                    sys.exit()
                else:
                    print('Invalid option.')

        print()
        if self.generate_logs:
            if self.log_path_set or self.verbose:
                print(f"Log file location: {str(self.log_path)}")
            else:
                print(f"Log file location: {self.log_path.name}")
        print('Starting clean...')
    
if __name__ == '__main__':
    # setup argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="the path of the drive or directory to perform the operation on", type=str)
    parser.add_argument('-n', '--no-inputs', help="skips all inputs, assuming the default value", action='store_true')
    parser.add_argument('-q', '--quiet', help="the app will not generate log files", action="store_true")
    parser.add_argument('-o', '--output', help="the path of the log output file", type=str)
    parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    source_path = args.path
    
    # run app
    App = DuplicateRemover(
        source_path,
        no_inputs=args.no_inputs,
        generate_logs=(not args.quiet),
        log_path=args.output,
        verbose=args.verbose)
    App.welcome()
