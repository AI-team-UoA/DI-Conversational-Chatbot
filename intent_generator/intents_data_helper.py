import sys
sys.path.append('../config')
from Intents import follow_up_intents_course, follow_up_intents_teacher

class IntentsDataHelper:

    # The followup intents: grade_course, ects_course - grade_course, ects_course - staff_course - grade_course 
	# have the same behavior, so they can be handled like grade_course
    def get_shared_usersays(self, filename, dictionary):
        filename_parts = filename.split('-')
        ending_indent = filename_parts[-1].strip()
        for intent_key in dictionary.keys():
            filename_parts = intent_key.split('-')
            ending_key_intent = filename_parts[-1].strip()
            if ending_indent == ending_key_intent:
                return dictionary[intent_key]