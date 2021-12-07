from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.english_to_french(textToTranslate)
    french_text = ''
    if translation:
        french_text = translation['translations'][0]['translation']
    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.french_to_english(textToTranslate)
    english_text = ''
    if translation:
        english_text = translation['translations'][0]['translation']
    return english_text

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
