# Copilot v0.01 20/12/2025

## Description:
Program to run when the Copilot key is pressed. This program has been designed to be executed when a key is pressed (The Copilot key) on a Linux platform but it should also work on Windows or Mac. It also sets an icon and centres the window on the primary monitor.

## TODO:
* Bind to a key on a Windows platform to test it works on Windows

## How To Bind A Program To A Key (Linux Mint 22.2 Cinnamon):
This program is designed to be linked to a key such as the Copilot key.<br />
On Linux Mint 22.2 Cinnamon:<br />
    1. Start Menu > Peferences > Keyboard<br />
    2. In the Keyboard app, select the "Shortcuts" pane<br />
    3. Click the "Add custom shortcut" button<br />
    4. In the dialog box that opens, put a human readable "Name" in the 1st box. E.g. Copilot<br />
    5. Enter this command to run this program: "$HOME/Programming/GitHub/Python/Copilot/.venv/bin/python $HOME/Programming/GitHub/Python/Copilot/src/main.pyw"<br />
        (note: this is the command that appears in the Terminal window in VSC when you click the "Run Python File" icon)<br />
    6. "Custom Shortcuts" in the left hand menu should now be selected, if not then select it<br />
    7. At the bottom right, in the "Keyboard bindings" pane, click on the top "unassigned"<br />
    8. Click on "unassigned" again so it changes to "Pick an accelerator"<br />
    9. Press the Copilot key (or whatever key you want)<br />
    10. It should now read "Shift+Super+TouchpadOff"<br />
    11. Now, if you press the Copilot key, the program will open<br />
    Note: I entered "gnome-system-monitor" to run System Monitor (command found in Properties for the start menu entry)<br />
To view or edit your customer shortcuts in the future, select "Custom Shortcuts" on the left hand side of the "Keyboard" application<br />
