# Google-Speech-to-Text

## About
Made this repo because couldn't find a good tutorial for Google Speech-To-Text API
- demo1.py for local audio file
- demo2.py for using Google Storage

## Getting Started
- Service account from Google Cloud Platform project and getting API KEY is required.  
- Download API key file for further credential confirmation.  
- 'sample_rate_hertz' in RecognitionConfig must match the sampling rate of the audio file.
You can check it by following code.
```
$ ffprobe commercial_mono.wav
[...]
Input #0, wav, from 'commercial_mono.wav':
  Duration: 00:00:35.75, bitrate: 128 kb/s
  Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 8000 Hz, 1 channels, s16, 128 kb/s
```

### Installation
```
pip install google-cloud-speech
```

### Acknowledgments
https://youtu.be/izdDHVLc_Z0?si=taqrNl4L4ztEjUGd  
https://cloud.google.com/speech-to-text?hl=en  
https://cloud.google.com/speech-to-text/docs/troubleshooting
