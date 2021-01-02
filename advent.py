#import modules
import datetime
import http.client, urllib.parse
import picamera

#set up the camera
cam = picamera.PiCamera()
#define the command 'pushover()
def pushover(message):
    print(message)
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "ahbkeq4cke711ywycdr4kje1rum95d",
        "user": "uwnanyz1zryjmscupbbm7tfyn4gbt5",
        "title": "Advent calendar",
        "message": message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

#get the date
date = datetime.date.today().strftime("%d")
month = datetime.date.today().strftime("%m")

#get how long it is untill Christmas
day = int(25) - int(date)
day = str(day)

#check if the month is December
if month == "12":

    #check if it's Christmas
    if day == '0':
        #send the message
        pushover('IT\'S CHRISTMAS!!!')
    else:
        pushover("It's " + day + " days till christmas!")
    #take the photo
    cam.capture('/var/www/html/advent.jpg')
#if its not December, send the message
else:
    pushover('It\'s not December yet!')
