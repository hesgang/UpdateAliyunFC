#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/4 9:43 
# @Author : hesgang
# @File : mirror.py 
from tenacity import retry, stop_after_attempt, wait_exponential
from git.repo import Repo
import git
import requests
import os
import zipfile
import shutil


class Mirror(object):
    def __init__(self, repo):
        self.repo = repo
        self.user_name, self.repo_name = self.repo.split('/')
        self.main_url = """https://codeload.github.com/{}/zip/refs/heads/main""".format(repo)
        self.master_url = """https://codeload.github.com/{}/zip/refs/heads/master""".format(repo)
        self.clone_repo = """https://github.com/{}.git""".format(repo)

    @retry(wait=wait_exponential(), reraise=True, stop=stop_after_attempt(3))
    def clone(self):
        print('cloning to local...')
        mygit = git.cmd.Git(os.getcwd())
        mygit.clone(git.cmd.Git.polish_url(self.clone_repo))

    def in_zip(self):
        self.clone()
        with zipfile.ZipFile('cache.zip', 'w') as target:
            for i in os.walk(self.repo_name):
                for n in i[2]:
                    print(''.join((i[0], '/', n)))
                    target.write(''.join((i[0], '/', n)))


if __name__ == '__main__':
    m = Mirror('hesgang/Auto-Run')
    m.clone()
