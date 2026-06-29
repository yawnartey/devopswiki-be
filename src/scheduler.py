from apscheduler.schedulers.background import BackgroundScheduler
from crawler import crawl

scheduler = BackgroundScheduler()
scheduler.add_job(crawl, 'interval', hours=24)
