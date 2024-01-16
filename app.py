from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donate():
    if request.method == 'POST':
        amount = request.form['amount']
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process the donation data (you can save it to a database)
        print(f'Donation: Amount - {amount}, Name - {name}, Email - {email}, Message - {message}')

        return render_template('thank_you.html', name=name, amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
