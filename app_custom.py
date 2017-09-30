#!/usr//bin/env python
# -*- coding:UTF-8 -*-





# 部署环境
# npm 环境
# git 环境
# jdk 环境
# gradle 环境


# 源码管理
# 拉取 GitHub 特定分支代码
# 如果本地已有源码就拉取分支最新代码 -> 保持源码为最新
# npm 依赖需要写死
# 每次都需要重新安装 npm 依赖?

# 打包
# 根据配置文件 修改源码
# 图片 -> 替换
# 变量名 -> 修改变量文件
# 包名 -> 修改 app/build.gradle 文件
# 运行 gradle 打包命令


import os
import json
import time

import xml_helper


def read_repo_from_config(config):
    return 'git@github.com:1-Hash/cloud-miner-android.git'


_config = None

_app_repo_address = read_repo_from_config(_config)

_repo_local_path = './AppProjects'


def pull_repo(repo_address):
    os.system('git pull')
    pass


def get_project_name():
    start = _app_repo_address.find('/') + 1
    end = len(_app_repo_address) - 4
    return _app_repo_address[start:end]


if __name__ == '__main__':
    print(get_project_name())
