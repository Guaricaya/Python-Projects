import schedule
import datetime
import time

def printar():
    
    print(f'Rodando no Servidor!!!!{datetime.datetime.now()}')
    schedule.every(10).seconds.do(printar)
    return schedule.CancelJob

printar()
while(1):
    schedule.run_pending()