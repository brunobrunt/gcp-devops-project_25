from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_bruno():
    return '''
    <html>
    <head>
        <style>
            body {
                background-color: yellow;
                margin: 0;
                padding: 0;
                overflow-x: hidden;
                font-family: Arial, sans-serif;
            }
            .fixed-text {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                color: black;
                margin-top: 20px;
            }
            .scrolling-image {
                position: relative;
                width: 100%;
                overflow: hidden;
                margin-top: 50px;
            }
            .scrolling-image img {
                position: absolute;
                width: 200px; /* You can adjust the size */
                animation: scrollImage 10s linear infinite;
            }
            @keyframes scrollImage {
                0% {
                    left: 100%;
                }
                100% {
                    left: -200px; /* Match the width of the image */
                }
            }
        </style>
    </head>
    <body>
        <div class="fixed-text">Hello Bruno, This is a Simple Flask application running on Jenkins Server.</div>

        <div class="scrolling-image">
            <img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" alt="Docker Logo">
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
