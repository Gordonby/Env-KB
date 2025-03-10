#PiPi-GHERKIN - Raspberry Pi PICO
#Rpi pico keyboard keymap, I used the gherkin keymap as a example :)
print("Keyboard is starting")
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes

envkb = KMKKeyboard()
keyboard = envkb
envkb.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP19, board.GP18, board.GP17, board.GP16)
envkb.row_pins = (board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
envkb.diode_orientation = DiodeOrientation.COLUMNS
envkb.debug_enabled = False
nokey = KC.NO

layers = Layers()
envkb.modules = [layers]

from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
#rgb_ext = RGB(pixel_pin=rgb_pixel_pin, num_pixels=27)
#
rgb_ext = RGB(pixel_pin=board.GP0,
        num_pixels=88,
        val_limit=100,
        hue_default=0
        sat_default=255,
        rgb_order=(1, 0, 2),  # GRB WS2812
        val_default=100,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        reverse_animation=False,
        )
keyboard.extensions.append(rgb_ext)


envkb.keymap = [
    [
    #Layer 0?
        KC.ESC, nokey, KC.F1, KC.F2, KC.F3, KC.F4, nokey, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, nokey, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, nokey, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, nokey, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT, nokey, nokey, nokey,
        KC.LSFT, KC.NONUS_BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, nokey, nokey, KC.UP, nokey,
        KC.LCTL, KC.LGUI, nokey, KC.LALT, nokey, nokey, KC.SPC, nokey,nokey, nokey, KC.RALT, KC.RGUI, nokey, KC.MO(1), KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [
    #Layer 1
        KC.TRNS, nokey, KC.F13, KC.F14, KC.F15, KC.F16, nokey, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24, KC.MUTE, KC.VOLD, KC.VOLU,
        KC.RGB_TOG, KC.RGB_HUI, KC.RGB_HUD, KC.RGB_SAI, KC.RGB_SAD, KC.RGB_VAI, KC.RGB_VAD, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, nokey, nokey, nokey,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey,
        KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey, nokey, nokey, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

#Simple thing to enable LED on pi once this script is executed
import digitalio
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True
#At this point once the LED is enabled the keyboard should be usable

#print("RGB is about to be set")
#import rgb
#exec(open('rgb.py').read())


def usbfunc():
    if __name__ == '__main__':
        print("starting main KB bits")
        envkb.go(hid_type=HIDModes.USB) #Wired USB enable
        raise Exception('Something has caused an error.')
        
try:
    usbfunc()
except Exception as e:
    import supervisor
    print(e)
    led.value = False
    supervisor.reload()

supervisor.reload()
#last ditch effort to reset the MCU, if this is being ran then something really is wrong lol