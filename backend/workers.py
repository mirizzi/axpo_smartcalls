import azure.cognitiveservices.speech as speechsdk


class SpeechWorker:
    def __init__(
        self,
        speech_api_key: str,
        speech_service_region: str = "westeurope",
    ):
        self.speech_api_key = speech_api_key
        self.speech_service_region = speech_service_region
        self.speech_config = speechsdk.SpeechConfig(
            subscription=self.speech_api_key, region=self.speech_service_region
        )

    def recognize_once(self, filename) -> str:
        audio_config = speechsdk.AudioConfig(filename=filename)
        recognizer = speechsdk.SpeechRecognizer(
            self.speech_config, audio_config, language="???"
        )
        while True:
            # do something and get text
            yield text
