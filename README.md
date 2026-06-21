<!-- prettier-ignore -->
# Snake Game

![GitHub stars](https://img.shields.io/github/stars/ShajahanImdaad53/SnakeGame?style=social)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Python](https://img.shields.io/badge/python-3.x-blue)

A polished, retro-style Snake game written in Python with Pygame. Play through multiple stages, dodge obstacles, and chase high scores.

Demo
----

If you have a GIF or a short clip, add it to the repo as `assets/demo.gif` and it will render here:

![Gameplay demo](assets/demo.gif)

Highlights
----------

- Multi-stage gameplay with growing difficulty and obstacles
- Special fruits and score multipliers
- Smooth grid-based movement and responsive controls
- Persistent high score saving
- Pause and restart controls
- Ready to build into a standalone executable with PyInstaller

Requirements
------------

- Python 3.8+
- Pygame

Install
-------

Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
pip install --upgrade pip
pip install pygame
```

Run
---

Start the game from the project root:

```powershell
python Snake.py
```

Controls
--------

- Arrow keys: move the snake
- `P`: pause / resume

Packaging (optional)
--------------------

Create a single-file executable with PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile Snake.py
```

The generated executable will appear in the `dist/` directory.

Contributing
------------

Contributions are welcome — open an issue or submit a pull request. Ideas:

- Add new levels or themes
- Add sound effects and music
- Improve AI for obstacles

Credits
-------

Created by ShajahanImdaad53. Inspired by the classic Snake arcade game.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for details.
