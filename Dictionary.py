from PyDictionary import PyDictionary as Diction
import pyttsx3
import speech_recognition as bot

listener = bot.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
    try:
      with bot.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'bot' in command:
                    print(command)

    except:
        pass
    return command


def run_bot():
    command = take_command()
    if 'synonyms' in command:
        talk('Please tell me the word')
        word = take_command()
        word = word.replace('what is the problem', '')
        word = word.replace('bot', '')
        word = word.replace('synonyms of', '')
        result = Diction.meaning(word)
        print(f'the synonyms for {word} is {result}')
        talk(f'the synonyms for {word} is {result}')
    elif 'antonyms' in command:
        talk('Please tell me the word')
        word = take_command()
        word= word.replace('what is the problem', '')
        word = word.replace('bot', '')
        word = word.replace('antonyms of', '')
        result = Diction.meaning(word)
        print(f'the antonyms for {word} is {result}')
        talk(f'the antonyms for {word} is {result}')

while True:
    run_bot()