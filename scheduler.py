from apscheduler.schedulers.blocking import BlockingScheduler
import run_once

scheduler = BlockingScheduler()

# TEST MODE: every 2 minutes
scheduler.add_job(run_once.main, 'interval', minutes=2)

print("AI OS Scheduler Started")

scheduler.start()