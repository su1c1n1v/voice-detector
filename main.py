import speech_recognition as sr

# Version of the speech_recognition library
# print(sr.__version__)

# List all the microphones connected to your computer
# print(sr.Microphone.list_microphone_names())

# Function to listen to the microphone
def listen():
    # Create a recognizer object
    r = sr.Recognizer()

    # Create a microphone object using the default mic
    mic = sr.Microphone()

    while(True):
        # Listen to the microphone
        print("Listening...")

        try:
            with mic as source:
            # Remove ambient noise
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            # To use API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            text = r.recognize_google(audio)
            print(text)

            if(text == "exit"):
                break

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

listen()