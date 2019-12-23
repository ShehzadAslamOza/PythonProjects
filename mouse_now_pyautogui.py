import pyautogui

print("Press Ctrl-C to quit")
try:
    while True:
        x, y = pyautogui.position()
        color = pyautogui.screenshot().getpixel((x,y))
        color = ' RGB: (' + str(color[0]).rjust(3) + ',' + str(color[1]).rjust(3) + ',' + str(color[2]).rjust(3) + ')'
        positionStr = 'X: ' + str(x).rjust(4) + '  Y:' + str(y).rjust(4) + color
        print(positionStr, end = '')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')