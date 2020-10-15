from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app.logger.info("Button was pressed by client.")
        return render_template('submission.html')
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
