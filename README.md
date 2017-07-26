# [Ubersicht](http://tracesof.net/uebersicht/) - Github Reviews

Have info about your latest TV Shows available at put.io right on your Mac desktop.

## Requirements

- [Ubersicht MacOSX App](http://tracesof.net/uebersicht/)
- Python >= 2.7
- requests python package installed. If you do not have it installed, please follow http://docs.python-requests.org/en/master/user/install/ (alternatively, run `pip install -r requirements.txt`)

## Installation

- clone this repository somewhere on your disk
- copy the github-reviews.widget folder into your Ubersicht widgets folder
- edit the get-data.py info with your credentials and your folder RSS
- (optional) edit index.coffee file styles based on your placement requirements

## Configuration

- GITHUB_PRIVATE_TOKEN = Generate your private Token for your Github account
- GITHUB_BASE_URL = Set your Github base URL (i.e https://github.com)
- GITHUB_USERNAME = Set your Github username
- REPOSITORY_NAME_PATTERN = In order to speed things up, it's best to set some query to decrease the number of repositories the script will go through in order to find your reviews.
