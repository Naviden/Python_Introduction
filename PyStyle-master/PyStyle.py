
def color_guide():
    """shows color code guide

        The color codes should be used in text_formatter() function

        Prints:
             Codes and color previews of Standard, High-intensity and Grayscale color
    """
    print('\n')
    print('\u001b[1mStandard Colors\u001b[0m\n')
    for j in range(0, 8):
        code = str(j)
        print(f"\u001b[48;5;{code}m {code.center(8)}", end='')
    print("\u001b[0m")

    print('\n')
    print('\u001b[1mHigh-Intensity Colors\u001b[0m\n')
    for j in range(8, 16):
        code = str(j)
        print(f"\u001b[48;5;{code}m {code.center(8)}", end='')
    print("\u001b[0m")

    print('\n')
    print('\u001b[1mColors\u001b[0m\n')
    for m in range(0, 6):
        for n in range(0, 36):
            code = str(m * 36 + (n + 16))
            print(f"\u001b[48;5;{code}m {code.ljust(3)}", end='')
        print("\u001b[0m")

    print('\n')
    print('\u001b[1mGrayscale colors\u001b[0m\n')
    for j in range(232, 256):
        code = str(j)
        print(f"\u001b[48;5;{code}m {code.ljust(5)}", end='')
    print("\u001b[0m")


def text_formatter(text:str,
                   bc=None,
                   tc=None,
                   bold:bool=False,
                   underline:bool=False,
                   reversed:bool=False):
    """Add requested style to the fgiven string.

    Adds ANSI Escape codes to add text color, background color and 
    other decorations like bold, undeline and reversed

    Args: 
        text: target string
        bc: Background color code (int)
        tc: Text color code (int)
        bold: if True makes the given string bold
        underline: if True makes the given string undelined
        reversed: if True revreses the background and text colors

    """

    assert isinstance(text, str), f'text should be string not {type(text)}'
    assert isinstance(
        bc, (int, type(None))), f'Background color code should be integer not {type(bc)}'
    assert isinstance(
        tc, (int, type(None))), f'Text color code should be integer not {type(tc)}'
    assert isinstance(
        bold, bool), f'Bold should be Boolean not {type(bold)}'
    assert isinstance(
        underline, bool), f'Underline should be Boolean not {type(underline)}'
    assert isinstance(
        reversed, bool), f'Reversed should be Boolean not {type(reversed)}'

    if bc is not None:
        bc = f'\u001b[48;5;{bc}m'
    else:
        bc = ''
    if tc is not None:
        tc = f'\u001b[38;5;{tc}m'
    else:
        tc = ''
    if bold:
        b = '\u001b[1m'
    else:
        b = ''
    if underline:
        u = '\u001b[4m'
    else:
        u = ''
    if reversed:
        r = '\u001b[7m'
    else:
        r = ''

    return(f'{b}{u}{r}{bc}{tc}{text}\u001b[0m')

# a = text_formatter('asghar',bold=True, underline=False, reversed=True )
# print(a)
