import time
t0 = time.monotonic()

from kb1364 import keyboard

import kmkx.fast
from kmkx.opt_overrides import umlaut

from kmk.keys import KC, Key

from kmk.modules.modtap import ModTap
from kmk.modules.layers import Layers
from kmkx.modules.modremap import ModRemap, ModRemapMeta
from kmkx.helpers import strings2keys

remap = ModRemap()

keyboard.modules.append(ModTap())
keyboard.modules.append(Layers())
keyboard.modules.append(remap)



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

'''
 label Base  None    Shift   Opt       Shift-Opt
 (     9     +shift  ,       w+shift   \ -shift
 )     0     +shift  .       [         \
 &     6     +shift  7       [+shift   None
 $     4     +shift  5       2+shift   None
 #     3     +shift  2       no ∆      None
 !     1     +shift  /       no ∆      /
'''

lprn = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: s and a, KC.BSLASH, {KC.LSFT,KC.RSFT}),
        (lambda c,s,a,g: s, KC['<']),
        (lambda c,s,a,g: a, KC.LSFT(KC.W)),
        (lambda c,s,a,g: True, KC['(']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


rprn = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: s and a, KC.BSLASH),
        (lambda c,s,a,g: s, KC['>']),
        (lambda c,s,a,g: a, KC['[']),
        (lambda c,s,a,g: True, KC[')']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


caret = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: s and a, KC.N6, {KC.LSFT,KC.RSFT}),
        (lambda c,s,a,g: a, KC['{']),
        (lambda c,s,a,g: s, KC['&']),
        (lambda c,s,a,g: True, KC['^']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


dollar = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: s and a, KC.N5, {KC.LSFT,KC.RSFT}),
        (lambda c,s,a,g: a, KC['@']),
        (lambda c,s,a,g: s, KC.N5),
        (lambda c,s,a,g: True, KC['$']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


hsh = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: a, KC.N3, {KC.LSFT,KC.RSFT}),
        (lambda c,s,a,g: s, KC.N2),
        (lambda c,s,a,g: True, KC['#']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


bang = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: s and a, KC['/']),
        (lambda c,s,a,g: s, KC['/']),
        (lambda c,s,a,g: a, KC.N1),
        (lambda c,s,a,g: True, KC['!']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


slash = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: not s and not a, KC['/']),
        (lambda c,s,a,g: True, KC.N8),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


lbrc = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: g and a, KC['{'], {KC.LALT,KC.RALT}),
        (lambda c,s,a,g: True, KC['[']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


rbrc = Key(
    code=9999,
    has_modifiers=None,
    meta=ModRemapMeta([
        (lambda c,s,a,g: g and a, KC['}'], {KC.LALT,KC.RALT}),
        (lambda c,s,a,g: True, KC[']']),
    ]),
    on_press=remap.press,
    on_release=remap.release
)


keyboard.keymap = [
    [   # Default Colemak Mod DH Layer
        'XXXXXXX', lprn,      rprn,      caret,     dollar,    'XXXXXXX', KC.GRAVE,  hsh,      bang,      slash,     lbrc,       rbrc,     KC.BSLASH,
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
