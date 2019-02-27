import datetime
from string import Template
from platform import system
import argparse
import ui_server


def main(args):
    density_matrix = ui_server.run()

    start_date = find_starting_date()

    commits = generate_commits(start_date, density_matrix)

    bash = substitute_template(args, {"commits": commits})

    with open(f"out.{get_file_ending()}", "w") as output_file:
        output_file.write(bash)


def generate_commits(start_date, density_matrix: list) -> str:
    out = ""
    d = datetime.timedelta(days=1)

    commit_density = [0, 1, 4, 7, 10]

    for density_col in zip(*density_matrix):  # Iter column wise
        for num_commits in density_col:
            for value in range(commit_density[num_commits]):
                out += f"echo {value} >> out.txt\n"
                out += "git add -A\n"
                out += f'git commit -m "Workworkwork" --date {start_date.isoformat()}\n'
            start_date += d
    return out


def substitute_template(args: dict, commits: dict):
    subs = {**args, **commits}
    with open("template.txt") as f:
        template = Template(f.read())
    output = template.substitute(subs)
    return output


def find_starting_date():
    date = datetime.date.today()
    day = datetime.timedelta(days=1)
    while date.weekday() != 6:
        date -= day
    date -= datetime.timedelta(weeks=52)
    return date


def get_file_ending():
    if system() == "Windows":
        return "bat"
    else:
        return "sh"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Draws on the contribution graph of a given Github user's repo."
    )
    parser.add_argument(
        "remote",
        help="A github repository. Ex: https://github.com/yourUser/emptyRepository.git",
    )

    args = vars(parser.parse_args())
    main(args)
