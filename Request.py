from NluService import NluService
# from CommonFunctions import convert_to_cap_greek
from IntentResponse import IntentResponse
import re 
	# import ipdb; ipdb.set_trace();


class Request:

	def __init__(self, sender_id: str, message_channel, question: str,
				 intent: str = '', parameter: str = '', answer: str = ''):
		self.sender_id = sender_id
		self.message_channel = message_channel
		self.question = question
		self.intent = intent
		self.parameter = parameter
		self.answer = answer
		
	def print(self):
		print(" --------- Req ---------\n\tfrom =", self.sender_id, \
'\n\tquestion =', self.question, '\n\tintent =', self.intent, \
'\n\tparameter =', self.parameter, '\n\tanswer =', self.answer,\
'\n\tmessage channel =', self.message_channel,\
'\n----------------------- \n')

def _shorten_intents(intent):
	if intent:
		#return the last word
		return intent.split()[-1]
	return "no intent"

def action_switcher(intent: str, entity: str):
	# The intents: Analysis_I - ects - grade, Analysis_I - ects - teacher - grade, Analysis_I - grade 
	# have the same behavior, so they can be handled like Analysis_I - grade
	shorted_intent = _shorten_intents(intent)
	if hasattr(IntentResponse,shorted_intent):
		# Use getattr() to dynamically call the method based on the modified intent
		method = getattr(IntentResponse, shorted_intent)
		return method(entity)
	return "I didn't understand the question"

def handle_request(req: Request):
	req.print()
	# get intent from NLU
	nlu = NluService('session_user__#' + req.sender_id)

	req.intent, req.parameter = nlu.get_intent(req.question , req.sender_id)
	# get data, depending on intent
	req.answer = action_switcher(req.intent, req.parameter)

	return req.answer


