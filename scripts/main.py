import argparse
from calc_table import *
from update_score import *
from upload_code import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Score Table for Competition')

    parser.add_argument("--score_file", type=str, default='./current_score.txt')
    parser.add_argument("--template", type=str, default='../resources/template_score.md')
    parser.add_argument("--output", type=str, default='../README.md')

    parser.add_argument("--github_token", type=str, required=True, default=None)
    parser.add_argument("--github_owner", type=str, default='oMFDOo')
    parser.add_argument("--github_repo", type=str, default='whimpering')
    parser.add_argument("--win_list", type=str, default='./win_list.txt')
    parser.add_argument("--output_score", type=str, default='./current_score.txt')

    parser.add_argument("--dir_solved_code", type=str, default='../solved_code')
    args = parser.parse_args()

    uploaded_uesr_num, issue = upload_code(args.github_token, args.github_owner, args.github_repo,
                           args.dir_solved_code)
    
    if uploaded_uesr_num == 1:
        # 먼저 코드 업로드를 수행하고, 이때 comment가 1개라면 점수와 테이블 갱신
        # 만약 comment가 2개라면 점수와 테이블 갱신은 하지 않도록 만들고, Issue는 알아서 Close가 되도록 만듬
        update_score(args.github_token, args.github_owner, args.github_repo,
                    args.win_list, args.output_score)
        update_table(args.score_file, args.template, args.output)
    elif uploaded_uesr_num == 2:
        # close issue!
        issue.edit(state="closed")

    