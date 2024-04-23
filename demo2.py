from google.oauth2 import service_account
from google.cloud import speech

client_file = {API_KEY_FILE_PATH}
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

# Load the audio file
gcs_uri = 'gs://BUCKET_NAME/AUDIO_FILE_NAME'
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='ko-KR',
    # model='video' # enhance quality
)
audio = speech.RecognitionAudio(uri=gcs_uri)

response = client.recognize(config=config, audio=audio)
for result in response.results:
    print(result.alternatives[0].transcript)