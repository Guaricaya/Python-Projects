import schedule
import datetime

def printar():
    
    print(f'Rodando no Servidor!!!!{datetime.datetime.now()}')
    schedule.every(5).seconds.do(printar)
    return schedule.CancelJob

printar()
while(1):
    schedule.run_pending()