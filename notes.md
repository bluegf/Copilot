# Notes

## Generate requirements.txt file:
* In VSC, open a Terminal, check you are using the venv and run this command: pip freeze > requirements.txt

## qt.qpa.plugin error:
* Will this be an issue on other platforms?
* Full error:<br />
    qt.qpa.plugin: From 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.<br />
    qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.<br />
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.<br />
    <br />
    Available platform plugins are: minimal, offscreen, linuxfb, wayland-brcm, wayland-egl, wayland, vkkhrdisplay, xcb, eglfs, vnc, minimalegl.<br />
    <br />
    Aborted (core dumped)<br />
* Execute this command ina Linux Terminal (not the venv/VSC Terminal): sudo apt-get install libxcb-cursor0
