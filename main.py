import json

# -------------------------------
# Load FAQ Data
# -------------------------------
def load_faq_data():
    with open("faq_data.json", "r") as file:
        return json.load(file)

# -------------------------------
# Clean User Input
# -------------------------------
def clean_input(user_input):
    return user_input.lower().strip()

# -------------------------------
# Remove Common Stop Words
# -------------------------------
def remove_stopwords(text):
    stop_words = {"is", "the", "what", "where", "how", "a", "an", "of", "to"}
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# -------------------------------
# Find Best Matching Question
# -------------------------------
def find_best_match(user_input, questions):
    highest_score = 0
    best_match = None

    user_words = set(remove_stopwords(user_input))

    for question in questions:
        question_words = set(remove_stopwords(question.lower()))
        score = len(user_words & question_words)

        if score > highest_score:
            highest_score = score
            best_match = question

    return best_match if highest_score > 0 else None

# -------------------------------
# Save Unanswered Questions
# -------------------------------
def save_unanswered(question):
    with open("unanswered.txt", "a") as file:
        file.write(question + "\n")

# -------------------------------
# Main Chatbot Logic
# -------------------------------
def chatbot():
    faq_data = load_faq_data()
    questions = faq_data.keys()

    print("==============================")
    print("      SMART FAQ BOT 🤖")
    print("==============================")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        user_input = clean_input(user_input)

        if user_input == "exit":
            print("Bot: Thank you! Have a great day.")
            break

        if user_input.startswith("http"):
            print("Bot: Please ask a valid question, not a URL.")
            continue

        match = find_best_match(user_input, questions)

        if match:
            print("Bot:", faq_data[match])
        else:
            print("Bot: Sorry, I don't understand your question.")
            save_unanswered(user_input)

# Run the bot
chatbot()