#!/usr/bin/env python3
from datetime import date, timedelta
from string import Template
import argparse
import ui_server


def main(args):
    density_matrix = ui_server.run()

    commits = generate_commits(density_matrix)

    bash = substitute_template(args, commits)

    print(bash)


def generate_commits(density_matrix: list) -> dict:
    out = ""
    x = date.today() - timedelta(days=365)
    d = timedelta(days=1)
    for density_col in zip(*density_matrix):  # Iter column wise
        for num_commits in density_col:
            out += f"git commit --date {x.isoformat()}"
            out += "\n"
        x = x + d

    return {"commits_modifications": out}


def substitute_template(args: dict, commits: dict):
    subs = {**args, **commits}
    with open('template.txt') as f:
        template = Template(f.read())
    output = template.substitute(subs)
    return output


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Draws on the contribution graph of a given Github user's repo.")
    parser.add_argument("remote")

    args = vars(parser.parse_args())
    main(args)
