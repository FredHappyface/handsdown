# cli_parser

> Auto-generated documentation for [fhdoc.cli_parser](../../fhdoc/cli_parser.py) module.

- [Fhdoc](../README.md#fhdoc-index) / [Modules](../README.md#fhdoc-modules) / [fhdoc](index.md#fhdoc) / cli_parser
    - [abs_path](#abs_path)
    - [dir_abs_path](#dir_abs_path)
    - [existing_dir_abs_path](#existing_dir_abs_path)
    - [git_repo](#git_repo)
    - [parse_args](#parse_args)

## abs_path

[[find in source code]](../../fhdoc/cli_parser.py#L48)

```python
def abs_path(path_str: Text) -> Path:
```

Validate `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

## dir_abs_path

[[find in source code]](../../fhdoc/cli_parser.py#L62)

```python
def dir_abs_path(path_str: Text) -> Path:
```

Validate directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path is not a directory.

## existing_dir_abs_path

[[find in source code]](../../fhdoc/cli_parser.py#L82)

```python
def existing_dir_abs_path(path_str: Text) -> Path:
```

Validate existing directory `path_str` and make it absolute.

#### Arguments

- `path_str` - A path to check.

#### Returns

An absolute path.

#### Raises

- `argparse.ArgumentTypeError` - If path does not exist or is not a directory.

## git_repo

[[find in source code]](../../fhdoc/cli_parser.py#L11)

```python
def git_repo(git_repo_url: Text) -> Text:
```

Validate `git_repo_url` to be a GitHub repo and converts SSH urls to HTTPS.

#### Arguments

- `git_repo_url` - GitHub URL or `remote.origin.url`

#### Returns

A GitHub URL.

## parse_args

[[find in source code]](../../fhdoc/cli_parser.py#L104)

```python
def parse_args(args: List[Text]) -> argparse.Namespace:
```

Get CLI arguments parser.

#### Returns

An `argparse.ArgumentParser` instance.
