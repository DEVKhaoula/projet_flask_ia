from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""

    if request.method == 'POST':
        prompt = request.form.get('prompt')

        if prompt:
            try:
                ollama_response = requests.post(
                    'http://localhost:11434/api/generate',
                    json={
                        "model": "llama3.2",
                        "prompt": prompt,
                        "stream": False
                    }
                )

                if ollama_response.status_code == 200:
                    data = ollama_response.json()
                    response_text = data.get('response', 'No response')
                else:
                    response_text = "Erreur API Ollama"

            except Exception as e:
                response_text = f"Erreur : {str(e)}"

    return render_template("index.html", response_text=response_text)


if __name__ == '__main__':
    app.run(debug=True)