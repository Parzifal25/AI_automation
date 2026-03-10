from apscheduler.schedulers.blocking import BlockingScheduler
import run_once

scheduler = BlockingScheduler()

# Run every day at 11:38 AM
scheduler.add_job(run_once.main, 'interval', minutes=2)

print("AI OS Scheduler Started...")

scheduler.start()
