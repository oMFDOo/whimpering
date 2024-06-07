from load_from_github import get_latest_closed_issue, get_win_latest, add_win_list, update_current_score
import argparse

def main(token: str, owner: str, repo: str, win_list: str, output_score: str):
    issue = get_latest_closed_issue(token, owner, repo)
    if issue == None:
        print("issue is nothing")
        return
    
    print(issue.body)
    win = get_win_latest(win_list)
    if issue.number in win:
        # 이미 처리된 문제
        print("processed problem.")
        return
    
    commend = issue.get_comments()
    win_user = commend[0].user.login

    add_win_list(win_list, issue.number, win_user)
    update_current_score(win_list, output_score)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Score Table for Competition')

    parser.add_argument("--github_token", type=str, default=None)
    parser.add_argument("--github_owner", type=str, default='oMFDOo')
    parser.add_argument("--github_repo", type=str, default='whimpering')
    parser.add_argument("--win_list", type=str, default='../win_list.txt')
    parser.add_argument("--output_score", type=str, default='../current_score.txt')

    args = parser.parse_args()

    main(args.github_token, args.github_owner, args.github_repo,
         args.win_list, args.output_score)

#%%
