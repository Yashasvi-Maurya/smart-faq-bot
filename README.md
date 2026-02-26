# Smart FAQ bot

A simple AI-inspired FAQ chatbot built using python.
It matches user questios with stored FAQs using keyword similarity and provides relevant answers.

------

## Features 

- Keyword-based questions matching 
- Case-insensitive input handling 
- Stop-word removal for smarter matching 
- Saves unanswered questions for future improvement 
- URL detection handling 
- Clean and structured modular code 

------

## Technologies Used 

- Python
- JSON (for storing FAQ data)
- File handling (to log unanswered questions)

------

## Project Stucture

Smart-faq-bot/
|
|-----main.py
|
|-----faq_data.json
|
|-----unanswered.txt
|
|-----README.md
|


## How to Run

1. Clone the repository:
   git clone <your-repo-link>

2. Navigate into the project folder:
   cd smart-faq-bot

3. Run the chatbot:
   python main.py


----


## Example

you: what is the registration fee 
Bot: The registration fees is 500 rupees.

you: where is the venue 
bot: The event will be held at NITRA Technical Campus.

you: random question
Bot: Sorry, I don't understand your question.

-----


## Future Improvements 

- Use NLP libraries like NLTK or spaCy
- Implement fuzzy matching 
- Add GUI using Tkinter
- Deploy as a web app using Flask
- Integrate real AI API


-----


## Author 

Built by Yashasvi Maurya 



