from github import Github
from datetime import datetime, timezone, timedelta

def get_win_latest(file: str) -> str:
    data = None
    with open(file, "r") as reader:
        data = reader.readlines()
    if len(data) == 0:
        return []
    # create_time, issue_id, winner
    return list(map(lambda x: int(x.split(',')[1]), data))

def add_win_list(file: str, issue_id: str, winner: str):
    data = None
    with open(file, "r") as reader:
        data = reader.readlines()
    korea_time_zone = datetime.now(timezone(timedelta(hours=+9))).isoformat()
    # create_time, issue_id, winner
    data.append("{0},{1},{2}".format(korea_time_zone, issue_id, winner))
    with open(file, "wt+") as writer:
        writer.writelines(data)

def get_latest_closed_issue(token, owner = 'oMFDOo', repo = 'whimpering'):
    g = Github(token)
    repository = g.get_repo(f"{owner}/{repo}")
    closed_issues = repository.get_issues(state='closed', sort='updated', direction='desc')
    
    latest_closed_issue = closed_issues[0] if closed_issues.totalCount > 0 else None
    return latest_closed_issue

def update_current_score(input: str, output: str):
    name = { 'oMFDOo': 0, 'Piorosen': 0 }
    with open(input, 'r') as f:
        text = list(map(lambda x: x.split(',')[-1], f.readlines()))
        for d in text:
            name[d] += 1
    result = "{0},{1}".format(name['oMFDOo'], name['Piorosen'])
    with open(output, 'wt+') as f:
        f.write(result)
    


#%%


# # issue = get_latest_closed_issue()
# commend = issue.get_comments()
# #%%
# # data = len(commend)
# for d in commend:
#     print(d.body)
#     print(d.user.name)
#     print(d.user.login)

# #%%
# # create_time, issue_id, winner
# print(issue.number)