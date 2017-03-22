# Fast Chat Robot Java Connect to Python

---
## Inspired By Indico Blog Article ["Building a Bot to Answer FAQs: Predicting Text Similarity"](https://indico.io/blog/faqs-bot-text-features-api/) & [Py4j](https://www.py4j.org/) & ["Fuzzy String Matching in Python By Marco Bonzanini"](https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/)


![image](http://i4.buimg.com/567571/8429a9ca09bf8760.png)



> Java Files

- Chatbot.java: For Clients to input the question.

- FAQ.java(Interface): All method will be implemented by python. Yeah, You are not in dream. Python will decide how to implement these method.

> Python Files

- ChatBot.py (Core Algorithm): 
    
    1. Indico’s Text Features API to find all the feature vectors for the text data.
    2. Cosine distance is the most reasonable metric for comparison of these 300d vectors By cdista of Scipy.
    3. Fuzzy Search by [Levenshtein distance](https://github.com/seatgeek/fuzzywuzzy) 
    

- FAQ.py : Connect to Java (Chatbot.java) and implemented the methods of FAQ.java 



> Bridge:

Java | Python
---|---
FAQ.java | FAQ.py




---
# Core Algorithm

![image](http://i4.buimg.com/567571/74907be0ac9b9c55.png)

- Level 1: when confidence threshold (Similarity >= 75) more than 75%, it means chatbot can find the high-accuracy answer by ![image](http://i2.buimg.com/567571/f88ec484f0b10ba4.png)
- Level 2: when confidence between 40% and 75%(Similarity > 40). I use "Fuzzy Search Algorithm" to slected the top similiraty question. 

![image](http://i4.buimg.com/567571/1ef668b740414d2f.png)


- Level 3: when confidence less than 40%, it means chatbot couldn't find the proper answer for customer.

![image](http://i1.piimg.com/567571/0e406e8d792587eb.png)


## Contiune Deploy Analysis ....