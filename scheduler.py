from apscheduler.schedulers.blocking import BlockingScheduler
import run_once

scheduler = BlockingScheduler()

<<<<<<< HEAD
# TEST MODE: every 2 minutes
scheduler.add_job(run_once.main, 'interval', minutes=2)

print("AI OS Scheduler Started")

scheduler.start()
=======
# Run every day at 11:38 AM
scheduler.add_job(run_once.main, 'interval', minutes=5)

print("AI OS Scheduler Started...")

scheduler.start()
>>>>>>> fba49e2ed82e3084ce601d978ebec102dcec0d6f
