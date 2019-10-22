#!/usr/bin/python

import colorsys

from clicolors import CLI, CLI256, CLIT

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
print((f"{' ' * 46}SHOULDN'T SEE ME \r{CLI.CLEAR_LINE}Line clear test."
       f" Should see nothing after me."))

# Test 8/16 colors
print()
foreground = [(i, CLI.from_val(i)) for i in range(30, 38)]
foreground.extend((i, CLI.from_val(i)) for i in range(90, 98))
background = [(i, CLI.from_val(i)) for i in range(40, 48)]
background.extend((i, CLI.from_val(i)) for i in range(100, 108))
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

# Test 256 colors
print()
c256 = [(i, CLI256.fg(i)) for i in range(0, 256)]
for i, code in c256:
    s = f"{code}{i:<3}"
    if i % 6 == 3:
        s += f"{CLI.RESET}\n"
    print(s, end='')

print()
c256b = [(i, CLI256.bg(i)) for i in range(0, 256)]
for i, code in c256b:
    s = f"{code}{i:<3}"
    if i % 6 == 3:
        s += f"{CLI.RESET}\n"
    print(s, end='')

print()
for i in [16, 52, 88, 124, 160, 196]:
    print(CLI256.bg(i) + " ", end='')
for i in reversed([16, 52, 88, 124, 160, 196]):
    print(CLI256.bg(i) + " ", end='')
print(f"{CLI.RESET}")
for i in [16, 22, 28, 34, 40, 46]:
    print(CLI256.bg(i) + " ", end='')
for i in reversed([16, 22, 28, 34, 40, 46]):
    print(CLI256.bg(i) + " ", end='')
print(f"{CLI.RESET}")
for i in range(16, 22):
    print(CLI256.bg(i) + " ", end='')
for i in range(21, 15, -1):
    print(CLI256.bg(i) + " ", end='')
print(f"{CLI.RESET}")

# Test truecolors
print()
print(''.join(f"{CLIT.bg(i, 0, 0)} " for i in range(0, 256, 2)), end='')
print(f"{CLI.RESET}")
print(''.join(f"{CLIT.bg(0, i, 0)} " for i in range(0, 256, 2)), end='')
print(f"{CLI.RESET}")
print(''.join(f"{CLIT.bg(0, 0, i)} " for i in range(0, 256, 2)), end='')
print(f"{CLI.RESET}")

print()
line = ""
for i in range(4096):
    r, g, b = colorsys.hsv_to_rgb(i / 4096.0 * 0.85, 1.0, 1.0)
    line += CLIT.bg(int(r * 255), int(g * 255), int(b * 255)) + " "
    if i % 128 == 127:
        line += CLI.RESET + "\n"
print(f"{line}{CLI.RESET}")
