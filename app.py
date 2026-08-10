from flask import Flask, render_template
from cube import Cube

# 1. Create the server
app = Flask(__name__)

# 2. Initialize your Python brain
my_python_cube = Cube()

# 3. Create the route that serves the HTML page
@app.route('/')
def dome():
    # This automatically looks inside the 'templates' folder for index.html
    return render_template('index.html')

if __name__ == '__main__':
    # Run the server!
    app.run(debug=True)