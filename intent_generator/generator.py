import uuid
import json
from itertools import product
from intents_data_helper import IntentsDataHelper
import sys
sys.path.append('../config')
from Intents import *

class DialogFlowGenerator():
    @staticmethod
    def generate_intent_with_followups(intent_name, children, intent_data, followup, shared_usersays):
        root_uuid = str(uuid.uuid4())
        root_unified_name = ''.join(intent_name.split()) 
        root_context_name = root_unified_name + '-followup'
        # First write the root intent
        root_json_data = {
            'id': root_uuid,
            'name': intent_name,
            'auto': True,
            'contexts': [],
            'responses': [
                {
                    'resetContexts': False,
                    'action': '',
                    'affectedContexts': [
                        {
                            'name': root_context_name,
                            'lifespan': 5
                        }
                    ],
                    'parameters': [],
                    'messages': [
                        {
                            'type': '0',
                            'title': '',
                            'textToSpeech': '',
                            'lang': 'en',
                            'condition': ''
                        }
                    ],
                    'speech': []
                }
            ],
            'priority': 500000,
            'webhookUsed': False,
            'webhookForSlotFilling': False,
            'fallbackIntent': False,
            'events': [],
            'conditionalResponses': [],
            'condition': '',
            'conditionalFollowupEvents': []
        }
        alias = followup
        if alias:
            root_json_data['responses'][0]['parameters'].append(
                {
                    'id': str(uuid.uuid4()),
                    'name': alias,
                    'required': True,
                    'dataType': '@' + alias,
                    'value': '$' + alias,
                    'defaultValue': '',
                    'isList': False,
                    'prompts': [],
                    'promptMessages': [],
                    'noMatchPromptMessages': [],
                    'noInputPromptMessages': [],
                    'outputDialogContexts': []
                }
            )
        root_json_data = json.dumps(root_json_data, indent=2)
        DialogFlowGenerator.write_to_file(intent_name + '.json', root_json_data)
        DialogFlowGenerator.generate_expression(intent_data = intent_data, alias = followup)
        
        # Now continue with children
        kwargs = []
        for i in range(len(children)):
            kwargs.append(children)
        
        followup_combinations =  [
            element for element in list(product(*kwargs)) \
            if len(list(set(element))) == len(children)
        ]

        children_dict = {}
        for child in children:
            child_name = intent_name + " - " + child
            child_json_data = {
                'id': str(uuid.uuid4()),
                'parentId': root_uuid,
                'rootParentId': root_uuid,
                'name': child_name,
                'auto': True,
                'contexts': [
                    root_context_name
                ],
                'responses': [
                    {
                        'resetContexts': False,
                        'action': root_unified_name + '.' + root_unified_name + '-custom',
                        'affectedContexts': [
                            {
                                'name': root_unified_name + '-' + child + '-followup',
                                'lifespan': 1
                            }
                        ],
                        'parameters': [],
                        'messages': [
                            {
                                'type': '0',
                                'title': '',
                                'textToSpeech': '',
                                'lang': 'en',
                                'condition': ''
                            }
                        ],
                        'speech': []
                    }
                ],
                'priority': 500000,
                'webhookUsed': False,
                'webhookForSlotFilling': False,
                'fallbackIntent': False,
                'events': [],
                'conditionalResponses': [],
                'condition': '',
                'conditionalFollowupEvents': []
            }

            children_dict[child] = child_json_data
            child_json_data = json.dumps(child_json_data, indent=2)
            DialogFlowGenerator.write_to_file(child_name + '.json', child_json_data)
            modified_intent_data = [child_name, intent_data_helper.get_shared_usersays(child_name,shared_usersays)]
            DialogFlowGenerator.generate_expression(intent_data = modified_intent_data, alias = followup)


        combination_dict = {}
        for combination in followup_combinations:
            current_index = 0
            parent = None
        
            for element in combination:
                if current_index == 0:
                    parent_data = children_dict[element]
                    current_index += 1
                    continue
      
                context = parent_data['responses'][0]['affectedContexts'][0]['name']
                context = context[:-1*(len('followup'))] + 'custom'

                combination_name = parent_data['name'] + ' - ' + element
                combination_data = {
                    'id' : str(uuid.uuid4()),
                    'parentId': parent_data['id'],
                    'rootParentId': root_uuid,
                    'name': combination_name,
                    'auto': True,
                    'contexts': [
                        parent_data['responses'][0]['affectedContexts'][0]['name'] 
                    ],
                    'responses': [
                        {
                            'resetContexts': False,
                            'action': parent_data['responses'][0]['action'] + '.' + context,
                            'affectedContexts': [],
                            'parameters': [],
                            'messages': [
                                {
                                    'type': 0,
                                    'title': '',
                                    'textToSpeech': '',
                                    'lang': 'en',
                                    'condition': ''
                                }
                            ],
                            'speech': []
                        }
                    ],
                    'priority': 500000,
                    'webhookUsed': False,
                    'webhookForSlotFilling': False,
                    'fallbackIntent': False,
                    'events': [],
                    'conditionalResponses': [],
                    'condition': '',
                    'conditionalFollowupEvents': []
                }

                if current_index != len(children) - 1:
                    combination_data['responses'][0]['affectedContexts'].append({
                        'name': ''.join(combination_name.split())  + '-followup',
                        'lifespan': 1
                    })

                combination_dict[combination_name] = combination_data
                parent_data = combination_data
                combination_data = json.dumps(combination_data, indent=2)
                DialogFlowGenerator.write_to_file(combination_name + '.json', combination_data)
                intents_data_helper = IntentsDataHelper()
                intent_data = [combination_name, intent_data_helper.get_shared_usersays(combination_name,shared_usersays)]
                DialogFlowGenerator.generate_expression(intent_data, alias = followup)
                current_index += 1
       
    @staticmethod
    def generate_intent(intent_name, alias):
        json_data = {
            'id': str(uuid.uuid4()),
            'name': intent_name,
            'auto': True,
            'contexts': [],
            'responses': [
                {
                    'resetContexts': False,
                    'action': '',
                    'affectedContexts': [],
                    'parameters': [],
                    'messages': [
                        {
                            'type': '0',
                            'title': '',
                            'textToSpeech': '',
                            'lang': 'en',
                            'condition': ''
                        }
                    ],
                    'speech': []
                }
            ],
            'priority': 500000,
            'webhookUsed': False,
            'webhookForSlotFilling': False,
            'fallbackIntent': False,
            'events': [],
            'conditionalResponses': [],
            'condition': '',
            'conditionalFollowupEvents': []
        }
        if alias:
            json_data['responses'][0]['parameters'].append(
                {
                    'id': str(uuid.uuid4()),
                    'name': alias,
                    'required': True,
                    'dataType': '@' + alias,
                    'value': '$' + alias,
                    'defaultValue': '',
                    'isList': False,
                    'prompts': [],
                    'promptMessages': [],
                    'noMatchPromptMessages': [],
                    'noInputPromptMessages': [],
                    'outputDialogContexts': []
                }
            )
        json_data = json.dumps(json_data, indent=2)
        DialogFlowGenerator.write_to_file(intent_name + '.json', json_data)

    @staticmethod
    def generate_expression(intent_data, alias=None):
        intent_name = intent_data[0]
        intent_expressions = intent_data[1]
        json_data = []
        for expression in intent_expressions:
            expression_data = {
                'id': str(uuid.uuid4()),
                'data': [],
                'isTemplate': False,
                "count": 0,
                "lang": "en",
                "updated": 0
            }
            if not alias:
                expression_data['data'].append(
                    {
                        "text": expression,
                        "userDefined": False
                    }
                )
            if alias:
                expression_parts = expression.split('$'+alias,1)
                expression_data['data'].append(
                    {
                        "text": expression_parts[0],
                        "userDefined": False
                    }
                )
                expression_data['data'].append(
                    {
                        "text": '$' + alias,
                        "meta": "@" + alias,
                        "alias": alias,
                        "userDefined": True
                    }
                )
                expression_data['data'].append(
                    {
                        "text": expression_parts[1],
                        "userDefined": False
                    }
                )                
            json_data.append(expression_data)

        json_data = json.dumps(json_data, indent=2)
        DialogFlowGenerator.write_to_file(intent_name + '_usersays_en.json', json_data)

    
    @staticmethod
    def write_to_file(filename, data):
        with open("./generated_intents/"+filename, "w") as output:
            output.write(data)


