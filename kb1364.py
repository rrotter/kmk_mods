import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# matrix init
keyboard.col_pins = (
    board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8,
    board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
)

keyboard.row_pins = (
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL
