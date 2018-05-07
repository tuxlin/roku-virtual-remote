# roku-virtual-remote

Control your Roku device with your computer and keyboard.

_tested with Python 3.6 and Firefox 59.0.2 only_

## Install
Enable External Control on your Roku device before installing

Settings -> System -> Advanced system settings -> Extrenal Control -> Network Access -> Default or Permissive

Clone the repository

`git clone https://github.com/tuxlin/roku-virtual-remote.git`

`cd roku-virtual-remote`

Create a Python3 virtualenv

`python3 -m venv python`

Activate the virtual environment

`source python/bin/activate`

Install the required pip modules

`pip install -r requirements.txt`


Set your Roku device's IP address in roku-remote.py

```tv = "http://[YOUR TV IP HERE]:8060"```

Start the virtual remote

`python roku-remote.py`


Launch your browser(Firefox 59.0.2+ for keyboard support)

```http://localhost:5000```

## Configure favorites

Add your favorites in the favorites.json file
```
[
  "hulu",
  "netflix",
  "sling tv",
  "hbo go"
]
```
Partially named apps will return all close matching named apps
"hbo" will add "HBO NOW" and "HBO GO" to to the controller's shortcut buttons.

## Keyboard support (Firefox 59.0.2+ only)

* Text entry windows, typing on your keyboard will enter alphanumeric characters(a-z, A-Z, 0-9)
* Backspace will enter backspace on text entry windows
* Arrow keys will move the selector around

### Keyboard shortcuts
| input | key  |
|-------|------|
|select|Enter  |
|back  |Escape |
|home  |F1     |
|volumeDown|-  |
|volumeUp|+    |

## Remote buttons

* All remote buttons function as they do on the actual remote displayed
* Volume controls are on the top right side
* Power off is the only function of the power button

![Alt text](/static/remote.png?raw=true "Optional Title")![Alt text](/static/remote-highlighted-buttons.png?raw=true "Optional Title")