if __name__ == "__main__":
    intent_data_helper = IntentsDataHelper()
    CONFIG_DICTIONARIES_POLICY = {
        'simple': [simple_intents],
        'number': [simple_intents_with_entity_number],
        'course': [
            follow_up_intents_course,
            follow_up_intents_course1,
            follow_up_intents_course2,
            follow_up_intents_course3,
            follow_up_intents_course4,
            follow_up_intents_course5,
            follow_up_intents_course6,
            follow_up_intents_course7
        ], 
        'teacher': [follow_up_intents_teacher]
    }

    for generation_policy in CONFIG_DICTIONARIES_POLICY:
        for dictionary in CONFIG_DICTIONARIES_POLICY[generation_policy]:
            if generation_policy == 'simple':
                for intent in dictionary:
                    DialogFlowGenerator.generate_expression(
                        alias='',
                        intent_data=[intent,dictionary[intent]]
                    )
                    DialogFlowGenerator.generate_intent(
                        intent_name = intent,
                        alias=''
                    )    
            elif generation_policy == 'number':
                for intent in dictionary:
                    DialogFlowGenerator.generate_expression(
                        alias='number',
                        intent_data=[intent,dictionary[intent]]
                    )
                    DialogFlowGenerator.generate_intent(
                        intent_name = intent,
                        alias='number'
                    )       
            elif generation_policy == 'course':
                # import ipdb; ipdb.set_trace();
                for follow_up_intent in dictionary:
                    children = list(dictionary)
                    children.remove(follow_up_intent)
                    DialogFlowGenerator.generate_intent_with_followups(
                        intent_name = follow_up_intent,
                        children = children,
                        intent_data=[follow_up_intent,dictionary[follow_up_intent]],
                        followup = 'course_name',
                        shared_usersays = dictionary
                    )
            elif generation_policy == 'teacher':
                for follow_up_intent in dictionary:
                    children = list(dictionary)
                    children.remove(follow_up_intent)
                    DialogFlowGenerator.generate_intent_with_followups(
                        intent_name = follow_up_intent,
                        children = children,
                        intent_data=[follow_up_intent,dictionary[follow_up_intent]],
                        followup = 'teacher_name',
                        shared_usersays = dictionary
                    )