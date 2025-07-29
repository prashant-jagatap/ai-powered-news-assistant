"""CLI simulator for testing Alexa intents locally"""

import json
from typing import Dict, Any

class AlexaSimulator:
    def __init__(self):
        self.session_data = {}
    
    def simulate_intent(self, intent_name: str, slots: Dict[str, str] = {}) -> Dict[str, Any]:
        """Simulate an Alexa intent request"""
        formatted_slots = {slot_name: {"value": value} for slot_name, value in slots.items()}

        request = {
            "type": "IntentRequest",
            "intent": {
                "name": intent_name,
                "slots": formatted_slots or {}
            },
            "session": {
                "user": {"userId": "test_user_123"}
            }
        }
        return request

if __name__ == "__main__":
    sim = AlexaSimulator()
    
    # Test our intents
    news_request = sim.simulate_intent("GetDailyNewsBriefingIntent")
    print("News Request:", json.dumps(news_request, indent=2))
    
    manage_request = sim.simulate_intent("ManageSourcesIntent", {"source": "BBC"})
    print("Manage Request:", json.dumps(manage_request, indent=2))