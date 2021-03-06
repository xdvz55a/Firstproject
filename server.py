# http://flask.pocoo.org/docs/patterns/fileuploads/
# sample call curl   -F "userid=1"   -F "filecomment=This is an image file"   -F "file=@/Users/XXXXX/Downloads/okta-aspnetcore-mvc-example-master.zip;type=application/zip"  http://127.0.0.1:5000/release/app01
import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/letor/Desktop/python_tests/html/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/<stage>/<appid>', methods=['GET', 'POST', 'PUT'])
def upload_file(stage,appid):
    print "11"
    if request.method == 'POST':
        print stage
        print appid
        file = request.files['file']
        print file
        if file and allowed_file(file.filename):
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # for browser, add 'redirect' function on top of 'url_for'
            return url_for('uploaded_file',
                                    filename=filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
	app.run(debug=True)
