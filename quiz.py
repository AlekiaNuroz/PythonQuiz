import json
import random
import requests
from os import system, name 
from time import sleep

def clear_screen(): 

    """ 
    Clears the console screen based on the operating system. 

    This function checks the operating system and executes the appropriate command to clear the console: 
    - On Windows systems, it runs the "cls" command. 
    - On other systems (e.g., Linux, macOS), it runs the "clear" command. 
 
    Side Effects: 
        - Executes a system command to clear the terminal screen. 
    """ 

    if name == "nt": 
        system("cls") 
    else: 
        system("clear")

def html_specialchars_decode(text):
    """
    Converts HTML special characters to their keyboard equivalents.

    Args:
        text (str or list of str): The input string or a list of strings containing HTML special characters.

    Returns:
        str or list of str: If the input is a string, returns the string with HTML special characters
        converted to their keyboard equivalents. If the input is a list of strings, returns a new list
        with each string having HTML special characters converted.

    Raises:
        TypeError: If the input is neither a string nor a list of strings.
    """
    replacements = {
        "&quot;": '"',
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#039;": "'",
    }

    def decode_string(s):
        """Helper function to decode a single string."""
        for key, value in replacements.items():
            s = s.replace(key, value)
        return s

    if isinstance(text, str):
        return decode_string(text)
    elif isinstance(text, list):
        return [decode_string(s) for s in text]
    else:
        raise TypeError("Input must be a string or a list of strings.")

def json_to_tuples(json_data):
    """
    Converts JSON data containing quiz questions into a list of tuples.

    Args:
        json_data (dict): The JSON data containing the quiz questions, typically fetched from an API.

    Returns:
        list of tuple: A list of tuples where each tuple contains the following elements:
        (question, difficulty, category, correct_answer, incorrect_answers).
    """
    data = json_data
    results = data.get('results', [])
    tuples = []

    for result in results:
        question = html_specialchars_decode(result.get('question'))
        difficulty = result.get('difficulty')
        category = result.get('category')
        correct_answer = html_specialchars_decode(result.get('correct_answer'))
        incorrect_answers = html_specialchars_decode(result.get('incorrect_answers'))
        tuples.append((question, difficulty, category, correct_answer, incorrect_answers))

    return tuples

# URL for the Open Trivia Database API.
api_url = "https://opentdb.com/api.php?amount=10&type=multiple"

try:
    # Attempt to fetch questions from the API.
    response = requests.get(api_url)
    questions = json_to_tuples(response.json())
except ConnectionError:
    # If unable to connect, load default questions.
    print("Unable to connect to API. Loading default questions...")
    questions = [
        ('General Knowledge', 'Easy', 'What is the name of the Jewish New Year?', 'Rosh Hashanah', ['Elul', 'New Year', 'Succoss']),
        ('General Knowledge', 'Medium', 'Which river flows through the Scottish city of Glasgow?', 'Clyde', ['Tay', 'Dee', 'Tweed']),
        ('General Knowledge', 'Easy', 'What is the French word for "fish"?', 'poisson', ['fiche', 'escargot', 'mer']), 
        ('General Knowledge', 'Hard', 'Sciophobia is the fear of what?', 'Shadows', ['Eating', 'Bright lights', 'Transportation']), 
        ('General Knowledge', 'Hard', 'Which film star has his statue in Leicester Square?', 'Charlie Chaplin', ['Paul Newman', 'Rowan Atkinson ', 'Alfred Hitchcock']), 
        ('General Knowledge', 'Hard', 'Originally another word for poppy, coquelicot is a shade of what?', 'Red', ['Green', 'Blue', 'Pink']), 
        ('General Knowledge', 'Easy', 'What is Tasmania?', 'An Australian State', ["A flavor of Ben and Jerry's ice-cream", 'A Psychological Disorder', 'The Name of a Warner Brothers Cartoon Character']), 
        ('General Knowledge', 'Hard', 'What is the romanized Korean word for "heart"?', 'Simjang', ['Aejeong', 'Jeongsin', 'Segseu']), 
        ('General Knowledge', 'Medium', 'What was the original name of the search engine "Google"?', 'BackRub', ['CatMassage', 'SearchPro', 'Netscape Navigator']), 
        ('General Knowledge', 'Hard', 'In the MMO RPG "Realm of the Mad God", what dungeon is widely considered to be the most difficult?', "The Shatter's", ['Snake Pit', "The Tomb of the Acient's", "The Puppet Master's Theater"])
    ]

# Initialize the score and shuffle the questions for randomness.
score = 0
num_questions = len(questions)
random.shuffle(questions)

# Iterate through each question and present it to the user.
for category, difficulty, question, correct_answer, incorrect_answers in questions:
    clear_screen()

    print(f"\nCategory: {category}")
    print(f"Difficulty: {difficulty}")
    print(f"\n{question}")

    # Combine correct and incorrect answers, then shuffle them.
    all_answers = incorrect_answers + [correct_answer]
    random.shuffle(all_answers)
    
    # Display the shuffled answers.
    print(f"a) {all_answers[0]}")
    print(f"b) {all_answers[1]}")
    print(f"c) {all_answers[2]}")
    print(f"d) {all_answers[3]}")

    # Prompt the user for their answer.
    user_answer = input("\nEnter your answer: ")

    # Determine the correct answer's letter.
    correct_answer_index = all_answers.index(correct_answer)
    correct_answer_letter = chr(ord('a') + correct_answer_index)
    
    if user_answer.lower() == correct_answer_letter:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is {correct_answer_letter}) {correct_answer}")
    
    sleep(1)

clear_screen()

# Display the final score.
print(f"\nYou scored {score} out of {num_questions}.")