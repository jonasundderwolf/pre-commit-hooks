from __future__ import print_function

import argparse

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output


def get_branch_name():
    try:
        branch = cmd_output('git', 'symbolic-ref', 'HEAD')
    except CalledProcessError:
        return False
    chunks = branch.strip().split('/')
    return '/'.join(chunks[2:])


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--subdomain', type=str,
        help='Subdomain of review app without branch name. '
             'Example: .subdomain.domain.de',
    )
    args = parser.parse_args(argv)

    if not args.subdomain:
        print('Please specify a subdomain with -s.')
        return 1

    branch_name = get_branch_name()

    if branch_name:
        common_name_length = len(branch_name) + len(args.subdomain)
        if common_name_length <= 64:
            return 0
        else:
            print('The commonName is too long. '
                  '({}.{} > 64 chars). Please make your branch name '
                  'shorter.'.format(branch_name, args.subdomain))
            return 1

    else:
        return 1


if __name__ == '__main__':
    exit(main())
