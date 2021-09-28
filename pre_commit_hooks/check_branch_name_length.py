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
    parser.add_argument(
        '-m', '--max', type=int,
        help='Maximum branch name length (mutually exclusive with -s)',
    )
    parser.add_argument(
        '--max-length-with-suffix', type=int, default=64,
        help='Maximum branch name length including suffix, default 64',
    )
    args = parser.parse_args(argv)

    if not bool(args.subdomain) ^ bool(args.max):
        print('Please specify a subdomain with -s OR a maximum branch length with -m')
        return 1

    branch_name = get_branch_name()

    if not branch_name:
        print('Can\'t get branch name from git. Are you in a git-tracked repository? Not in detached head?')
        return 1
    if args.max:
        if len(branch_name) <= args.max:
            return 0
        print(f'The branch name {branch_name} is longer as the allowed {args.max} length.')
        return 1
    if len(branch_name) + len(args.subdomain) <= args.max_length_with_suffix:
        return 0
    print('The commonName is too long. '
          f'({branch_name}.{args.subdomain} > {args.max_length_with_suffix} chars). '
          'Please make your branch name shorter.')
    return 1


if __name__ == '__main__':
    exit(main())
