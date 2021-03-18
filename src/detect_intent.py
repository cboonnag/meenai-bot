import json
import google.cloud.dialogflow_v2 as dialogflow
import os
from google.api_core.exceptions import InvalidArgument

def detectIntentText(intent_text, session_id, language_code = 'th'):

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '../private_key.json'
    DIALOGFLOW_PROJECT_ID = 'meena-th'
    DIALOGFLOW_LANGUAGE_CODE = language_code
    SESSION_ID = session_id

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=intent_text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    print (response.query_result.fulfillment_text)
    return response.query_result.fulfillment_text

if __name__ == "__main__":
    print( detectIntentText("เซนทรัล","me") )