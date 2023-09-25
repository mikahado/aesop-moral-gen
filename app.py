import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read the content of the input.txt file
with open("story.txt", "r") as file:
    input_text = file.read()

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # animal = request.form["animal"]
        # Use the content of the input.txt file in your custom prompt generation
        prompt = generate_prompt(input_text)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=300
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(input_text):
    return f"""{input_text}

Summarize the moral of the story above in 280 characters or less for elementary school students with accessibility needs. Use lots of playful, meaningful emojis to assist in reading comprehension. 
""".format(
        input_text.capitalize()
    )

if __name__ == "__main__":
    app.run()

# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))

#     result = request.args.get("result")
#     return render_template("index.html", result=result)



# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )
