import os
import google.cloud.dialogflow_v2 as dialogflow
import uuid
from credentials import keys_and_credentials
import ipdb
import json

class NluService:

	def __init__(self, session_id: str = 'dibot_'):
		# Authenticate this program
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keys_and_credentials.google_connection
		self.client : dialogflow.SessionsClient = dialogflow.SessionsClient()
		self.session_name : str = session_id

		print('> Started DialogFlow.  //session=', self.session_name)

	def get_intent(self, question: str , session_name2 : str = '0') -> tuple :
		# get intent for question
		current_session = self.client.session_path(keys_and_credentials.project_id, self.session_name + session_name2)
		text_input = dialogflow.types.TextInput(text=question, language_code='en-US')
		query = dialogflow.types.QueryInput(text=text_input)
		response = self.client.detect_intent(session=current_session, query_input=query)
		intent = response.query_result.intent.display_name
		print(intent)
		param_value = ''
		print(response)
		parent_intent = intent.split(' - ')[0]
		for context in response.query_result.output_contexts:
			if 'parameters' in context:
				parameters = context.parameters
				if intent:
					intent_parts = intent.split('_')
					if len(intent_parts) > 1:
						if 'course_name' in parameters and parameters['course_name'] and 'course' in intent_parts[1]:
							param_value = parameters['course_name']
						if 'teacher_name' in parameters and parameters['teacher_name'] and 'teacher' in intent_parts[1]:
							param_value = parameters['teacher_name']
					print(f"Parameter value: {param_value}")
		parameter : str = ''
		if bool(response.query_result.parameters):
			items = list(response.query_result.parameters.items())
			parameter = items[0][1]
		else:
			parameter = param_value
		return intent, parameter