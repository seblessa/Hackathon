from flask import Flask, request, render_template
from pp import model
from chatgui import faz_tudo

app = Flask(__name__)

# Create a list to hold the messages
messages = []


# Define a route to handle the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the message from the form and add it to the list of messages
        message = request.form['message']
        if message:
            messages.append(('sender', message))
            # Call the model function to get the response

            response = faz_tudo(message)
            if response is None:
                print("PP")
                response = model(message)
            else:
                print("chatbot")
            messages.append(('receiver', response))

    # Render the template with the messages
    return render_template('index.html', messages=messages)


def main():
    app.run()
