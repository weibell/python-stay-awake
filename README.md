# python-stay-awake
Wiggles your mouse to prevent your computer from going to sleep


## Example usage

Setup:
```bash
git clone https://github.com/weibell/python-stay-awake
cd python-stay-awake
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Usage:
```bash
cd python-stay-awake
source venv/bin/activate
python3 stay-awake.py
```

## Additional information
* Simulates minimal mouse movement to prevent the computer from starting the screensaver, going to sleep, etc.
* Makes use of [PyAutoGUI](https://pyautogui.readthedocs.io/) to ensure cross-platform compatibile mouse movements
* Defaults to moving the mouse one pixel back and forth every 3 minutes
* Inspired by https://github.com/Johnson468/Stay-Awake
