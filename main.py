#!/usr/bin/env python3
from datetime import date, timedelta
import ui_server


def main():
    res = ui_server.run()
    res = ['bla']
    generate_bash(res)


def generate_bash(density_list):
    x = date.today() - timedelta(days=365)
    d = timedelta(days=1)
    for _ in range(365):
        print("git commit --date {}".format(x.isoformat()))
        x = x + d


if __name__ == "__main__":
    main()
