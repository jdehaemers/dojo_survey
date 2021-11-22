from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'kjadjhakjkjhakjZEWw'

fields = []
languages = ['Python', 'JavaScript', 'HTML', 'C++', 'C#']

@app.route('/')
def survey():
    global languages
    print(languages)
    return render_template('survey.html', languages = languages)

@app.route('/process', methods=['POST'])
def process():
    global fields
    fields = []
    for i in request.form:
        fields.append(i)
        session[i] = request.form[i]
    print(session)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', fields = fields)

if __name__ == '__main__':
    app.run(debug=True)