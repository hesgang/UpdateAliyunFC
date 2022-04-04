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

    def install_zip(self):
        self.clone()
        rez = shutil.make_archive(base_name='cache', base_dir='/%s' % self.repo_name, format='zip')
        print(rez)


if __name__ == '__main__':
    m = Mirror('hesgang/Auto-Run')
    m.clone()
