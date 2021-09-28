# pre-commit-hooks

Some hooks for pre-commit.

See https://pre-commit.com/ for additional information.

## Using pre-commit-hooks with pre-commit

If you want to use this repository of hooks you need to add a `.pre-commit-config.yaml`
file to the root folder of your project.

This is an example for your `.pre-commit-config.yaml`
```
fail_fast: true
repos:
-   repo: https://github.com/jonasundderwolf/pre-commit-hooks
    rev: v1.0.0
    hooks:
    -   id: check-branch-name-length
        args: [ -s, .subdomain.domain.de ]
    ...
```

`fail_fast` is the option to stop after the first error.

See https://pre-commit.com/#install for additional information.

## Hooks available

### check-branch-name-length

This hook checks if a branch name has a specific length. It has been designed to limit
the branch length to allow certbot to emit SSL certificates without errors, for example 
for review apps. You need to specify the subdomain of the review app without the branch name.

Example: `-s=.subdomain.domain.de` for desired domain `https://branch-name.subdomain.domain.de`
