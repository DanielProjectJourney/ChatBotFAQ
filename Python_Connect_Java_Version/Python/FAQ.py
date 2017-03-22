from ChatBot import *
class FAQ(object):


    def __init__(self, question = None ,answer = None):
        self.question = question
        self.answer = answer

    #Serilize the String into Pickle File
    def serialize(self):
        serialize()

    def setQuestion(self, question = None ):
        self.question = question

    def getQuestion(self):
        return self.question

    # Chatbot will analysis the question, then return the Answer
    def setAnswer(self, question = None):
        if self.question:
            chatbot = ChatBot()
            print("I am here")
            data = list(faqs.keys())
            with open('faq_feats.pkl', 'rb') as f:
                    feats = pickle.load(f)
            input_results = chatbot.input_question(data, feats, self.question)
            new_data = input_results[0]
            new_feats = input_results[1]
            distance_matrix = chatbot.calculate_distances(new_feats)
            idx = 0
            self.answer = chatbot.similarity_text(idx, distance_matrix, new_data)
        else:
            self.answer = "Please tell me what can I do for you?"

    def getAnswer(self):
        return self.answer

    #Connect to the Java File
    class Java:
        implements = ["py4j.examples.Chatbot"]

# Make sure that the python code is started first.
# Then execute: java -cp py4j.jar py4j.examples.SingleThreadClientApplication
from py4j.java_gateway import JavaGateway, CallbackServerParameters
faq = FAQ()

#Start the Python Server and Connect Java By Port: 25334 (Default)
gateway = JavaGateway(callback_server_parameters=CallbackServerParameters(),python_server_entry_point=faq)
