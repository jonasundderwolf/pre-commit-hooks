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
        stages: [push]
    ...
```

`fail_fast` is the option to stop after the first error.

Adding `stages: [push]` for the `check-branch-name-length` hook is probably sufficient.

See https://pre-commit.com/#install for additional information.

## Hooks available

### check-branch-name-length

This hook checks if a branch name exceeds a specific length. 

One way is to set that maximum to some specific value, using `--max 90`, for example to
ensure it is fully displayed in your dev tools or ticket system.

The other way, and why it has been designed, is to limit the branch length to allow 
certbot to emit SSL certificates without errors, for example for review apps. 
You need to specify the subdomain of the review app without the branch name.

Example: `-s .subdomain.domain.de` for desired domain `https://branch-name.subdomain.domain.de`.

By default, it will use certbot maximum domain length of 64, but you overwrite this adding
`--max-length-with-suffix 128`.
