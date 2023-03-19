# EnvyControl-PyQt
PyQt5 widget for the [EnvyControl](https://github.com/bayasdev/envycontrol), program aimed to provide an easy way to switch GPU modes on Nvidia Optimus systems under Linux. Widget supports both windowed and  system tray mode.


Recored with [Peek](https://github.com/phw/peek)

https://user-images.githubusercontent.com/23504691/218213253-9169b3bb-3d07-43b5-b0dc-fcabe41b2681.mp4

## Dependencies

On Arch Linux/EndeavourOS/Manjaro/Garuda/Artix and other Arch-based:
- PyQt5

```terminal
pip install pyqt5
```

## Installation

1. Make install.sh executable:
a) via GUI on right click Properties --> Permissions --> click `is executable`
b) via terminal - `cd` into the directory with install.sh --> chmod +x  install.sh

2. Run it on double click or in the terminal.

- Autostart

On KDE plasma you can try to add `EnvyControl Qt.dekstopp` file to the autostart in Plasma Settings.
If it's didn't worked, try manually place `EnvyControl Qt.dekstop` file into the `~/.config/autostart` folder.

* You still need to reboot after change of the graphics mode.
