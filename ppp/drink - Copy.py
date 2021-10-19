from plyer import notification
import time
if __name__ == '__main__':
    while True:
        notification.notify(
            title = 'DRINK WATER NOW',
            message = "HEY! DON'T FORGET TO DRINK WATER",
            app_icon = 'D:/Responsive Website Using HTML CSS JAVASCRIPT/ppp/waterglass.ico',
            timeout = 5
        )
        time.sleep(15)
