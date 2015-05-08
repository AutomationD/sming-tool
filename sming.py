#!/usr/bin/env python3
# coding=utf-8
import os
from jinja2 import Environment, FileSystemLoader
import argparse
from git import Repo
import codecs
from github import Github
from pprint import pprint

PATH = os.path.dirname(os.path.abspath(__file__))

# Args
parser = argparse.ArgumentParser(description='Sming toolbelt', prog='sming')
parser.add_argument(
    '--verbose',
    help='verbose output',
    action='store_true',
    default=False
)

subparsers = parser.add_subparsers(
    dest='operation',
    help='Run sming {command} -h for additional help'
)
subparsers.required = True


# List
init_parser = subparsers.add_parser(
    'list',
    help='List templates'
)


# Init
init_parser = subparsers.add_parser(
    'init',
    help='Project type'
)

init_parser.add_argument(
    'project_name',
    help='Project template to use.'
)

# Show
init_parser = subparsers.add_parser(
    'show',
    help='Show value'
)

init_parser.add_argument(
    'show_value',
    nargs='+',
    help='show.'
)

args = parser.parse_args()


TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(
        searchpath="/"
    ),
    trim_blocks=False)

class Sming:
    def _render_template(self, template_filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

    @staticmethod
    def list_templates():
        g = Github()

        for repo in g.get_user().get_repos():
            if repo.name.startswith("sming-"):
                print(repo.name)
        for repo in g.get_user('anakod').get_repos():
            if repo.name.startswith("sming"):
                print(repo.name)

    @staticmethod
    def clone_template():
        Repo.clone_from('git@github.com:kireevco/sming-'+args.project_name+'.git', args.project_name)

    def create_project(self):
        self.clone_template()

        walk_dir = os.path.join(os.getcwd(), args.project_name)
        for root, subdirs, files in os.walk(walk_dir):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
                if '.git' not in root:
                    context = {'project_name': args.project_name}
                    result = self._render_template(file_path, context)
                    with open(file_path, 'w') as template:
                        print(file_path)
                        print(result)
                        template.write(result)
                    template.close()


def main():
    sming = Sming()
    if args.operation == 'init':
        sming.create_project()
    elif args.operation == 'list':
        sming.list_templates()

########################################

if __name__ == "__main__":
    main()