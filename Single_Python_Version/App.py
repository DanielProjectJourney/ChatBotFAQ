from ChatBot import *

serialize()

chatbot = ChatBot()
data = list(faqs.keys())
with open('faq_feats.pkl', 'rb') as f:
        feats = pickle.load(f)

input_results = chatbot.input_question(data, feats)
new_data = input_results[0]
new_feats = input_results[1]
distance_matrix = chatbot.calculate_distances(new_feats)
idx = 0
chatbot.similarity_text(idx, distance_matrix, new_data)
