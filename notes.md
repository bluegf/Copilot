# Notes

## Generate requirements.txt file
* In VSC, open a Terminal, check you are using the venv and run this command: pip freeze > requirements.txt

## qt.qpa.plugin error:
* Will this be an issue on other platforms?
* Full error:
    qt.qpa.plugin: From 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.
    qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

    Available platform plugins are: minimal, offscreen, linuxfb, wayland-brcm, wayland-egl, wayland, vkkhrdisplay, xcb, eglfs, vnc, minimalegl.

    Aborted (core dumped)
* Execute this command ina Linux Terminal (not the venv/VSC Terminal): sudo apt-get install libxcb-cursor0
