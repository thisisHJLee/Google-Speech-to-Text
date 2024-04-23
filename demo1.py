import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = {API_KEY_FILE_PATH}
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Load the audio file
audio_file = {AUDIO_FILE_PATH}
with io.open(audio_file, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='ko-KR',
    # model='video' # enhance quality
)

response = client.recognize(config=config, audio=audio)
# print(response)
for result in response.results:
    print(result.alternatives[0].transcript)