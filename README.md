# Snake Game

A classic Snake game implemented in Python using Pygame, featuring multiple stages with increasing difficulty and obstacles.

## Features

- Multi-stage gameplay with increasing speed and obstacles
- Special fruits that appear every 10 fruits eaten
- Grid-based movement
- Score tracking and stage progression
- High score saving
- Pause functionality (press P)
- Obstacles in higher stages

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShajahanImdaad53/SnakeGame.git
   cd SnakeGame
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

## How to Play

Run the game:
```bash
python Snake.py
```

Use arrow keys to control the snake:
- ↑ Up
- ↓ Down
- ← Left
- → Right

Press P to pause/unpause the game.

Eat fruits to grow and increase your score. Avoid walls, your own body, and obstacles in higher stages.

## Gameplay Video

![Snake Game Demo](Snake%20Game.mp4)

## Building Executable

To build an executable using PyInstaller:

```bash
pyinstaller --onefile Snake.py
```

The executable will be in the `dist/` folder.

## License

MIT License