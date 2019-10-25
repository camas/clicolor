# clicolor

[![PyPI version](https://badge.fury.io/py/clicolor.svg)](https://badge.fury.io/py/clicolor)
[![Build Status](https://travis-ci.org/camas/clicolor.svg?branch=master)](https://travis-ci.org/camas/clicolor)

Quick python reference for terminal color escape codes

## Usage

Install options:

- Install the package `clicolor`

- Add as a submodule

```python
git submodule add https://github.com/camas/clicolor
```

- Or just copy `cli.py` and `LICENSE` somewhere

Then `from clicolor.cli import CLI, ...`

## Examples

```python
print(f"{CLI.BG_YELLOW}{CLI.GREEN}Green on yellow.{CLI.RESET}")
```

![Green text on yellow background example](https://raw.githubusercontent.com/camas/clicolor/master/examples/green_on_yellow.png)

```python
print(f"{CLI.BOLD}{CLI.RED}Bold red.{CLI.RESET}")
```

![Bold red text example](https://raw.githubusercontent.com/camas/clicolor/master/examples/bold_red.png)

```python
print(f"{CLIT.bg(128,0,0)}{CLIT.fg(255,99,71)}Truecolor tomato red on maroon red background{CLI.RESET}")
```

![Truecolor red example](https://raw.githubusercontent.com/camas/clicolor/master/examples/truecolor_red.png)

## test.py

use test.py to run a variety of tests including modifiers, 8/16 colors, 256 colors and Truecolors.
