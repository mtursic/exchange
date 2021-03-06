import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from trader.trader import run_trader

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(run_trader,
                  id='greetings',
                  name='test',
                  trigger='cron',
                  second='*/2',
                  )

atexit.register(lambda: scheduler.shutdown())
