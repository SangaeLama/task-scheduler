from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
import datetime
import sys

job_file = sys.argv[1]
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text color to default


# Read the file containing scheduled tasks
def parse_schedule(filename):
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                date_time, command = line.split('|')
                tasks.append((date_time.strip(), command.strip()))
    return tasks

# Schedule tasks from the list
def schedule_task(schedule_date, command):
    def job():
        print(f"{BOLD}Running job: {command}{RESET}")
        subprocess.run(command, shell=True)

    scheduled_time = datetime.datetime.strptime(schedule_date, "%Y-%m-%d %H:%M:%S")
    scheduler.add_job(job, 'date', run_date=scheduled_time)

# Main function
def main():
    file_path = job_file  # Change this to the path of your schedule file
    tasks = parse_schedule(file_path)

    for task in tasks:
        date_time, command = task
        print(f"{BOLD}Scheduling a job: {RESET}{GREEN}{command}{RESET} at {YELLOW}{date_time}.{RESET}")
        schedule_task(date_time, command)

    # Start the scheduler
    scheduler.start()


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    main()

    try:
        while scheduler.get_jobs():
            pass
        print(f"{BOLD}{GREEN}ALL VALID JOBS COMPLETED!!! {RESET}")

    except:
        print(f"{RED}SHUTTING DOWN THE SCHEDULER!!!{RESET}")
        scheduler.shutdown()
