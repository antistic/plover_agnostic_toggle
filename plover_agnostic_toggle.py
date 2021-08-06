#!/usr/bin/env python

from plover import steno
from plover import system

from plover_stroke import BaseStroke


class Stroke(BaseStroke):
    pass


def toggle_key(translator, stroke, cmdline):
    # Toggle keys of previous stroke
    toggles = [key.strip().replace(" ", "") for key in cmdline.split(",")]
    translations = translator.get_state().translations
    if not translations:
        return
    t = translations[-1]
    translator.untranslate_translation(t)

    Stroke.setup(
        system.KEYS, system.IMPLICIT_HYPHEN_KEYS, system.NUMBER_KEY, system.NUMBERS
    )
    keys = Stroke(t.strokes[-1].rtfcre).keys()

    for key in toggles:
        if key in keys:
            keys.remove(key)
        else:
            keys.append(key)

    translator.translate_stroke(steno.Stroke(keys))


def stroke_negative(translator, stroke, cmdline):
    # Toggle ALL keys of previous stroke
    translations = translator.get_state().translations
    if not translations:
        return
    t = translations[-1]
    translator.untranslate_translation(t)

    Stroke.setup(
        system.KEYS, system.IMPLICIT_HYPHEN_KEYS, system.NUMBER_KEY, system.NUMBERS
    )
    keys = Stroke(t.strokes[-1].rtfcre).keys()

    for key in system.KEYS:
        if key in keys:
            keys.remove(key)
        else:
            keys.append(key)

    translator.translate_stroke(steno.Stroke(keys))
