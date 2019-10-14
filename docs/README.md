# 🙌 Handsdown - Python documentation generator

- [🙌 Handsdown - Python documentation generator](#%f0%9f%99%8c-handsdown---python-documentation-generator)
  - [🔬 Features](#%f0%9f%94%ac-features)
  - [🎉 Usage](#%f0%9f%8e%89-usage)
    - [💻 From command line](#%f0%9f%92%bb-from-command-line)
    - [🧩 As a module](#%f0%9f%a7%a9-as-a-module)
  - [🐶 Installation](#%f0%9f%90%b6-installation)
  - [🔧 Development](#%f0%9f%94%a7-development)

Python docstring-based documentation generator for lazy perfectionists.

## 🔬 Features

- 👓 PEP257, Google and RST docstrings support. All of them are converted to a valid markdown.
- 🐈 Github-friendly. Use your local markdown viewer or open docs [right on Github](https://github.com/vemel/handsdown/blob/master/docs/README.md#modules)
- 📚 Signatures for every class, function and method.
- 🚀 Support for type annotations. Even for the ones from the `__future__`!
- 📦 Nice list of all modules in [Modules](https://github.com/vemel/handsdown/blob/master/docs/README.md#modules)
- 🔎 Gather all scattered `README.md` in submodules to one place
- 🚧 Links to source code from every doc section.
- #️⃣ Create links easily as [Generator().replace_links](./handsdown_generator.md#generatorreplace_links) (check [Docs index](https://github.com/vemel/handsdown/blob/master/docs/README.md#features))
- 💕 Do you love type annotations? Well, you get auto-discovery of related modules for free!

## 🎉 Usage

### 💻 From command line

Just go to your favorite project that has lots of docstrings but missing auto-generated docs and let `handsdown` do the thing.

```bash
cd ~/my/project

# output buolt MD files to docs/*
handsdown

# or provide custom output: output_dir/*
handsdown -o output_dir

# generate docs only for my_module, but no migrations, plz
handsdown my_module --exclude my_module/migrations
```

Navigate to `docs/README.md` to check your new documentation!

### 🧩 As a module

```python
from handsdown import Generator
from handsdown import PathFinder
repo_path = Path.cwd()

handsdown = Generator(
    input_path=repo_path,
    output_path=repo_path / 'output',
    source_paths=PathFinder(repo_path, "**/*.py").list()
)

# generate all docs at once
handsdown.generate_docs()

# or generate just for one doc
handsdown.generate_doc(repo_path / 'my_module' / 'source.py')

# and generate index.md file
handsdown.generate_index()
```

## 🐶 Installation

Install using pip

```bash
pip install handsdown
```

## 🔧 Development

- Install [pipenv](https://pypi.org/project/pipenv/)
- Run `pipenv install -d`
- Use `black` formatter in your IDE

## Modules

- Handsdown
  - [Main](./handsdown___main__.md)
  - [CLI Parser](./handsdown_cli_parser.md)
  - [Generator](./handsdown_generator.md)
  - [IndentTrimmer](./handsdown_indent_trimmer.md)
  - [Loader](./handsdown_loader.md)
  - [Main](./handsdown_main.md)
  - [MDDocument](./handsdown_md_document.md)
  - [ModuleRecord](./handsdown_module_record.md)
  - [PathFinder](./handsdown_path_finder.md)
  - [Processors](./handsdown_processors_index.md)
    - [Base](./handsdown_processors_base.md)
    - [Pep257](./handsdown_processors_pep257.md)
    - [Rst](./handsdown_processors_rst.md)
    - [SectionMap](./handsdown_processors_section_map.md)
    - [Smart](./handsdown_processors_smart.md)
  - [Signature](./handsdown_signature.md)
  - [Utils](./handsdown_utils.md)