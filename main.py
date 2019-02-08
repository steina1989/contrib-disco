#!/usr/bin/env python3
import datetime
import ui_server


def main():
    res = ui_server.run()
    generate_bash(res)


def generate_bash(density_list):
    pass

if __name__ == "__main__":
    main()
