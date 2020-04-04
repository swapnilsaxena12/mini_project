import pyttsx3
importspeech_recognition as sr #pip install speechRecognition
importdatetime
importwikipedia #pip install wikipedia
importwebbrowser
importos
importsmtplib
from selenium import webdriver
frompynput.mouse import Button , Controller

m = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
engine.say(audio)
engine.runAndWait()

defwishMe():
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
speak("Good Morning!!!")

elif hour>=12 and hour<18:
speak("Good Afternoon!!!!")
else:
speak("Good Evening!!!!!")
speak("I am Jarvis. Please tell me how may I help you")

deftakeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
withsr.Microphone() as source:
print("Listening...")
r.pause_threshold = 1
audio = r.listen(source)

try:
print("Recognizing...")
query = r.recognize_google(audio, language='en-in')
print(f"User said: {query}\n")
if 'how are you' not in query and 'tell me about yourself' not in query and "sing for me" not in query:
speak(query)

except Exception as e:
        # print(e)
speak("Say that again please...")
return "None"
return query

def sendEmail(to, content):
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('swapnilsaxena1998@gmail.com', '830@yaswapnil')
server.sendmail(‘swapnilsaxena1998@gmail.com', to, content)
server.close()
if __name__ == "__main__":
wishMe()
while True:
    # if 1:
query = takeCommand().lower()

 # Logic for executing tasks based on query
if 'wikipedia for' in query:
speak('Searching Wikipedia...')
query = query.split(" ")
location = query[2:]
location=' '.join(location)
webbrowser.open('https://en.wikipedia.org/wiki/'+ location)
text = wikipedia.summary(query)
print(text)
speak(text)

elif 'this' in query:
query = query.split(" ")
            c=query[1:]
location=' '.join(c)

webbrowser.open('https://www.youtube.com/results?search_query=' + location)
elif 'open google' in query:
webbrowser.open("google.com")

elif 'open stackoverflow' in query:
webbrowser.open("stackoverflow.com")

elif 'open gla website' in query:
webbrowser.open("www.gla.ac.in")
elif 'how are you' in query:
speak('i am fine what can i do  for you')

elif 'tell me about yourself' in query:
speak('i am jarvis your personal virtual assistant created to help you')

elif 'open youtube on' in query:
query=query.split(" ")
location = query[3:]
location=' '.join(location)
webbrowser.open("https://www.youtube.com/results?search_query=" + location)
m.position = (395,306)
for _ in range(10000):
for i in range(10000):
pass
m.press(Button.left)
m.release(Button.left)

elif "where is" in query:
query = query.split(" ")

location = query[2:]
location=' '.join(location)
speak("Hold on Sir, I will show you where " + location + " is.")
webbrowser.open('https://www.google.com/maps/place/'+ location)
elif "record audio" in query:
            r = sr.Recognizer()
withsr.Microphone() as source:
speak("Say something!")
audio = r.listen(source)
        # Speech recognition using Google Speech Recognition
            data = ""
try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
data = r.recognize_google(audio)
speak("i recorded: " + data)

speak("do you want to save this audio")
withsr.Microphone() as s:
ad=r.listen(s)
                y=r.recognize_google(ad)
if "yes" in y:
speak("file has been successfully saved")
exceptsr.UnknownValueError:
print("Google Speech Recognition could not understand audio")
exceptsr.RequestError as e:
print("Could not request results from Google Speech Recognition service; {0}".format(e))

elif 'open playlist' in query:
music_dir = "C:\\Users\\This PC\\Desktop\\new\\"
songs = os.listdir(music_dir)
print(songs)
os.startfile(os.path.join(music_dir, songs[0]))

elif 'the time' in query:
strTime = datetime.datetime.now().strftime("%H:%M:%S")
speak(f"Sir, the time is {strTime}")

elif 'open code' in query:
codePath = "C:\\Users\\This PC\\Desktop\\jarvis.py"
os.startfile(codePath)

elif 'email to annan' in query:
try:
speak("What should I say?")
content = takeCommand()
to = "mohd.annanjix@gmail.com"
sendEmail(to, content)
speak("Email has been sent!")
except Exception as e:
print(e)
speak("Sorry my friend. I am not able to send this email")

elif 'email to palak' in query:
try:
speak("What should I say?")
content = takeCommand()
to = "palak.agarwal_cs17@gla.ac.in"

sendEmail(to, content)
speak("Email has been sent!")
continue
except Exception as e:
print(e)
speak("Sorry my friend. I am not able to send this email")
elif 'priyanka' in query:
try:
speak("What should I say?")
content = takeCommand()
to = "priyanka.gupta_cs17@gla.ac.in"
sendEmail(to, content)
speak("Email has been sent!")
continue
except Exception as e:
print(e)
speak("Sorry my friend. I am not able to send this email")
elif 'email to priyanka' in query:
try:
speak("What should I say?")
content = takeCommand()
to = "priyanshu.jain_cs17@gla.ac.in"
sendEmail(to, content)
speak("Email has been sent!")
continue
except Exception as e:
print(e)
speak("Sorry my friend. I am not able to send this email")

elif 'email to myself' in query:
try:
speak("What should I say?")
content = takeCommand()
to = "swapnil.saxena_cs17@gla.ac.in"
sendEmail(to, content)
speak("Email has been sent!")
continue
except Exception as e:
print(e)
speak("Sorry my friend. I am not able to send this email")

elif 'email to ayushi' in query:
try:
speak("What should I say?")
content = takeCommand()
to = "ayushisaxenalko@gmail.com"
sendEmail(to, content)
speak("Email has been sent!")
continue
except Exception as e:
print(e)
speak("Sorry my friend harry bhai. I am not able to send this email")
elif 'tell me about' in query:
try:
speak('this is what i found')
query=query.split(" ")
content=query[3:]
webbrowser.open('https://www.google.com/search?q=' + str(*content))
except Exception as e:
print(e)
speak("sorry")

elif 'good job jarvis' in query:
speak('thank you sir')
elif 'open word' in query:
speak("opening Microsoft word")

os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk')
elif 'open Excel' in query:
speak("opening Microsoft Excel")
os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk')
elif 'open powerpoint' in query:
speak("opening Microsoft powerpoint")
os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Powerpoint 2010.lnk')
elif 'open notepad' in query:
speak("opening windows notepad")
os.startfile('C:\\Users\\This PC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk')
elif "shutdown" in query:
speak("do you wish to shutdown your computer")
speak("press enter to shutdown!")
os.system("shutdown /s /t 1")
