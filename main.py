import time
t0 = time.monotonic()

from kb1364 import keyboard

import kmkx.fast
from kmkx.opt_overrides import umlaut

from kmk.keys import KC

from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers
# from kmk.modules.modremap import ModRemap
from kmkx.helpers import strings2keys

keyboard.modules.append(ModTap())
keyboard.modules.append(Layers())
# keyboard.modules.append(ModRemap())



# ctrl/esc key
CESC = KC.MT(KC.ESC, KC.LCTRL)

LPRN   = KC.LPRN
RPRN   = KC.RPRN
CARET  = KC['^']
DOLLAR = KC.DOLLAR
HASH   = KC.HASH
BANG   = KC['!']
SLASH  = KC.SLASH

COMMA  = KC.COMMA
DOT    = KC.DOT


CLR    = KC.NUM_LOCK
MO_NUM = KC.MO(1)
TG_NUM = KC.TG(2)
MO_F   = KC.MO(3)

Ä = umlaut(KC.A)
Ö = umlaut(KC.O)
Ü = umlaut(KC.U)

keyboard.keymap = [
    [   # Default Colemak Mod DH Layer
        'XXXXXXX', LPRN,      RPRN,      CARET,     DOLLAR,    'XXXXXXX', KC.GRAVE,  HASH,      BANG,      SLASH,     KC.LBRC,    KC.RBRC,  KC.BSLASH,
        'XXXXXXX', 'Q',       'W',       'F',       'P',       'B',       KC.TAB,    'J',       'L',       Ü,         'Y',        '-',      '=',
        CESC,      Ä,         'R',       'S',       'T',       'G',       KC.BSPC,   'M',       'N',       'E',       'I',        Ö,        KC.QUOTE,
        'LSFT',    'Z',       'X',       'C',       'D',       'V',       MO_NUM,    'K',       'H',       COMMA,     DOT,        'UP',     'RSFT',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'LOPT',    'LCMD',    'ENTER',   'SPACE',   'XXXXXXX', 'RCMD',    'ROPT',    'LEFT',     'DOWN',   'RIGHT'
    ],
    [   # Momentary number layer
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', TG_NUM,    CLR,       KC.PEQL,   KC.PSLS,    KC.PAST,  'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', MO_F,      'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', KC.P7,     KC.P8,     KC.P9,      KC.PMNS,  'XXXXXXX',
        '_______', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', '_______', 'XXXXXXX', KC.P4,     KC.P5,     KC.P6,      KC.PPLS,  'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', '_______', 'XXXXXXX', KC.P1,     KC.P2,     KC.P3,      KC.PENT,  'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', KC.P0,     KC.PDOT,   KC.PDOT,    KC.PENT,  'XXXXXXX'
    ],
    [   # Toggled number layer
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', '_______', TG_NUM,    CLR,       KC.PEQL,   KC.PSLS,    KC.PAST,  'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'UP',      'XXXXXXX', 'XXXXXXX', '_______', 'XXXXXXX', KC.P7,     KC.P8,     KC.P9,      KC.PMNS,  'XXXXXXX',
        '_______', 'XXXXXXX', 'LEFT',    'DOWN',    'RIGHT',   'XXXXXXX', '_______', 'XXXXXXX', KC.P4,     KC.P5,     KC.P6,      KC.PPLS,  'XXXXXXX',
        '_______', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', TG_NUM,    'XXXXXXX', KC.P1,     KC.P2,     KC.P3,      KC.PENT,  'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', '_______', '_______', '_______', '_______', 'XXXXXXX', KC.P0,     KC.PDOT,   KC.PDOT,    KC.PENT,  'XXXXXXX'
    ],
    [   # Momentary F key layer
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', KC.F9,     KC.F10,    KC.F11,   KC.F12,     'XXXXXXX',
        '_______', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', KC.F5,     KC.F6,     KC.F7,    KC.F8,      'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', KC.F1,     KC.F2,     KC.F3,    KC.F4,      'XXXXXXX',
        'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX'
    ],
]

strings2keys(keyboard.keymap)

t1 = time.monotonic()
print(f'Boot time: {t1-t0}')

if __name__ == '__main__':
    keyboard.go()
