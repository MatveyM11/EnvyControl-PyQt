# EnvyControl-PyQt
PyQt5 widget for the [EnvyControl](https://github.com/bayasdev/envycontrol), program aimed to provide an easy way to switch GPU modes on Nvidia Optimus systems under Linux. Widget supports both windowed and  system tray mode.


Recored with [Peek](https://github.com/phw/peek)

https://user-images.githubusercontent.com/23504691/218213253-9169b3bb-3d07-43b5-b0dc-fcabe41b2681.mp4


- To run it with .desktop file:

1. Make it executable
2. Add fullpath to the script and icon in this lines -

```desktop
Exec=python3 /full path to the script/envycontrol_qt.py
Icon=/full path to the icon/envycontrol.png
```

- Autostart

On KDE plasma you can try to add `EnvyControl Qt.dekstopp` file to the autostart in Plasma Settings.
If it's didn't worked, try manually place `EnvyControl Qt.dekstop` file into the `~/.config/autostart` folder.

* You still need to rebood after change of the graphics mode.
