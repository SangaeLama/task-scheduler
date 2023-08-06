# Task Scheduler

Task Scheduler is a Python script that reads a schedule file containing specific dates, times, and commands to run. It uses the apscheduler library to schedule these tasks for execution in the background.

## Requirements

- Python 3.x
- apscheduler library (install using `pip install apscheduler`)

## Usage

1. Create a text file named `jobs.txt` in the same directory as the script.
2. Each line in `jobs.txt` should follow the format: `YYYY-MM-DD HH:MM:SS | your_command_here`. For example:
3. Run the script using the following command, providing the schedule file as an argument:

python task_scheduler.py jobs.txt

4. The script will read the schedule from the specified file and execute the specified commands at the specified dates and times.

## Features

- Scheduled tasks are executed in the background.
- The script provides colorful and bold terminal output for easy identification of job scheduling and execution.

## Example

Suppose you have the following `jobs.txt` file with following lines:

`2023-08-10 15:30:00 | echo "Hello world!!!" > hello.txt`

`2023-08-11 03:30:00 | python3 -m http.server` 

Running `scheduler.py jobs.txt` will schedule the commands 
`echo "Hello world!!!" > hello.txt` to run on August 10, 2023, at 3:30 PM 
and 
`python3 -m http.server` to run on August 11, 2023, at 3:30 AM.

## Notes

- Lines starting with `#` in the schedule file are considered comments and will be ignored by the script.
- Ensure that the required commands and arguments are correctly specified in the schedule file.
- Make sure your system's timezone settings are accurate to ensure proper scheduling.

## Author
Sangay Lama
