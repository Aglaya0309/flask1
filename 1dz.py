from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_current_time():

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Текущее время</title>
        <meta charset="utf-8">
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                text-align: center;
                margin-top: 50px;
            }}
            .time {{
                font-size: 2em;
                color: #333;
                padding: 20px;
                background-color: #f0f0f0;
                border-radius: 10px;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <h1>Текущие дата и время</h1>
        <div class="time">{current_time}</div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)