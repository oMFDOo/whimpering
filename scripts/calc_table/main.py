import argparse
from .calc_table import get_current_information, generate_score_table

def update_table(score_file: str, template: str, output: str):
    score = get_current_information(score_file)
    result = generate_score_table(template, score)
    with open(output, "wt+") as file:
        file.write(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Score Table for Competition')

    parser.add_argument("--score_file", type=str, default='../current_score.txt')
    parser.add_argument("--template", type=str, default='../../resources/template_score.md')
    parser.add_argument("--output", type=str, default='../../README.md')

    args = parser.parse_args()

    update_table(args.score_file, args.template, args.output)
