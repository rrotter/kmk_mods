from kmk.keys import KC

'''
Modify keymap in place to replace strings w/ Key objects. Also translates
`_______` to `KC.TRNS`.

strings2keys(keyboard.keymap)
'''
def strings2keys(keymap):
    for _, layer in enumerate(keymap):
        for key_idx, key in enumerate(layer):
            if isinstance(key, str):
                if key == '_______':
                    replacement = KC.TRNS
                else:
                    replacement = KC.get(key)
                if replacement is None:
                    raise(f"I don't know what '{key}' is!")
                layer[key_idx] = replacement
