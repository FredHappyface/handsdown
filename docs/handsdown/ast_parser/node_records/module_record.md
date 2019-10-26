# ModuleRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.module_record](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py) module.

Wrapper for an `ast.Module` node with corresponding node info.

- [Handsdown](../../../README.md#-handsdown---python-documentation-generator) / [Modules](../../../MODULES.md#modules) / [Handsdown](../../index.md#handsdown) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / ModuleRecord
    - [ModuleRecord](#modulerecord)
        - [ModuleRecord().build_children](#modulerecordbuild_children)
        - [ModuleRecord().find_record](#modulerecordfind_record)
        - [ModuleRecord().get_title_parts](#modulerecordget_title_parts)
        - [ModuleRecord().iter_records](#modulerecorditer_records)

## ModuleRecord

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L21)

```python
class ModuleRecord(NodeRecord):
    def __init__(source_path: ImportString, import_string: Path) -> None:
```

Wrapper for an `ast.Module` node with corresponding node info.

Responsible for parsing Python source as well.

#### Arguments

- `source_path` - Path to a Python source file.
- `import_string` - File absolute import string.

#### See also

- [ImportString](../../utils/import_string.md#importstring)
- [NodeRecord](node_record.md#noderecord)

### ModuleRecord().build_children

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L147)

```python
def build_children() -> None:
```

Collect full information about Module child records.

Used only when doc for this ModuleRecord is building.

### ModuleRecord().find_record

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L68)

```python
def find_record(import_string: ImportString) -> Optional[NodeRecord]:
```

Find child in the Module by an absolute or relative import string.

#### Attributes

- `import_string` - record import string.

#### Returns

Found child record on None.

#### See also

- [ImportString](../../utils/import_string.md#importstring)
- [NodeRecord](node_record.md#noderecord)

### ModuleRecord().get_title_parts

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L49)

```python
def get_title_parts() -> List[Text]:
```

Get Module title from a splitted `import_string`.

#### Returns

Titles from the top parent to itself.

### ModuleRecord().iter_records

[[find in source code]](https://github.com/vemel/handsdown/blob/master/handsdown/ast_parser/node_records/module_record.py#L88)

```python
def iter_records() -> Generator[NodeRecord, None, None]:
```

Iterate over Module class, method and fucntion records.

#### Yields

A child record.

#### See also

- [NodeRecord](node_record.md#noderecord)