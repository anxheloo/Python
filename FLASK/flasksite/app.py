from flask import Flask, redirect, url_for, request,render_template, make

#We need to create an app with a name
app = Flask(__name__)



# @app.route('/')
# def index():
# 	return render_template('hello.html')



# @app.route('/welcome/<username>')
# def passingDataToTemplates(username):
# 	return render_template('hello.html', name = username)


# @app.route('/')
# def student():
# 	return render_template('student.html')


# @app.route('/result', methods= ['POST','GET'])
# def result():
# 	if request.method == 'POST':
# 		# this extracts all the data that are stored in the form
# 		result = request.form

# 		#we save the value result we use in html, at result value we created to save the extracted values
# 		return render_template('result.html', result = result)


# Using Cookies
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/setcookie', methods= ['POST','GET'])
def setcookie():
	if request.method == 'POST':
		user = request.form['nm'] #we store the user attribute which is called 'nm' 

		resp = make_response(render_template('readcookie.html'))
		resp.set_cookie('userID',user)

		return resp



@app.route('/getcookie')
def getcookie():
	name = request.cookies.get('userID')
	return '<h1>Hello ' + name + ' </h1>'




#To run this app
if __name__ == '__main__':
	app.run()

