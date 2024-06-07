#%%
from load_from_github import *
import os
import argparse

def upload_code(token, owner, repo, dir_solved_code) -> int:
    issue = get_latest_closed_issue(token, owner, repo)
    comment = get_code_from_issue(issue)
    code = get_code_by_user(comment)

    title: str = issue.title
    title = title.replace('[', '').replace(']', '')
    for c in code:
        dir = '{0}/{1}/{2}'.format(dir_solved_code, c['name'], title)
        if not os.path.exists(dir):
            print(dir)
            os.makedirs(dir)

        file = os.path.join(dir, "solve.cpp")
        if not os.path.exists(file):
            with open(os.path.join(dir, "solve.cpp"), "wt+") as f:
                f.write(c['body'])

    return len(code), issue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Score Table for Competition')

    parser.add_argument("--github_token", type=str, required=True)
    parser.add_argument("--github_owner", type=str, default='oMFDOo')
    parser.add_argument("--github_repo", type=str, default='whimpering')
    parser.add_argument("--dir_solved_code", type=str, default='../../solved_code')

    args = parser.parse_args()

    uploaded_uesr_num, issue = upload_code(args.github_token, args.github_owner, args.github_repo,
                                           args.dir_solved_code)

