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
    def download(self):
        print("Downloading...")
        try:
            r = requests.get(self.master_url)
            if r.content == b'404: Not Found':
                r = requests.get(self.main_url)
            name = 'cache.zip'
            with open(name, 'wb') as f:
                f.write(r.content)
                f.close()
        except Exception as e:
            print(e)
            self._clone()

    @retry(wait=wait_exponential(), reraise=True, stop=stop_after_attempt(3))
    def clone(self):
        print('cloning to local...')
        mygit = git.cmd.Git(os.getcwd())
        mygit.clone(git.cmd.Git.polish_url(self.clone_repo))

    def in_zip(self):
        try:
            self.clone()
        except Exception as e:
            print(e)

        os.chdir(self.repo_name)
        with zipfile.ZipFile('../cache.zip', 'w') as target:
            for i in os.walk("."):
                for n in i[2]:
                    target.write(''.join((i[0], '/', n)))
        os.chdir('..')


if __name__ == '__main__':
    m = Mirror('hesgang/Auto-Run')
    m.clone()
