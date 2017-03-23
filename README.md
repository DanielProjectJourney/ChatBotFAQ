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

- Level 1: when confidence threshold (Similarity >= 75) more than 75%, it means chatbot can find the high-accuracy answer by

![image](http://i2.buimg.com/567571/f88ec484f0b10ba4.png)


- Level 2: when confidence between 40% and 75%(Similarity > 40). I use "Fuzzy Search Algorithm" to slected the top similiraty question. 

![image](http://i4.buimg.com/567571/1ef668b740414d2f.png)


- Level 3: when confidence less than 40%, it means chatbot couldn't find the proper answer for customer.

![image](http://i1.piimg.com/567571/0e406e8d792587eb.png)

---

# Performance Analysis
### Due to every text will be processed into 300 Vectors,  I serialise the vectors of every text into the faq_feats.pkl(Pickle File).

### When customer start chat, background process will implement the serilization. Then will display "Hi, I am Chat Robort. What Can I do for you?"

![image](http://i1.piimg.com/567571/29033dff7beefe64.png)
![image](http://i1.piimg.com/567571/ac55a5c1fdc45bc7.png)

## Caculate Reply Time (Between Java & Python)

1. Find the Answer

![image](http://i1.piimg.com/567571/1fe552952ec65a1a.png)

2. Know 

![image](http://i4.buimg.com/567571/61e83e1e4bd3b854.png)

## Contiune Deploy Analysis ....

---


# License
Author: Daniel Zhang [MIT License](http://www.opensource.org/licenses/MIT)

<img src="http://i2.buimg.com/567571/65205e085388d236.png" width="50%" height="50%">
