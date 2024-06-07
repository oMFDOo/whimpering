from github import Github
import github
def get_latest_closed_issue(token, owner = 'oMFDOo', repo = 'whimpering'):
    g = Github(token)
    repository = g.get_repo(f"{owner}/{repo}")
    closed_issues = repository.get_issues(state='open', sort='updated', direction='desc')
    
    latest_closed_issue = closed_issues[0] if closed_issues.totalCount > 0 else None
    return latest_closed_issue

def get_code_from_issue(issue):
    commend = issue.get_comments()
    commend = list(filter(lambda x: x.user.login in ["Piorosen", "oMFDOo"], commend))
    return commend
    
def get_code_by_user(comment):
    data = list(map(lambda x: {
            'body': x.body,
            'name': x.user.login
        }, comment))
    name = []
    result = []
    for item in data:
        if not item['name'] in name:
            name.append(item['name'])
            result.append(item)
    return result
