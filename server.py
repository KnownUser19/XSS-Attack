from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load the HTML template
template = open('index.html').read()

@app.route('/')
def index():
    return render_template_string(template, comment='')

@app.route('/submit', methods=['POST'])
def submit():
    comment = request.form.get('comment')
    # Directly render user input without sanitization (vulnerable)
    return render_template_string(template, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
