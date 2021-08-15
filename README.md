# Jiggler

Don't ever let your system sleep again.
This program moves your mouse, presses keys on your keyboard and switches screens for you while you rest.

[![asciicast](https://asciinema.org/a/430517.svg)](https://asciinema.org/a/430517)

## Install with pip

```bash
pip install jiggler
```

**Note** - For Linux or macOS, use `pip3` instead of `pip`

> Incase you face any errors with installing `pynput` as a dependency try installing it separately via `pip install pynput`

## Usage

Open command prompt or terminal and type -

```bash
jiggler
```

and that's it.

### Configuration Options

```
Options:

-s, --seconds INTEGER           Seconds to wait between actions.
                                Default is 10

-p, --pixels INTEGER            Number of pixels the mouse should move.
                                Default is 1

-m, --mode [m|k|mk|ks|ms|mks]   Available options: m, k, mk, ks, ms, mks;
                                default is mks.
                                This is the action that execites when the
                                user is idle at the defined interval.
                                m -> moves mouse defined number of pixels;
                                k -> presses shift key on keyboard;
                                s -> switches windows on screen;

-t, --tabs INTEGER              Number of window tabs to switch screens

-k, --key [alt|cmd]             Special key for switching windows

--help                          Show this message and exit.

```
