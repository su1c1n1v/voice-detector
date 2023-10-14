## Description

It's a simple project that listens to the microphone and prints what you said in the terminal

## How to

- Clone the repository
```shell
git clone https://github.com/su1c1n1v/voice-detector.git
```
- Install the packages
```shell
pip install -r requirements.txt
```
- Run
```shell
python main.py
```

## Additional Information

- The library ```speech_recognition``` uses the default API key, which can be revoked at any moment. In real projects, it's essential to add a valid Google API key.


### Libraries

- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyaudio](https://pypi.org/project/PyAudio/)


### Credits

- [Realpython](https://realpython.com/python-speech-recognition/#installing-speechrecognition)