from flask import Flask, render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = 'kristajona_'
# our index route will handle rendering our form

@app.route('/users', methods=['POST'])
def create_user():
    print('got post info')
        
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # print(request.form)
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/show')
# def show_user():
#     return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)

