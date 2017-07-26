#!/usr/bin/python
import sys, os
import json
import requests
from widget import Widget

widget = Widget('github')

GITHUB_PRIVATE_TOKEN = 'YOUR_GITHUB_PRIVATE_TOKEN'
GITHUB_BASE_URL = 'YOUR_GITHUB_BASE_URL'
GITHUB_USERNAME = 'YOUR_GITHUB_LOGIN_USERNAME'
REPOSITORY_NAME_PATTERN = 'YOUR_REPO_NAME_PATTERN'

REPOSITORIES_URL = '{}/api/v3/search/repositories?q={}'.format(GITHUB_BASE_URL, REPOSITORY_NAME_PATTERN)

auth = {'access_token': GITHUB_PRIVATE_TOKEN}

def get_data():
    local_repos = {}
    data = {}
    try:
        repos = widget.get_response(REPOSITORIES_URL, 'GET', auth).json()
        if 'items' not in repos:
            data['error'] = 'No repos found on {}'.format(GITHUB_BASE_URL)
            return data

        for repo in repos['items']:
            local_repos[repo['url']] = {
                'url': repo['url'],
                'name': repo['name'],
                'full_name': repo['full_name']
            }

        for url, repo_data in local_repos.items():
            should_show = False
            prs = widget.get_response('{}/pulls?state=open'.format(url), 'GET', auth).json()
            for pr in prs:
                pr_number = pr['number']
                pr_url = pr['url']
                pr_name = pr['title']
                reviewers = pr['requested_reviewers']
                for reviewer in reviewers:
                    if reviewer['login'] == GITHUB_USERNAME:
                        if 'prs' not in local_repos[url]:
                            local_repos[url]['prs'] = []

                        local_repos[url]['prs'].append({
                            'name': pr_name,
                            'url': pr_url,
                            'number': pr_number
                        })
                        should_show = True

            if should_show:
                data[url] = local_repos[url]

    except requests.ConnectionError as ce:
        data['error'] = 'Cannot connect to {}'.format(GITHUB_BASE_URL)

    if len(data) == 0:
        data['message'] = 'No pending reviews'

    return data

data = get_data()
print json.dumps(data) if isinstance(data, (dict, list, tuple, set)) else data.encode('utf-8')

sys.exit()
