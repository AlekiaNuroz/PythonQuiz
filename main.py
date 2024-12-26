import json

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

  data = json.loads(json_data)
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

raw_json_data = '{"response_code":0,"results":[{"type":"multiple","difficulty":"easy","category":"General Knowledge","question":"What is the name of the Jewish New Year?","correct_answer":"Rosh Hashanah","incorrect_answers":["Elul","New Year","Succoss"]},{"type":"multiple","difficulty":"medium","category":"General Knowledge","question":"Which river flows through the Scottish city of Glasgow?","correct_answer":"Clyde","incorrect_answers":["Tay","Dee","Tweed"]},{"type":"multiple","difficulty":"easy","category":"General Knowledge","question":"What is the French word for &quot;fish&quot;?","correct_answer":"poisson","incorrect_answers":["fiche","escargot","mer"]},{"type":"multiple","difficulty":"hard","category":"General Knowledge","question":"Sciophobia is the fear of what?","correct_answer":"Shadows","incorrect_answers":["Eating","Bright lights","Transportation"]},{"type":"multiple","difficulty":"hard","category":"General Knowledge","question":"Which film star has his statue in Leicester Square?","correct_answer":"Charlie Chaplin","incorrect_answers":["Paul Newman","Rowan Atkinson ","Alfred Hitchcock"]},{"type":"multiple","difficulty":"hard","category":"General Knowledge","question":"Originally another word for poppy, coquelicot is a shade of what?","correct_answer":"Red","incorrect_answers":["Green","Blue","Pink"]},{"type":"multiple","difficulty":"easy","category":"General Knowledge","question":"What is Tasmania?","correct_answer":"An Australian State","incorrect_answers":["A flavor of Ben and Jerry&#039;s ice-cream","A Psychological Disorder","The Name of a Warner Brothers Cartoon Character"]},{"type":"multiple","difficulty":"hard","category":"General Knowledge","question":"What is the romanized Korean word for &quot;heart&quot;?","correct_answer":"Simjang","incorrect_answers":["Aejeong","Jeongsin","Segseu"]},{"type":"multiple","difficulty":"medium","category":"General Knowledge","question":"What was the original name of the search engine &quot;Google&quot;?","correct_answer":"BackRub","incorrect_answers":["CatMassage","SearchPro","Netscape Navigator"]},{"type":"multiple","difficulty":"hard","category":"General Knowledge","question":"In the MMO RPG &quot;Realm of the Mad God&quot;, what dungeon is widely considered to be the most difficult?","correct_answer":"The Shatter&#039;s","incorrect_answers":["Snake Pit","The Tomb of the Acient&#039;s","The Puppet Master&#039;s Theater"]}]}'

print(json_to_tuples(raw_json_data))