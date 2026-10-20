# Copilot v0.02 20/10/2026

## Description

Program to run when the Copilot key is pressed. Tested on a Linux platform but it should also work on Windows or Mac. It also sets an icon and centres the window on the primary monitor.

## Requirements

* Python 3.xx
* PySide6 Python module <https://pypi.org/project/PySide6/>

## TODO

* Bind to a key on a Windows platform to test it works on Windows

## How To Bind A Program To A Key (Linux Mint 22.2 Cinnamon)

This program is designed to be linked to by a key such as the Copilot key. The steps below are overly verbose, it is a simple process.
  
On Linux Mint 22.2 Cinnamon:

  1. **Start Menu > Peferences > Keyboard**
  2. In the **Keyboard** app, select the **Shortcuts** pane
  3. Click the **Add custom shortcut** button
  4. In the dialog box that opens, put a human readable "Name" in the 1st box. E.g. Copilot
  5. Enter this command to run this program:

          ~/path/to/your/python/.venv/bin/python ~/path/to/main.pyw

        Note: You can use the command that appears in the Terminal pane in VSC when you click the **Run Python File** icon

  6. **Custom Shortcuts** in the left hand menu should now be selected, if not then select it
  7. At the bottom right, in the **Keyboard bindings** pane, click on the top **unassigned**
  8. Click on **unassigned** again so it changes to **Pick an accelerator**
  9. Press the Copilot key (or whatever key you want)
  10. It should now read **Shift+Super+TouchpadOff**
  11. Now, if you press the Copilot key, the program will open  
        Note: I entered **gnome-system-monitor** to run System Monitor (command found in **Properties** for the start menu entry)

To view or edit your custom shortcuts in the future, select "Custom Shortcuts" on the left hand side of the "Keyboard" application.
