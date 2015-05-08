#!/usr/bin/env python3
# coding=utf-8
import os
from jinja2 import Environment, FileSystemLoader
import argparse
from git import Repo
from pprint import pprint
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(PATH, os.path.join('templates'))
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
    loader=FileSystemLoader(TEMPLATE_PATH),
    trim_blocks=False)
# print(os.path.join(PATH, os.path.join('templates', args.filename)))


class Sming:
    def _render_template(self, template_filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

    def clone_template(self):
        Repo.clone_from('git@github.com:kireevco/sming-sample_project.git', args.project_name)

    def create_project(self):
        walk_dir = os.path.join(TEMPLATE_PATH,args.project_name)
        #
        # print('walk_dir = ' + walk_dir)
        #
        # # If your current working directory may change during script execution, it's recommended to
        # # immediately convert program arguments to an absolute path. Then the variable root below will
        # # be an absolute path as well. Example:
        # # walk_dir = os.path.abspath(walk_dir)
        # print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
        #
        # for root, subdirs, files in os.walk(walk_dir):
        #     print('--root (relative) = ' + os.path.relpath(root, walk_dir))
        #     print('--\nroot = ' + root)
        #     list_file_path = os.path.join(root, 'my-directory-list.txt')
        #     print('list_file_path = ' + list_file_path)
        #
        #     # os.mkdir(os.path.join(os.getcwd(),os.path.relpath(root, walk_dir)))
        #     # print('creating '+os.path.join(os.getcwd(),os.path.relpath(root, walk_dir)))
        #
        #     with open(list_file_path, 'wb') as list_file:
        #         for subdir in subdirs:
        #             print('\t- subdirectory ' + subdir)
        #
        #         for filename in files:
        #             file_path = os.path.join(root, filename)
        #
        #             print('\t- file %s (full path: %s)' % (filename, file_path))
        #
        #             with open(file_path, 'rb') as f:
        #                 context = {'project_name':'test'}
        #                 f_content = f.read()
        #                 list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
        #                 list_file.write(f_content)
        #                 list_file.write(b'\n')
        #                 #os.path.join(os.getcwd(),filename)
        #                 html = self._render_template(os.path.join(root,filename), context)
        #                 print(html)
        #                 f.write(html)
        #







def main():
    sming = Sming()
    sming.clone_template()
    # sming.create_project()

########################################

if __name__ == "__main__":
    main()