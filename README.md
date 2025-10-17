
# Random jokes api

Just an api that allows you generate random jokes, using FastAPI and vanilla JS.  

## Technologies used

- Python 3.11+
- FastAPI
- HTML, CSS, JS

## Project structure

app/ # FastAPI server
static/ # HTML, CSS, JS
requirements.txt

## Installation

1. Clone the repository:

```bash
git clone https://github.com/c-dvoid/random_jokes.git
```
======================================================

2. Create a virtual environment and install the requirements:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```
==============================================================

3. Launch the server:

```bash
uvicorn app.main:app --reload
```
==================================

## Funcionality
- Generating random jokes that could boost your mood!