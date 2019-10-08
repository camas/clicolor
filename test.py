#!/usr/bin/python

from clicolors import CLI, CLI256

# Test modifiers
print()
modifiers = [
    ("Bold", CLI.BOLD, CLI.RESET_BOLD),
    ("Dark", CLI.DARK, CLI.RESET_DARK),
    ("Underline", CLI.UNDERLINE, CLI.RESET_UNDERLINE),
    ("Blink", CLI.BLINK, CLI.RESET_BLINK),
    ("Reverse", CLI.REVERSE, CLI.RESET_REVERSE),
    ("Hidden", CLI.HIDDEN, CLI.RESET_HIDDEN),
]
for disp, set_mod, unset_mod in modifiers:
    print(f"Normal {set_mod}{disp:<10}{unset_mod} Reset {disp}{CLI.RESET}")

print()
header = "      "
for disp, set_a, _ in modifiers:
    header += f" {disp[:4]} {CLI.RESET}"
print(header)
for disp, set_a, _ in modifiers:
    line = f" {disp[:4]} {CLI.RESET}"
    for _, set_b, _ in modifiers:
        line += f"{set_a}{set_b} Text {CLI.RESET}"
    print(line)

# Test clear
print()
print(f"SHOULDNT SEE ME SHOULDNT SEE ME SHOU  SHOULDN'T SEE ME \r{CLI.CLEAR_LINE}Line clear test. Should only see me.")

# Test 8/16 colors
print()
foreground = [(i, f'\033[{i}m') for i in range(30, 38)]
foreground.extend((i, f'\033[{i}m') for i in range(90, 98))
background = [(i, f'\033[{i}m') for i in range(40, 48)]
background.extend((i, f'\033[{i}m') for i in range(100, 108))
for i, code in foreground:
    print(f"{code}{i:<3}{CLI.RESET}", end='')
print()
for i, code in background:
    print(f"{code}{i:<3}{CLI.RESET}", end='')
print()

print()
header = "   "
for i, f in foreground:
    header += f"{f}{i:<3}{CLI.RESET}"
print(header)
for bi, b in background:
    line = f"{b}{bi:<3}{CLI.RESET}"
    for fi, f in foreground:
        line += f"{f}{b}LoL{CLI.RESET}"
    print(line)

print()
c256 = [(i, f'\033[38;5;{i}m') for i in range(0, 256)]
for i, code in c256:
    s = f"{code}{i:<3}"
    if i % 16 == 15:
        s += f"{CLI.RESET}\n"
    print(s, end='')

print()
c256b = [(i, f'\033[48;5;{i}m') for i in range(0, 256)]
for i, code in c256b:
    s = f"{code}{i:<3}"
    if i % 16 == 15:
        s += f"{CLI.RESET}\n"
    print(s, end='')
