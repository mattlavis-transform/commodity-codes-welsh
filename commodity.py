from googletrans import Translator
from google.cloud import translate
from google.oauth2 import service_account
from dotenv import load_dotenv
import os


class Commodity(object):
    def __init__(self, sid, id, pls, description):
        self.sid = sid
        self.id = id
        self.pls = pls
        self.description = description.lstrip("- ")
        self.description = self.description.replace('"', "")
        self.description_welsh = ""

    def x_translate(self):

        translator = Translator()
        res = translator.translate(self.description, src='en', dest='cy')
        self.description_welsh = res.text
        print(self.description_welsh)
        
        self.extract = str(self.sid) + ',"' + str(self.id) + '","'  + str(self.pls) + '","' + self.description + '","' + self.description_welsh + '"' + "\n"


    def translate(self, project_id="civic-cedar-304921"):
        load_dotenv('.env')
        self.project_id = os.getenv('PROJECT_ID')
        credentials = service_account.Credentials.from_service_account_file("Tariff Welsh Translation-9272e3628404.json")
        client = translate.TranslationServiceClient(credentials=credentials)
        location = "global"
        parent = f"projects/{self.project_id}/locations/{location}"

        # Detail on supported types can be found here:
        # https://cloud.google.com/translate/docs/supported-formats
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [self.description],
                "mime_type": "text/plain",  # mime types: text/plain, text/html
                "source_language_code": "en-GB",
                "target_language_code": "cy",
            }
        )

        # Display the translation for each input text provided

        try:
            self.description_welsh = response.translations[0].translated_text
            print(self.description_welsh)
        except:
            pass

        # for translation in response.translations:
        #     print("Translated text: {}".format(translation.translated_text))
        self.extract = str(self.sid) + ',"' + str(self.id) + '","'  + str(self.pls) + '","' + self.description + '","' + self.description_welsh + '"' + "\n"
