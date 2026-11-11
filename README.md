# Personal task Manager
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)

A simple task manager built with Python for learning git and github

## Feature 
- add multiple tasks
- save tasks
- load save tasks
- admin mode
- set task priority

## Task Priority
each task can have one of this priority levels:
- low
- medium
- high

## Requirements
- python
- python-dotenv


## Project Structure
```text
personal_task_manager1/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   tasks.py
│   
├───gifs
│       gif.gif
│
├───image
│       p1.jpg

```


## Installation
install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Enviroment Setup
create a `.env` file in the project folder

Use `.env.example` as a template

Add your admin password

```env
admin_pass=your_password_here
```

replace `your_password_here` with your own admin password 

## Run the Program
run the main file
```bash
python main.py
```

## Screenshot
![personal_task_manager_screenshot](image\screenshot.jpg)


## Demo
![personal_task_manager_screenshot](gifs\gif1.gif)


nooshika fallah