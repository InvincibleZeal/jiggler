import os
import platform
import time
from random import randint
from threading import Thread, current_thread
from time import sleep

import click
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController

mouse = MouseController()
keyboard = KeyboardController()


special_keys = {
    "Darwin": "cmd",
    "Linux": "alt",
    "Windows": "alt",
}


def key_press(seconds):
    """Presses Shift key every x seconds

    Args:
        seconds (int): Seconds to wait between consecutive key press actions
    """
    this = current_thread()
    this.alive = True
    while this.alive:
        sleep(seconds)
        if not this.alive:
            break

        keyboard.press(Key.shift)
        keyboard.release(Key.shift)
        print(f"{time.ctime()}\t[keypress]\tPressed {Key.shift} key")


def switch_screen(seconds, tabs, key):
    """Switches screen windows every x seconds

    Args:
        seconds (int): Seconds to wait between consecutive switch screen actions
        tabs (int): Number of windows to switch at an instant
        key (str) [alt|cmd]: Modifier key to press along with Tab key
    """
    this = current_thread()
    this.alive = True
    while this.alive:
        sleep(seconds)
        if not this.alive:
            break

        modifier = getattr(Key, key)
        with keyboard.pressed(modifier):
            t = tabs if tabs else randint(1, 3)

            for _ in range(t):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
            print(f"{time.ctime()}\t[switch_screen]\tSwitched tab {t} {modifier} {Key.tab}")


def move_mouse(seconds, pixels):
    """Moves mouse every x seconds

    Args:
        seconds (int): Seconds to wait between consecutive move mouse actions
        pixels ([type]): Number of pixels to move mouse
    """
    this = current_thread()
    this.alive = True
    while this.alive:
        sleep(seconds)
        if not this.alive:
            break

        mouse.move(pixels, pixels)
        x, y = list("{:.2f}".format(coord) for coord in mouse.position)
        print(f"{time.ctime()}\t[move_mouse]\tMoved mouse to {x}, {y}")


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-s",
    "--seconds",
    type=int,
    help="Seconds to wait between actions. Default is 10",
    default=10,
)
@click.option(
    "-p",
    "--pixels",
    type=int,
    help="Number of pixels the mouse should move. Default is 1",
    default=1,
)
@click.option(
    "-m",
    "--mode",
    type=click.Choice(["m", "k", "mk", "ks", "ms", "mks"]),
    help="Available options: m, k, mk, ks, ms, mks; default is mks. "
    "This is the action that will be executed when the user is idle at the defined interval: "
    "m -> moves mouse defined number of pixels; "
    "k -> presses shift key on keyboard; "
    "s -> switches windows on screen; ",
    default="mks",
)
@click.option("-t", "--tabs", type=int, help="Number of window tabs to switch screens")
@click.option(
    "-k",
    "--key",
    type=click.Choice(["alt", "cmd"]),
    help="Special key for switching windows",
    default=special_keys[platform.system()],
)
def start(seconds, pixels, mode, tabs, key):

    try:
        threads = []
        if "m" in mode:
            threads.append(Thread(target=move_mouse, args=(seconds, pixels)))

        if "k" in mode:
            threads.append(Thread(target=key_press, args=(seconds,)))

        if "s" in mode:
            threads.append(Thread(target=switch_screen, args=(seconds, tabs, key)))

        for t in threads:
            t.start()

        for t in threads:
            t.join()
    except KeyboardInterrupt as e:
        print("Exiting...")
        for t in threads:
            t.alive = False
        for t in threads:
            t.join()

        print("So you don't need me anymore?")
        os._exit(1)
