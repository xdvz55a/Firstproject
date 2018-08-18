from flask import Flask, request, send_from_directory
 
# set the "static" directory as the static folder.
# this will ensure that all the static files are under one folder
# This is a test of the webhook
# Test 9. 
app = Flask(__name__, static_url_path='/static')
 
# serving some static html files
@app.route('/html/<path:path>')
def send_html(path):
	return send_from_directory('static', path)

@app.route('/upload', methods=['POST'])
def upload_file():
	req_data = request.get_json()
	fileApp = req_data['fileApp']
	print fileApp
	print request.files
	# checking if the file is present or not.
	#if 'fileApp' not in request.files:
	#	return "No file found"
 
	file = request.files['file']
	#file = req_data['fileApp']
	print file
	file.save("/Users/letor/Desktop/python_tests/html/newfile.png")
	return "file successfully saved"

@app.route('/uploadfile', methods=['PUT'])
def upload_file2():
 
	print request.files
	# checking if the file is present or not.
	if 'file' not in request.files:
		return "No file found"
	 
	file = request.files['file']
	file.save("/Users/letor/Desktop/python_tests/html/hello33.txt")
	return "file successfully saved"
 
if __name__ == "__main__":
	app.run()



# https://sourcedexter.com/python-rest-api-flask-part-2/
# sample call http://localhost:5000/html/test.html
