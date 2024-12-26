import json
import random
import requests

def html_specialchars_decode(text):
  """
  Converts HTML special characters to their keyboard equivalents.

  Args:
    text: The input string or a list of strings containing HTML special characters.

  Returns:
    If the input is a string, returns the string with HTML special characters 
    converted to their keyboard equivalents. 
    If the input is a list of strings, returns a new list with each string 
    having HTML special characters converted.
  """
  replacements = {
      "&quot;": '"',
      "&amp;": "&",
      "&lt;": "<",
      "&gt;": ">",
      "&#039;": "'",
  }

  def decode_string(s):
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
    json_data: The JSON data containing the quiz questions.

  Returns:
    A list of tuples, where each tuple represents a question and its details:
      (question, correct_answer, incorrect_answers)
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

api_url = "https://opentdb.com/api.php?amount=10&type=multiple"

try:
    response = requests.get(api_url)
    questions = json_to_tuples(response.json())
except ConnectionError:
    print("Unable to connect to API. Loading default questions...")
    questions = [('General Knowledge', 'Easy', 'What is the name of the Jewish New Year?', 'Rosh Hashanah', ['Elul', 'New Year', 'Succoss']),
                 ('General Knowledge', 'Medium', 'Which river flows through the Scottish city of Glasgow?', 'Clyde', ['Tay', 'Dee', 'Tweed']),
                 ('General Knowledge', 'Easy', 'What is the French word for "fish"?', 'poisson', ['fiche', 'escargot', 'mer']), 
                 ('General Knowledge', 'Hard', 'Sciophobia is the fear of what?', 'Shadows', ['Eating', 'Bright lights', 'Transportation']), 
                 ('General Knowledge', 'Hard', 'Which film star has his statue in Leicester Square?', 'Charlie Chaplin', ['Paul Newman', 'Rowan Atkinson ', 'Alfred Hitchcock']), 
                 ('General Knowledge', 'Hard', 'Originally another word for poppy, coquelicot is a shade of what?', 'Red', ['Green', 'Blue', 'Pink']), 
                 ('General Knowledge', 'Easy', 'What is Tasmania?', 'An Australian State', ["A flavor of Ben and Jerry's ice-cream", 'A Psychological Disorder', 'The Name of a Warner Brothers Cartoon Character']), 
                 ('General Knowledge', 'Hard', 'What is the romanized Korean word for "heart"?', 'Simjang', ['Aejeong', 'Jeongsin', 'Segseu']), 
                 ('General Knowledge', 'Medium', 'What was the original name of the search engine "Google"?', 'BackRub', ['CatMassage', 'SearchPro', 'Netscape Navigator']), 
                 ('General Knowledge', 'Hard', 'In the MMO RPG "Realm of the Mad God", what dungeon is widely considered to be the most difficult?', "The Shatter's", ['Snake Pit', "The Tomb of the Acient's", "The Puppet Master's Theater"])]

score = 0
num_questions = len(questions)

# Shuffle the questions for a random order.
random.shuffle(questions)

for category, difficulty, question, correct_answer, incorrect_answers in questions:
    print(f"\nCategory: {category}")
    print(f"Difficulty: {difficulty}")
    print(f"\n{question}")

    # Shuffle the answer choices for each question
    all_answers = incorrect_answers + [correct_answer]
    random.shuffle(all_answers)
    
    print(f"a) {all_answers[0]}")
    print(f"b) {all_answers[1]}")
    print(f"c) {all_answers[2]}")
    print(f"d) {all_answers[3]}")

    user_answer = input("\nEnter your answer: ")

    correct_answer_index = all_answers.index(correct_answer)
    correct_answer_letter = chr(ord('a') + correct_answer_index)
    
    if user_answer.lower() == correct_answer_letter:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct anser is {correct_answer_letter}) {correct_answer}")
    
print(f"\nYou scored {score} out of {num_questions}.")
