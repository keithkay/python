# Python Crash Course
#
# Chapter 11 - Testing
#
# This is the function to be tested by test_survey.py

class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_questions(self):
        """Show the survey question."""
        print(question)
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the survey responses."""
        print("Survey results:")
        for response in responses:
            print('- ' + response)