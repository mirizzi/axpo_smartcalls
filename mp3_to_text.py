# %%
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment

# Azure Key Vault URL
vault_url = "https://smartcallkey.vault.azure.net/"

# Create an instance of the secret client
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)
# speech_key= client.get_secret("speech-key").value
class SpeechWorker:
    speech_key ="d7491e71ad04765a20926ae1dc05c3e"

    def recognize_once(self, filename) -> str:
            # Load mp3
            audio = AudioSegment.from_mp3(filename)
            # Export as wav
            audio.export("audio.wav", format="wav")
            audio_config = speechsdk.audio.AudioConfig(filename="audio.wav")
            speech_config = speechsdk.SpeechConfig(subscription="ad7491e71ad04765a20926ae1dc05c3e", region="westeurope")
            speech_config.speech_recognition_language="pt-PT"
            speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

            call=""

            while True:
                out=speech_recognizer.recognize_once()
                #print(out.text)
                if out.reason!=speechsdk.ResultReason.RecognizedSpeech:
                    break
                call= call + " \n " + out.text
                yield out.text
    




# %%



