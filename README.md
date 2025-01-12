# OLC interview tasks

For python tasks I used python 3.12.
So add project to your `PYTHONPATH`

```bash
  export PYTHONPATH=$PYTHONPATH:/path/to/olc-interview-tasks
```

### Running the tests

```bash
  python -m unittest -b
```

## Snakes and Ladders

This is a simple implementation of the game Snakes and Ladders. For interview purposes, I have implemented the game in
Python. The players take turns to roll a dice and move their respective pieces on the board. The first player to reach
the end of the board wins the game.

### Running the game

```bash
  python snakes_and_ladders/run.py
```

## OOP

In this part of task i created Object representation of HTML elements. Run `python oop/run.py`, and It makes
`oop/index.html` file. You can open it in your browser or do `cd oop && python -m http.server` and open
`http://localhost:8000/` in your browser.

## Database

I selected postgresql for these tasks. Each of the task is in separate file.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)