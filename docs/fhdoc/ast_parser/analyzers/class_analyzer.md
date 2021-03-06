# class_analyzer

> Auto-generated documentation for [fhdoc.ast_parser.analyzers.class_analyzer](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py) module.

AST analyzer for `ast.ClassDef` records.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../README.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [analyzers](index.md#analyzers) / class_analyzer
    - [ClassAnalyzer](#classanalyzer)
        - [ClassAnalyzer().generic_visit](#classanalyzergeneric_visit)
        - [ClassAnalyzer().visit_Assign](#classanalyzervisit_assign)
        - [ClassAnalyzer().visit_AsyncFunctionDef](#classanalyzervisit_asyncfunctiondef)
        - [ClassAnalyzer().visit_ClassDef](#classanalyzervisit_classdef)
        - [ClassAnalyzer().visit_FunctionDef](#classanalyzervisit_functiondef)

## ClassAnalyzer

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py#L13)

```python
class ClassAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.ClassDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### ClassAnalyzer().generic_visit

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py#L143)

```python
def generic_visit(_node: ast.AST) -> None:
```

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_Assign

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py#L103)

```python
def visit_Assign(node: ast.Assign) -> None:
```

Parse info about class attribute statements.

Adds new `ast.Assign` entry to `attribute_nodes`.
Skips assignments to anything pther that a new variable.
Skips multiple assignments.
Skips assignments with names starting with `_`.

#### Examples

```python
class MyClass:
    MY_MODULE_ATTR = "value"
    my_attr = "value"

    # these entries are skipped
    _MY_MODULE_ATTR = "value"
    multi_attr_1, multi_attr_2 = [1, 2]
    my_object.name = "value"
```

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_AsyncFunctionDef

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py#L85)

```python
def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef) -> None:
```

Parse info about class asynchronous method statements.

Adds new `FunctionRecord` entry to `method_records`.

#### Examples

class MyClass:
    async def my_method(self, arg):
        return await arg

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_ClassDef

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py#L26)

```python
def visit_ClassDef(node: ast.ClassDef) -> None:
```

Entrypoint for the analyzer.

Adds new `ast.expr` entry to `decorator_nodes` for each node
from `node.decorator_list`.
Adds new `ast.expr` entry to `base_nodes` for each node
from `node.bases`.
Visits each node from `node.body` list to parse methods.

#### Examples

```python
def my_func():
    pass
```

#### Arguments

- `node` - AST node.

### ClassAnalyzer().visit_FunctionDef

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/class_analyzer.py#L67)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

Parse info about class method statements.

Adds new `FunctionRecord` entry to `method_records`.

#### Examples

class MyClass:
    def my_method(self, arg):
        return arg

#### Arguments

- `node` - AST node.
