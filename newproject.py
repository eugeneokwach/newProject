import assemblyai as aai

aai.settings.api_key = "490c81cbc64c4866b369e1371bf4b1c0"

FILE_URL = '/Users/eugeneokwach/Downloads/Patrick 5 Min Chunk For Transcription.mp3'

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
