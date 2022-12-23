#!/usr/bin/python3

import argparse
import os
import subprocess

# 环境变量
appname = os.path.basename(__file__)
workspace = os.path.dirname(__file__)
arch = subprocess.run(["dpkg", "--print-architecture"], stdout=subprocess.PIPE, text=True).stdout[:-1]
app_version = '0.2'

def dists_download():
    print('Download')

def dists_update():
    print('Update')

def simulate_install(packages):
    tmp = os.popen('apt-get -f install -qqq --reinstall --print-uris ' + " ".join(packages) + ' 2>/dev/null').readlines()
    print(tmp)
    print('appname: ' + appname)
    print('workspace: ' + workspace)
    print('arch: ' + arch)
    print('app_version: ' + app_version)

def main():
    # 参数处理
    parser = argparse.ArgumentParser(
        description='apt-offline-kylin',
        epilog='https://github.com/cyanogenic')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-d', '--download',
        action='store_true',
        help='download dists from mirrors',
        dest='download',
    )
    group.add_argument(
        '-u', '--update',
        action='store_true',
        help='update current apt database',
        dest='update',
    )
    group.add_argument(
        '-i', '--install',
        nargs='+',
        help='run apt install simulation to generate package list which to be installed',
        metavar='package',
        dest='install',
    )
    args = parser.parse_args()

    if args.download :
        dists_download()
    elif args.update :
        dists_update()
    elif args.install :
        simulate_install(args.install)
    else :
        print('Nothing')

if __name__ == "__main__" :
    main()
