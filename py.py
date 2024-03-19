import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""

if __name__ == "__main__":
    speak("Hey Nova, what's the weather like today?")
    weather_query = listen()

    if "weather" in weather_query:
        speak("Good morning! It's a beautiful Tuesday morning. Sunny skies with a high of 72 degrees Fahrenheit.")
        speak("Perfect, I was thinking about going for a run this afternoon.")
        speak("Sounds like a great plan! There's a low chance of rain, but you might want to bring some sunscreen.")

    speak("Oh, and Nova, is there anything on my calendar for today?")
    calendar_query = listen()

    if "calendar" in calendar_query:
        speak("Let me see. You have a dentist appointment at 3 pm and a team meeting at 10 am.")
        speak("Ugh, a dentist appointment. Can you remind me 30 minutes before?")
        speak("Certainly, I can set a reminder for 2:30 pm for your dentist appointment.")

    speak("Last thing, Nova, what are some trending news stories this morning?")
    news_query = listen()

    if "news" in news_query:
        speak("Absolutely. The top story right now is about the launch of a new space telescope. Would you like to hear the details?")
        speak("(Plays a short news clip about the space telescope launch)")
        speak("Wow, that's amazing! Thanks for the update, Nova.")

    speak("You're welcome! Is there anything else I can help you with today?")

    while True:
        query = listen()

        if "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")
