import argparse
from calc_table import *
from update_score import *
from upload_code import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Score Table for Competition')

    parser.add_argument("--score_file", type=str, default='./current_score.txt')
    parser.add_argument("--template", type=str, default='../resources/template_score.md')
    parser.add_argument("--output", type=str, default='../README.md')

    args = parser.parse_args()
    
    update_table(args.score_file, args.template, args.output)
