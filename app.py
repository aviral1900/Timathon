import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = f'{os.getcwd()}/uploads'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/<name>')
def uploaded(name):
    cap = ""
    with open(f"uploads/{name}.txt", "r") as f:
        cap += f.read()
    return render_template('index_after_upload.html', content=cap, img_name=name)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    ll = os.listdir(UPLOAD_FOLDER)
    for ele in ll:
        os.remove(UPLOAD_FOLDER + "/"+ ele)
    fpath = UPLOAD_FOLDER+"image.jpg"
    if os.path.exists(fpath):
        os.remove(fpath)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',filename=filename))

            with open(f"uploads/{filename}.txt", "w") as f:
                f.write("This is the Caption")
            return redirect(url_for('uploaded', name=filename))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
