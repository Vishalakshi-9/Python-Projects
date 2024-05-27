import win32com.client
 
speaker=win32com.client.Dispatch("SAPI.SpVoice")

w= str("Welcome to Kuku Speaks 1.0 created by Vishalakshi")
print(w)
speaker.Speak(w)
while True:
     x= input("Enter what you want to speak:  ")
     if(x=='z'):
         speaker.Speak("Oops!It's time to go. Bye Bye")
         break
     speaker.Speak(x)
