"""Alexa intent handlers"""

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components.request_components import AbstractRequestHandler
from ask_sdk_core.utils.predicate import is_intent_name

class GetDailyNewsBriefingHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("GetDailyNewsBriefingIntent")(handler_input)
    
    def handle(self, handler_input):
        speech_text = "Here's your daily news briefing: [Mock summary of top headlines]"
        
        return handler_input.response_builder.speak(speech_text).response

class ManageSourcesHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("ManageSourcesIntent")(handler_input)
    
    def handle(self, handler_input):
        # Get slot value
        slots = handler_input.request_envelope.request.intent.slots
        source = slots.get("source", {}).get("value", "unknown source")
        
        speech_text = f"I've updated your news sources to include {source}"
        
        return handler_input.response_builder.speak(speech_text).response

# Skill builder
sb = SkillBuilder()
sb.add_request_handler(GetDailyNewsBriefingHandler())
sb.add_request_handler(ManageSourcesHandler())

lambda_handler = sb.lambda_handler()