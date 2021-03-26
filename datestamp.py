import shutil
from datetime import datetime
import argparse

date = datetime.strftime(datetime.now(), '%Y%m%d')


parser = argparse.ArgumentParser(description='Back up a log file with a timestmap')
parser.add_argument('-in', '--fileName', type=str, required=True, help='Name of input file')
parser.add_argument('-out','--outDirectory', type=str, required=True, help="Name of ouput directory")
args = parser.parse_args()


def timestamp_log(infile, outdirectory):
    timestamp_file = infile.split('.')[0]
    file_format = infile.split('.')[1]
    outfile = f"{timestamp_file}-{date}.{file_format}"
    shutil.copyfile(infile, f"{outdirectory}/{outfile}")


timestamp_log(args.fileName, args.outDirectory)