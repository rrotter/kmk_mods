'''
Should save over 200ms off boot time (tested on RP2040) with uncompiled python.
This might make your keyboard boot a little faster. Maybe it will crash.

import kmkx.fast
'''

from kmk.keys import KC, make_mod_key, ALL_ALPHAS, ALL_NUMBERS, Key

def make_key(code, names):
    k = Key(code)
    for name in names:
        KC[name] = k

make_mod_key(0x01, ('LEFT_CONTROL', 'LCTRL', 'LCTL'))
make_mod_key(0x02, ('LEFT_SHIFT', 'LSHIFT', 'LSFT'))
make_mod_key(0x04, ('LEFT_ALT', 'LALT', 'LOPT'))
make_mod_key(0x08, ('LEFT_SUPER', 'LGUI', 'LCMD', 'LWIN'))
make_mod_key(0x20, ('RIGHT_SHIFT', 'RSHIFT', 'RSFT'))
make_mod_key(0x40, ('RIGHT_ALT', 'RALT', 'ROPT'))
make_mod_key(0x80, ('RIGHT_SUPER', 'RGUI', 'RCMD', 'RWIN'))

make_key( 4, ('A', 'a'))
make_key( 5, ('B', 'b'))
make_key( 6, ('C', 'c'))
make_key( 7, ('D', 'd'))
make_key( 8, ('E', 'e'))
make_key( 9, ('F', 'f'))
make_key(10, ('G', 'g'))
make_key(11, ('H', 'h'))
make_key(12, ('I', 'i'))
make_key(13, ('J', 'j'))
make_key(14, ('K', 'k'))
make_key(15, ('L', 'l'))
make_key(16, ('M', 'm'))
make_key(17, ('N', 'n'))
make_key(18, ('O', 'o'))
make_key(19, ('P', 'p'))
make_key(20, ('Q', 'q'))
make_key(21, ('R', 'r'))
make_key(22, ('S', 's'))
make_key(23, ('T', 't'))
make_key(24, ('U', 'u'))
make_key(25, ('V', 'v'))
make_key(26, ('W', 'w'))
make_key(27, ('X', 'x'))
make_key(28, ('Y', 'y'))
make_key(29, ('Z', 'z'))

make_key(40, ('ENTER', 'ENT', '\n', 'RETURN', 'RET')) # BECAUSE THAT'S WHAT IT'S CALLED!
make_key(43, ('TAB', '\t'))
make_key(44, ('SPACE', 'SPC', ' '))
make_key(45, ('MINUS', 'MINS', '-'))
make_key(46, ('EQUAL', 'EQL', '='))
make_key(53, ('GRAVE', 'GRV', 'ZKHK', '`')),
