from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/download')

def homePage():
    return render_template('download.html')

@app.route('/admin')

def aboutPage():
    return render_template('admin.html')
    
if __name__ == '__main__':
    app.run(debug=True)
