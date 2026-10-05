from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This stores our character data simply
    name = "Spider-Man"
    real_name = "Peter Parker"
    backstory = (
        "Bitten by a radioactive spider, teenager Peter Parker gained extraordinary abilities. "
        "After the tragic loss of his Uncle Ben, he dedicated his life to protecting New York City, "
        "learning that with great power comes great responsibility."
    )

    # This creates the visual layout for Mu to display
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Marvel Character Database</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; }}
            .card {{ background: white; padding: 30px; border-radius: 10px; max-width: 500px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
            h1 {{ color: #e62429; margin-top: 0; }}
            h3 {{ color: #333; border-bottom: 2px solid #e62429; padding-bottom: 5px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{name}</h1>
            <p><strong>Real Name:</strong> {real_name}</p>

            <h3>Backstory</h3>
            <p>{backstory}</p>

            <h3>Core Powers</h3>
            <ul>
                <li><strong>Wall-Crawling:</strong> Can cling to solid surfaces.</li>
                <li><strong>Spider-Sense:</strong> Pre-cognitive danger warning.</li>
                <li><strong>Superhuman Agility:</strong> Enhanced reflexes and strength.</li>
            </ul>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    # This starts the website on your local computer
    app.run(debug=True)

