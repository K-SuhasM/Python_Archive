from plyer import notification
import time
while True:
    t=int(time.strftime("%H"))
    m=int(time.strftime("%M"))
    print(t,m)
    
    if t % 2==0 and m==00:
         notification.notify(
            title="Drink water!",
            message="This is a reminder to drink water. Stay hydrated.",
            app_name="Reminder",
            timeout=10)
    time.sleep(60)