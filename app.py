from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_bruno():
    return '''
    <html>
    <head>
        <style>
            body {
                background-color: yellow; /* Set background to yellow */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            .scroll-text {
                white-space: nowrap;
                font-size: 24px;
                font-weight: bold;
                color: black;
                position: absolute;
                animation: scroll 10s linear infinite;
            }
            @keyframes scroll {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
        </style>
    </head>
    <body>
        <marquee><img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" alt="Docker Logo"></marquee>
        <div class="scroll-text">Hello Bruno, This is a Simple Flask application running on Jenkins Server.</div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
