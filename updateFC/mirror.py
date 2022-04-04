#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/4 9:43 
# @Author : hesgang
# @File : mirror.py 
from tenacity import retry, stop_after_attempt, wait_exponential
from git.repo import Repo
import requests
import os
import shutil


class Mirror(object):
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.main_url = """https://codeload.github.com/{}/zip/refs/heads/main""".format(repo_name)
        self.master_url = """https://codeload.github.com/{}/zip/refs/heads/master""".format(repo_name)
        self.clone_repo = """https://github.com/{}.git""".format(repo_name)

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
    def _clone(self):
        print('cloning to local...')
        _path = os.path.join(os.getcwd(), 'cache')
        Repo.clone_from(self.clone_repo, to_path=_path)
        rez = shutil.make_archive(base_name='cache', base_dir='/cache', format='zip')
        print(rez)



if __name__ == '__main__':
    m = Mirror('hesgang/Auto-Run')
    m._clone()
