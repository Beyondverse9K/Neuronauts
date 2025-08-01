# -*- coding: utf-8 -*-
"""FirstClass.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y08SUnLaoXLXXhOdb2gtbybb_Fm-4Rgd

Step 1: Install required packages
"""

!pip install google-generativeai --quiet
!pip install ipywidgets --quiet. #create a beautiful UI

"""Step 2: Import libraries"""

import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown

"""Step 3: Set up Gemini API"""

API_KEY = "***************************************"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

"""Step 4: Define the input form"""

topic_input = widgets.Text(
    description = "Topic",
    layout = widgets.Layout(width = '400px')
)

tone_input = widgets.Dropdown(
    description = "Tone",
    options = ['Professional', 'Casual', 'Motivational', 'Informative'],
    layout = widgets.Layout(width = '400px')
)

audience_input = widgets.Text(
    description = "Audience",
    layout = widgets.Layout(width = '400px')
)


hashtag_input = widgets.Text(
    description = "Hashtags",
    layout = widgets.Layout(width = '400px')
)

submit_button = widgets.Button(
    description = "Generate Tweet",
    button_style = 'Success',
    tooltip = 'click to generate tweet',
    layout = widgets.Layout(width = '400px')
)

output = widgets.Output()

"""Step 5: Generate Tweet Function"""

def generate_tweet(b):
  output.clear_output()
  prompt = f"""
  You are an expert Content Writer
  generate a tweet about the topic "{topic_input.value}".
  use a tone {tone_input.value}.
  generate tweet for audience {audience_input.value}.
  Include the hashtags {hashtag_input.value}.
  Keep it under 280 characters
  """
  with output:
    try:
      response = model.generate_content(prompt)
      tweet = response.text.strip()
      display(Markdown(f"### Generated Tweet : \n\n {tweet} "))
    except Exception as e:
      print("Error", e)


submit_button.on_click(generate_tweet)

"""Step 6: Display the form"""

form = widgets.VBox([
    widgets.HTML(value="<h3>📝 Tweet Generator Agent</h3>"),
    topic_input,
    tone_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])

display(form)